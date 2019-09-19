'''
trying another way
'''
import smtplib
from datetime import date

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from pkg.config import PW, EMAIL

def create_content(data_id, data_content, block_type) -> str:
    '''
    create html content to sub in
    '''
    if block_type == 'Text':
        return "<a href='https://are.na/block/{0}' style=' text-decoration: \
            none;'><div style='display: -webkit-box; -webkit-line-clamp: 20; \
            -webkit-box-orient: vertical; margin: 50px; overflow: hidden; \
            word-wrap: break-word; color: #9A9696; object-fit: contain; \
            text-decoration: none; font-size: 18px;'>{1}</div></a>".format(
                data_id,
                data_content
            )
    if block_type == 'Info':
        return '<br><p style="color: #9A9696;"><b>channel&nbsp;&nbsp;/&nbsp;\
            &nbsp;</b>{0}</p><p style="color: #9A9696; margin-top:-5px;"><b>\
            add date&nbsp;&nbsp;/&nbsp;&nbsp;</b>{1}</p><br>'.format(
                data_id,
                data_content
            )
    return "<a href='https://are.na/block/{0}'><img src='{1}' style='\
        height: 100%; width: 100%; object-fit: contain;'/></a>".format(
            data_id,
            data_content
        )


def send_email(html_content) -> None:
    '''
    send email!
    '''
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 're.are.na / {0}/{1}'.format(
        date.today().month,
        date.today().day
    )
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
