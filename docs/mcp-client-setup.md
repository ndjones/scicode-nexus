# MCP Client Setup for Cognee MCP Server

The Cognee MCP server is available at `http://localhost:8002/mcp` when running via Docker Compose.

## Claude CLI

To add the Cognee MCP server to Claude CLI:

```bash
claude mcp add cognee-http -t http http://localhost:8002/mcp
```

Verify the connection:

```bash
claude mcp list
```

You should see:
```
Checking MCP server health...

cognee-http: http://localhost:8002/mcp (HTTP) - ✓ Connected
```

## Cursor

To add the Cognee MCP server to Cursor, edit your `~/.cursor/mcp.json` file to include:

```json
{
  "mcpServers": {
    "cognee-http": {
      "url": "http://localhost:8002/mcp"
    }
  }
}
```

Then restart Cursor and check the MCP server status in the settings.

## Roo Code

To add the Cognee MCP server to Roo Code, edit your Roo Code MCP configuration (likely in `.roo/mcp.json` or similar) to include:

```json
{
  "mcpServers": {
    "cognee-http": {
      "url": "http://localhost:8002/mcp"
    }
  }
}
```

Then restart Roo Code and check the MCP server status.

## Manual Configuration

If you are using another MCP client, you can manually configure it to connect to:
- Type: HTTP
- URL: http://localhost:8002/mcp

## Notes

- Make sure the Docker Compose services are running: `docker compose up -d`
- The Cognee MCP server depends on the `db` and `cognee` services, so they will be started automatically.
- If you encounter connection issues, check the logs of the cognee-mcp service: `docker compose logs cognee-mcp`