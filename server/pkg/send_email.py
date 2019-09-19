'''
trying another way
'''
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pkg.config import PW, EMAIL

def create_content(block_id, block_content, block_type) -> str:
    '''
    create html content to sub in
    '''
    if block_type == 'Text':
        return "<a href='https://are.na/block/{0}' style='text-decoration: none;'><div style='\
            overflow: hidden; word-wrap: break-word; color: #9A9696;\
            object-fit: contain; text-decoration: none;'>{1}</div></a>".format(
                block_id,
                block_content
            )
    return "<a href='https://are.na/block/{0}'><img src='{1}' style='\
        height: 100%; width: 100%; object-fit: contain;'/></a>".format(
            block_id,
            block_content
        )


def send_email(html_content) -> None:
    '''
    send email!
    '''
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = EMAIL
    msg['To'] = EMAIL

    # Record the MIME types of both parts - text/plain and text/html.
    content = MIMEText(html_content, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(content)

    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()
    mail.starttls()

    mail.login(EMAIL, PW)
    mail.sendmail(EMAIL, EMAIL, msg.as_string())
    mail.quit()
