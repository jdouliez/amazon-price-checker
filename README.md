# Tool
* Scraps amazon url webpage 
* Get item price 
* Send email if price is under threshold


# Installation
```
pip3 install -r requirements.txt
```

# Configuration
Edit file and add `SMTP_SERVER`, `SMTP_PORT`, `SMTP_LOGIN`, `SMTP_PWD` and `EMAIL_TO`


# Automation
```
(crontab -l 2>/dev/null; echo "0 * * * * python3 ~/amazon-scraper.py "<AMAZON_ITEM_URL>" <AMAZON_ITEM_THRESHOLD_PRICE> >> amazon-prices.txt 2>&1") | crontab -
```
