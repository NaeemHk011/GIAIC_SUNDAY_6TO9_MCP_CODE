"""
server.py  —  FastMCP Weather Server
======================================
This is our MCP Server.
It has 2 tools that the Agent will use.

agent.py starts this server automatically — no need to run it separately.
"""

from fastmcp import FastMCP

# ── Create the server ─────────────────────────────────────────
mcp = FastMCP("Weather Server")


# ── Tool 1: Get weather of a city ────────────────────────────
@mcp.tool
def get_weather(city: str) -> str:
    """Returns the weather of any city"""
    data = {
        "karachi":   "🌤️  35°C · Sunny · Very hot",
        "lahore":    "⛅  28°C · Cloudy · Cool weather",
        "islamabad": "🌥️  22°C · Clear · Very pleasant",
        "peshawar":  "☀️  31°C · Hot · Quite hot",
    }
    result = data.get(city.lower())
    if result:
        return f"{city} weather: {result}"
    return f"Sorry, {city} is not available. Try: Karachi, Lahore, Islamabad, Peshawar"


# ── Tool 2: List available cities ────────────────────────────
@mcp.tool
def get_available_cities() -> str:
    """Returns the list of cities with available weather data"""
    return "Available cities: Karachi, Lahore, Islamabad, Peshawar"


if __name__ == "__main__":
    mcp.run(transport="stdio")