# How to Setup Your Daily AI News Agent

This guide will help you setup your AI Agent step-by-step.

## Step 1: Install Dependencies (If not already done)
Open your terminal/command prompt and run:
`pip install -r requirements.txt`

## Step 2: Get your Gmail App Password
Currently, Google does not allow using your regular password for apps due to security. You need an "App Password".

1.  Go to your **Google Account Settings**.
2.  Search for **"App Passwords"** (or go to Security > 2-Step Verification > App Passwords). 
    *   *Note: You must have 2-Step Verification enabled first.*
3.  Create a new app password. 
    *   Select App: **Mail**
    *   Select Device: **Windows Computer**
4.  It will generate a 16-character password (e.g., `abcd efgh ijkl mnop`). Copy this.

## Step 3: Configure the Script
1.  Open the file `news_agent.py` in your code editor (VS Code, Notepad++, etc).
2.  Find the lines at the top:
    ```python
    SENDER_EMAIL = "your_email@gmail.com"
    SENDER_PASSWORD = "your_app_password" 
    RECEIVER_EMAIL = "your_email@gmail.com"
    ```
3.  Replace `your_email@gmail.com` with your Gmail address.
4.  Replace `your_app_password` with the 16-character code you copied (keep the quotes!).

## Step 4: Run the Agent!
Open your terminal and run:
`python news_agent.py`

If everything is correct, you should see:
`DEBUG: Fetching news for Artificial Intelligence...`
And then receive an email shortly after!

## Step 5: Automate it (Make it Daily)
Right now, the script runs once and stops. To make it run daily:

1.  Open `news_agent.py`.
2.  Uncomment the scheduler lines at the bottom:
    ```python
    schedule.every().day.at("08:00").do(job)
    
    while True:
        schedule.run_pending()
        time.sleep(60)
    ```
3.  Run the script again. Leave the terminal window open, and it will send emails every day at 8:00 AM.
