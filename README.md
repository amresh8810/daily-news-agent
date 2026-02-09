# Daily AI News Agent 🤖📰

This is a Python-based AI Agent that fetches the latest news on a specific topic (default: "Artificial Intelligence"), summarizes it, and emails a daily digest to your inbox.

It uses the **ScrapingDog API** to fetch news from Google News and **SMTP** to send emails via Gmail.

## Features
- 🔍 **Fetches News**: get the latest stories on any topic you choose.
- 📧 **Automated Emails**: Sends a clean, HTML-formatted email digest.
- ⏰ **Scheduled**: Runs automatically every day at 8:00 AM.
- 🔒 **Secure**: Keeps your API keys and passwords safe in a local configuration file.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/amresh8810/daily-news-agent.git
cd daily-news-agent
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Secrets (Critical Step!)
Since passwords and API keys should never be shared publicly, you need to create a `secrets_config.py` file in the project folder.

1.  Create a new file named `secrets_config.py`.
2.  Add the following content to it, replacing the placeholders with your actual details:

```python
# secrets_config.py

# TOPIC: What kind of news do you want?
NEWS_TOPIC = "Artificial Intelligence"

# API KEY for ScrapingDog (Get one at scrapingdog.com)
SCRAPINGDOG_API_KEY = "your_scrapingdog_api_key_here"

# EMAIL CONFIG
# For Gmail, you MUST use an App Password, not your login password.
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_16_char_app_password"
RECEIVER_EMAIL = "your_email@gmail.com"
```

### 4. Run the Agent
```bash
python news_agent.py
```
The agent will perform an immediate check to confirm everything is working, and then it will keep running to send you news every day at 8:00 AM.
