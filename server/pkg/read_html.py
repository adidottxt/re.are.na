'''
reading in email content from .html file
'''
import codecs
import os

HTML_DIR = ''.join([os.getcwd(), '/pkg/html/'])

READ_HTML = codecs.open(''.join([HTML_DIR, 'final.html']), 'r')
FINAL_HTML = READ_HTML.read()

READ_JINJA_HTML = codecs.open(''.join([HTML_DIR, 'final.html']), 'r')
FINAL_JINJA_HTML = READ_JINJA_HTML.read()
