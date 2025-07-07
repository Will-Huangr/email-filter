# email-filter MCP Server

A simple MCP server for filtering spam emails using the DeepSeek API.

This project provides a "tool" that can be called by an MCP host. The tool analyzes email content and returns a judgment on whether it's spam.

## What is MCP?

MCP (Model Context Protocol) is a protocol that allows a host application to discover and use "tools" provided by separate server processes. This allows for creating modular and language-independent extensions. For more details, check out the [MCP specification](https://modelcontextprotocol.io/introduction).

## Requirements

- Python 3.10+
- DeepSeek API key

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Will-Huangr/email-filter.git
   cd email-filter
   ```

2. **Install dependencies:**
   ```bash
   pip install "mcp[cli]" httpx
   ```

3. **Get your DeepSeek API key:**
   Sign up and get your API key from [DeepSeek Platform](https://platform.deepseek.com/)

4. **Configure the MCP client:**
   Add this configuration to your MCP client settings (e.g., Claude Desktop config):
   ```json
   {
     "email-filter": {
       "command": "python3",
       "args": [
         "<path_to_email_filter>/email_filter.py"
       ],
       "env": {
         "DEEPSEEK_API_KEY": "<your_deepseek_api_key>"
       }
     }
   }
   ```
   Replace `<path_to_email_filter>` with the actual path to your email-filter directory and `<your_deepseek_api_key>` with your actual API key.

## Usage

Run the server with the built-in stdio transport, which allows it to communicate over standard input/output.

```bash
python email_filter.py
```

The server will start and wait for an MCP host to connect and call its tools.

## MCP Tool: `filter_email`

- **Description:** Analyzes email content to determine if it's spam and provides a summary.
- **Input:** `email_content: str` - The full content of the email, including headers, sender, and body.
- **Output:** `str` - The analysis result from the DeepSeek model.

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

## Integration

### Using with Cursor Desktop
1. After configuring the MCP server, restart Cursor Desktop.
2. You can now use the `filter_email` tool directly in your conversations within Cursor.
   <img width="730" alt="image" src="https://github.com/user-attachments/assets/55c9ffc5-8b1a-4f29-9047-14538ba7fead" />

4. Example: "Please analyze this email for spam: [paste email content]"

### Using with other MCP clients
Refer to your MCP client documentation for connecting via stdio transport.

## License

MIT License - see LICENSE file for details.
