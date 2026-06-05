import asyncio

from google.adk.tools import McpToolset
from google.adk.tools.mcp_tool.mcp_toolset import (
    ToolArgsConfig,
)

async def main():
    toolset = McpToolset.from_config(
        ToolArgsConfig(
            stdio_server_params={
                "command": "npx",
                "args": ["@zereight/mcp-gitlab"],
                "env": {
                    "GITLAB_PERSONAL_ACCESS_TOKEN": "PUT_YOUR_PAT_HERE"
                }
            }
        ),
        "."
    )

    tools = await toolset.get_tools()

    print("\nAvailable tools:\n")
    for tool in tools:
        print(tool.name)

asyncio.run(main())