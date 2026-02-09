print("Starting imports...")
try:
    import requests
    print("requests imported")
    import smtplib
    print("smtplib imported")
    import schedule
    print("schedule imported")
    import nltk
    print("nltk imported")
    from newspaper import Article
    print("newspaper imported")
except Exception as e:
    print(f"Import failed: {e}")
print("Done.")
