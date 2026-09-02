#!/usr/bin/env python3
"""Local, read-only MCP server for the Sumble REST API."""

import json
import os
import sys
import urllib.error
import urllib.request
from typing import Any, Dict


SERVER_NAME = "sumble-local"
SERVER_VERSION = "0.1.0"
API_BASE = "https://api.sumble.com/v3"


TOOLS = [
    {
        "name": "sumble_find_organizations",
        "description": "Find organizations using Sumble firmographic, industry, job-function, or technology filters.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "filters": {"type": "object", "description": "Sumble organization filters."},
                "limit": {"type": "integer", "minimum": 1, "maximum": 100, "default": 10},
                "offset": {"type": "integer", "minimum": 0, "maximum": 10000, "default": 0},
            },
            "required": ["filters"],
            "additionalProperties": False,
        },
    },
    {
        "name": "sumble_enrich_organization",
        "description": "Check whether an organization matches specified Sumble technologies or enrichment filters.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "organization": {"type": "object", "description": "Organization identifier, such as {domain: 'example.com'}."},
                "filters": {"type": "object", "description": "Sumble enrichment filters."},
            },
            "required": ["organization", "filters"],
            "additionalProperties": False,
        },
    },
    {
        "name": "sumble_find_people",
        "description": "Find people at an organization by role, seniority, job function, or related filters.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "organization": {"type": "object", "description": "Organization identifier, such as {domain: 'example.com'}."},
                "filters": {"type": "object", "description": "Sumble people filters."},
                "limit": {"type": "integer", "minimum": 1, "maximum": 100, "default": 10},
                "offset": {"type": "integer", "minimum": 0, "maximum": 10000, "default": 0},
            },
            "required": ["filters"],
            "additionalProperties": False,
        },
    },
    {
        "name": "sumble_find_jobs",
        "description": "Find job postings by organization, technology, date, team, or job-function filters.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "organization": {"type": "object", "description": "Optional organization identifier."},
                "filters": {"type": "object", "description": "Sumble job filters."},
                "limit": {"type": "integer", "minimum": 1, "maximum": 100, "default": 10},
                "offset": {"type": "integer", "minimum": 0, "maximum": 10000, "default": 0},
            },
            "required": ["filters"],
            "additionalProperties": False,
        },
    },
    {
        "name": "sumble_find_technologies",
        "description": "Look up Sumble technology names and slugs for use in organization or job filters.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "query": {"type": "string", "description": "Technology name or partial name."},
            },
            "required": ["query"],
            "additionalProperties": False,
        },
    },
]


def respond(request_id: Any, result: Dict[str, Any]) -> None:
    message = {"jsonrpc": "2.0", "id": request_id, "result": result}
    sys.stdout.write(json.dumps(message, separators=(",", ":")) + "\n")
    sys.stdout.flush()


def error(request_id: Any, code: int, message: str) -> None:
    respond(request_id, {"error": {"code": code, "message": message}})


def api_request(path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.environ.get("SUMBLE_API_KEY")
    if not api_key:
        raise RuntimeError("SUMBLE_API_KEY is not set")

    body = json.dumps(payload).encode("utf-8")
    request = urllib.request.Request(
        f"{API_BASE}/{path}",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "sumble-local-mcp/0.1.0",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Sumble API returned HTTP {exc.code}: {detail[:500]}") from exc
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Could not reach Sumble API: {exc.reason}") from exc


def call_tool(name: str, args: Dict[str, Any]) -> Dict[str, Any]:
    if name == "sumble_find_organizations":
        payload = {"filters": args["filters"], "limit": args.get("limit", 10), "offset": args.get("offset", 0)}
        return api_request("organizations/find", payload)
    if name == "sumble_enrich_organization":
        return api_request("organizations/enrich", {"organization": args["organization"], "filters": args["filters"]})
    if name == "sumble_find_people":
        payload = {"filters": args["filters"], "limit": args.get("limit", 10), "offset": args.get("offset", 0)}
        if "organization" in args:
            payload["organization"] = args["organization"]
        return api_request("people/find", payload)
    if name == "sumble_find_jobs":
        payload = {"filters": args["filters"], "limit": args.get("limit", 10), "offset": args.get("offset", 0)}
        if "organization" in args:
            payload["organization"] = args["organization"]
        return api_request("jobs/find", payload)
    if name == "sumble_find_technologies":
        return api_request("technologies/find", {"query": args["query"]})
    raise ValueError(f"Unknown tool: {name}")


def handle(request: Dict[str, Any]) -> None:
    request_id = request.get("id")
    method = request.get("method")
    params = request.get("params") or {}

    if method == "initialize":
        respond(request_id, {
            "protocolVersion": params.get("protocolVersion", "2024-11-05"),
            "capabilities": {"tools": {}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        })
    elif method == "notifications/initialized":
        return
    elif method == "ping":
        respond(request_id, {})
    elif method == "tools/list":
        respond(request_id, {"tools": TOOLS})
    elif method == "tools/call":
        try:
            result = call_tool(params.get("name", ""), params.get("arguments") or {})
            respond(request_id, {"content": [{"type": "text", "text": json.dumps(result, indent=2)}], "structuredContent": result})
        except (KeyError, TypeError, ValueError, RuntimeError) as exc:
            respond(request_id, {"content": [{"type": "text", "text": str(exc)}], "isError": True})
    else:
        error(request_id, -32601, f"Method not found: {method}")


def main() -> None:
    for line in sys.stdin:
        if line.strip():
            try:
                handle(json.loads(line))
            except json.JSONDecodeError as exc:
                error(None, -32700, f"Invalid JSON: {exc}")


if __name__ == "__main__":
    main()
