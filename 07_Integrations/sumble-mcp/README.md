# Local Sumble MCP server

This is a local, read-only MCP server for Sumble's REST API. It exposes organization search and enrichment, people search, job search, and technology lookup.

## Setup

1. Create a Sumble API key at <https://sumble.com/account/api-keys>.
2. Set it in the environment used to launch the server:

```sh
export SUMBLE_API_KEY="your-key"
```

3. Add this server to the local MCP configuration used by Codex:

```json
{
  "mcpServers": {
    "sumble-local": {
      "command": "python3",
      "args": ["/absolute/path/to/repository/07_Integrations/sumble-mcp/sumble_mcp_server.py"],
      "env": {
        "SUMBLE_API_KEY": "${SUMBLE_API_KEY}"
      }
    }
  }
}
```

Keep the API key in your shell or secret manager. Do not commit it to this repository.

## Available tools

- `sumble_find_organizations`: search by Sumble filters
- `sumble_enrich_organization`: enrich an organization
- `sumble_find_people`: find people at an organization
- `sumble_find_jobs`: find relevant job postings
- `sumble_find_technologies`: resolve technology names and slugs

The server uses Sumble's v3 API and passes through the API response, including credit fields when Sumble returns them. The default result limit is 10 and the maximum is 100.
