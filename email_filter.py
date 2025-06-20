from typing import Any
import os
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("email-filter")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"

async def call_deepseek(user_question: str) -> str:
    if not DEEPSEEK_API_KEY:
        return "DeepSeek API key not set in environment variable DEEPSEEK_API_KEY."
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
    }
    payload = {
        "model": "deepseek-reasoner",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert at detecting spam. Analyze the following email content and determine if it is spam. Provide a brief explanation for your reasoning.",
            },
            {"role": "user", "content": user_question},
        ],
        "max_tokens": 1024,
    }
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.post(DEEPSEEK_API_URL, headers=headers, json=payload, timeout=30.0)
            resp.raise_for_status()
            data = resp.json()
            return data["choices"][0]["message"].get("content", "No content found in response.")
        except Exception as e:
            return f"Error calling DeepSeek API: {e}"

@mcp.tool()
async def filter_email(email_content: str) -> str:
    """分析邮件内容是否为垃圾邮件，并给出总结和说明。\n\nArgs:\n    email_content: 用户提供的邮件内容，可能包含发件人/标题/正文\n"""
    result = await call_deepseek(email_content)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio") 