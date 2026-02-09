import requests 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

# --- CONFIGURATION ---
# We keep our secrets in a separate file (secrets_config.py)
# so they don't get accidentally uploaded to GitHub.
try:
    import secrets_config
except ImportError:
    print("CRITICAL ERROR: secrets_config.py not found!")
    print("Please create a file named 'secrets_config.py' with your API keys and emails.")
    exit(1)

NEWS_TOPIC = getattr(secrets_config, "NEWS_TOPIC", "Technology")
SCRAPINGDOG_API_KEY = getattr(secrets_config, "SCRAPINGDOG_API_KEY", "")
SENDER_EMAIL = getattr(secrets_config, "SENDER_EMAIL", "")
SENDER_PASSWORD = getattr(secrets_config, "SENDER_PASSWORD", "")
RECEIVER_EMAIL = getattr(secrets_config, "RECEIVER_EMAIL", "")

if not SCRAPINGDOG_API_KEY or not SENDER_PASSWORD:
    print("ERROR: API Key or Password missing in secrets_config.py")
    exit(1)

def fetch_and_summarize_news(topic="Technology", limit=3):
    """
    Fetches news from ScrapingDog Google News API.
    Uses the snippet provided by the API as the summary (AI summarization removed for stability).
    """
    print(f"DEBUG: Fetching news for {topic} using ScrapingDog...")
    
    # ScrapingDog Google News API URL
    url = f"https://api.scrapingdog.com/google_news/v2?api_key={SCRAPINGDOG_API_KEY}&query={topic}&country=us"
    
    try:
        response = requests.get(url)
        data = response.json()
    except Exception as e:
        print(f"Error fetching data from ScrapingDog: {e}")
        return []

    news_items = []
    
    if isinstance(data, list):
        entries = data
    elif "news_results" in data:
        entries = data["news_results"]
    else:
        print("Unknown API response structure:", data.keys() if isinstance(data, dict) else data)
        entries = []

    count = 0
    for entry in entries:
        if count >= limit:
            break
            
        try:
            title = entry.get("title", "No Title")
            link = entry.get("link", "")
            snippet = entry.get("description", "") 
            
            if not link:
                continue

            print(f" - Found article: {title}")
            
            # Use the snippet as the summary
            summary = snippet if snippet else "No summary available."
            
            news_items.append({
                "title": title,
                "link": link,
                "summary": summary
            })
            count += 1
            
        except Exception as e:
            print(f"Error processing item: {e}")
            continue
            
    return news_items

def format_email_body(news_items):
    """Formats the news items into a nice HTML email body."""
    html_content = f"<h1>Daily {NEWS_TOPIC} News Brief</h1>"
    
    for item in news_items:
        html_content += f"""
        <div style="margin-bottom: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
            <h3><a href="{item['link']}">{item['title']}</a></h3>
            <p>{item['summary']}</p>
        </div>
        """
    
    html_content += "<p><em>Sent by your Python News Agent</em></p>"
    return html_content

def send_email(subject, body_html):
    """Sends the email using Gmail SMTP."""
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = subject

        msg.attach(MIMEText(body_html, 'html'))

        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def job():
    """The main job to run daily."""
    print("Starting daily news job...")
    news = fetch_and_summarize_news(NEWS_TOPIC, limit=5)
    if news:
        body = format_email_body(news)
        send_email(f"Your Daily {NEWS_TOPIC} Brief", body)
    else:
        print("No news found.")

if __name__ == "__main__":
    print("News Agent is running...")
    print(f"Tracking topic: {NEWS_TOPIC}")
    print("It will check for news every day at 08:00 AM.")
    
    # 1. Schedule the job (e.g., every day at 8:00 AM)
    schedule.every().day.at("08:00").do(job)
    
    # FOR TESTING: Run immediately
    print("Performing immediate startup check...")
    job() 
    
    # Keep the script running
    while True:
        schedule.run_pending()
        time.sleep(60)
