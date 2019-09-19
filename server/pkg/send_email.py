'''
trying another way
'''
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from read_html import FINAL_HTML
from config import PW, EMAIL

# Create message container - the correct MIME type is multipart/alternative.
MSG = MIMEMultipart('alternative')
MSG['Subject'] = "Link"
MSG['From'] = EMAIL
MSG['To'] = EMAIL

# Record the MIME types of both parts - text/plain and text/html.
PART1 = MIMEText(FINAL_HTML, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
MSG.attach(PART1)

# Send the message via local SMTP server.
MAIL = smtplib.SMTP('smtp.gmail.com', 587)

MAIL.ehlo()
MAIL.starttls()

MAIL.login(EMAIL, PW)
MAIL.sendmail(EMAIL, EMAIL, MSG.as_string())
MAIL.quit()
