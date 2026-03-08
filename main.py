from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from dotenv import load_dotenv
import os
import asyncio
# from agents import enable_verbose_stdout_logging

# enable_verbose_stdout_logging()
load_dotenv()  # .env file se environment variables load karo

async def main():
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ OPENAI_API_KEY set nahi hai!")
        print("   PowerShell mein chalao:")
        print('   $env:OPENAI_API_KEY = "sk-xxxxxxxxxxxx"')
        return
    
    print("🚀 Weather Agent starting...\n")

    async with MCPServerStdio(
    params={"command": "uv", "args": ["run", "server.py"]}
    ) as mcp_server:

        print("✅ Connected to MCP Server!\n")

        agent = Agent(
            name="personal ai Assistant",
            instructions="""
            tum mere personal ai ho jo kam kahunga krogy tools use kr skty ho mcp server use kr skty ho zrort parne per
            """,
            mcp_servers=[mcp_server]
        )

        result = await Runner.run(
            agent,
            input="tmhary pas konsa weather available he?"
        )
        print(f"🤖 Agent: {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())




