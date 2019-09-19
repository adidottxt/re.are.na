'''
reading in email content from .html file
'''
import codecs

READ_HTML = codecs.open('html/final.html', 'r')
FINAL_HTML = READ_HTML.read()
