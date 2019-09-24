'''
trying another way
'''
import smtplib
from datetime import date

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from .config import EMAIL_FUNCTION_PW, EMAIL_FUNCTION_ID


def create_content(data_id: str, data_content: str, block_type: str) -> str:
    '''
    description:            create html content to be used to substitute
                            specific values in full email html using jinja

    param:                  data_id: this could be the block_id or the channel
                                     title in the case of block info

                            data_content: block_content, or block add date.

                            block_type: either 'Text', or 'Info', the rest
                                        are considered media.

    return:                 a string representation of the html code to be
                            used to substitute in using jinja
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


def send_email(html_content: str) -> None:
    '''
    description:            given html content / a html file in string format,
                            send an email

    param:                  html_content: the content of the email to be sent

    return:                 N/A
    '''
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 're.are.na / {0}/{1}'.format(
        date.today().month,
        date.today().day
    )
    msg['From'] = EMAIL_FUNCTION_ID
    msg['To'] = EMAIL_FUNCTION_ID

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

    mail.login(EMAIL_FUNCTION_ID, EMAIL_FUNCTION_PW)
    mail.sendmail(EMAIL_FUNCTION_ID, EMAIL_FUNCTION_ID, msg.as_string())
    mail.quit()
