import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from youtube_api_call import *

EMAIL_ID = os.environ.get('EMAIL_ID')
EMAIL_PASS = 'kgskerxacgyysafr'

message = MIMEMultipart("alternative")
message['From'] = EMAIL_ID
message['To'] = EMAIL_ID
message['Subject'] = "Youtube Videos to watch this week"

# Getting the results from Youtube API call, code present in other file
API_KEY, CHANNEL_ID, EXTRACTED_DATA, YOUTUBE = config()
df = get_channel_details(API_KEY, CHANNEL_ID, EXTRACTED_DATA, YOUTUBE)
df_most_viewed, df_max_view_count_records = fetching_most_viewed_videos(df)

df_most_viewed = df_most_viewed.to_html(index=False)
df_max_view_count_records = df_max_view_count_records.to_html(index=False)

html = f"""
<html>
  <head></head>
  <body>
    <h2>Hey Kanishk,</h2>
    <h2>Your weekly YouTube video updates are ready:</h2>
    <h3>1. Top 5 Videos from Your Preferred Channels</h3>
    {df_most_viewed}<br><br>
    <h3>2. Most Watched Videos from Each Channel</h3>
    {df_max_view_count_records}
  </body>
</html>
"""

part = MIMEText(html, 'html')

# Encode file in ASCII characters to send by email
#encoders.encode_base64(part)

# Add attachment to message
message.attach(part)

context = ssl.create_default_context()

try:
  with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

    smtp.starttls(context=context)    
    smtp.login(EMAIL_ID, EMAIL_PASS)
    smtp.sendmail(EMAIL_ID, EMAIL_ID, message.as_string())

except Exception as e:
  print("An exception occurred while sending the mail {}".format(e))