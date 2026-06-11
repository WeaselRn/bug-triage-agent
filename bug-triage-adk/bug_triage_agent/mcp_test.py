import asyncio
import os

from google.adk.tools import McpToolset
from google.adk.tools.mcp_tool.mcp_toolset import ToolArgsConfig


async def main():
    print("Connecting to GitLab MCP server...\n")

    toolset = McpToolset.from_config(
        ToolArgsConfig(
            stdio_server_params={
                "command": "npx",
                "args": ["@zereight/mcp-gitlab"],
                "env": {
                    **os.environ,
                    "GITLAB_PERSONAL_ACCESS_TOKEN": os.getenv(
                        "GITLAB_PERSONAL_ACCESS_TOKEN", ""
                    ),
                },
            }
        ),
        ".",
    )

    tools = await toolset.get_tools()

    print(f"\nFound {len(tools)} tools:\n")

    for i, tool in enumerate(tools, start=1):
        try:
            print(f"{i}. {tool.name}")
        except Exception:
            print(f"{i}. {tool}")

    print("\nDone.")


if __name__ == "__main__":
    asyncio.run(main())