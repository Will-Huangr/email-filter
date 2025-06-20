# email-filter MCP Server

A simple MCP server for filtering spam emails using the DeepSeek API.

This project provides a "tool" that can be called by an MCP host. The tool analyzes email content and returns a judgment on whether it's spam.

## What is MCP?

MCP (Massively-parallel Compute Protocol) is a protocol that allows a host application to discover and use "tools" provided by separate server processes. This allows for creating modular and language-independent extensions. For more details, check out the MCP specification (you might want to add a link here if one is available).

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/email-filter.git
    cd email-filter
    ```

2.  **Install dependencies:**
    This project uses `uv` for environment and package management.
    ```bash
    # Create the virtual environment
    uv venv

    # Activate the environment
    source .venv/bin/activate

    # Install dependencies from pyproject.toml
    uv pip install -e .
    ```

3.  **Set your DeepSeek API key:**
    You need to get an API key from [DeepSeek](https://platform.deepseek.com/).
    ```bash
    export DEEPSEEK_API_KEY='your_deepseek_api_key_here'
    ```

## Usage

Run the server with the built-in stdio transport, which allows it to communicate over standard input/output.

```bash
uv run email_filter.py
```

The server will start and wait for an MCP host to connect and call its tools.

## MCP Tool: `filter_email`

-   **Description:** Analyzes email content to determine if it's spam and provides a summary.
-   **Input:** `email_content: str` - The full content of the email, including headers, sender, and body.
-   **Output:** `str` - The analysis result from the DeepSeek model.

### Example

**Input `email_content`:**
```
From: "Urgent Notification" <no-reply@suspicious.com>
Subject: Your account has been compromised!

Dear user, we have detected suspicious activity on your account. Please click the link below immediately to verify your identity and secure your account. http://very-real-bank-not-a-scam.com/login
```

**Example Output:**
```
This is likely a spam email. It uses common phishing tactics such as an urgent and alarming subject line, a generic greeting, and a suspicious link. The sender's email address is also a red flag.
```

## MCP Tool

- **filter_email(email_content: str) -> str**
  - 输入: 邮件内容（可包含发件人/标题/正文）
  - 输出: DeepSeek 分析结果，判断是否为垃圾邮件并给出总结说明

## Integration

Refer to your MCP client or host documentation for how to connect to this server via stdio. 