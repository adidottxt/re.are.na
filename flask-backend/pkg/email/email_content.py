import codecs

f = codecs.open('table-final.html', 'r')
FINAL_HTML = f.read()

HTML = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a style='color: red' href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>
"""

# FINAL_HTML = '''\
# <html>
#   <head></head>
#   <body>
#     <div id='rectangle' width: 100px height: 50px border: 3px solid #A4E4A1>
#       <p id='header-title'>re.are.na</p>
#       <p id='header-blocks'>3 blocks</p>
#       <p id='header-author'>
#         <a href='https://are.na/adi'>by adi /
#         </a>
#       </p>
#     </div>
#   </body>
# </html>
# '''

# TEXT = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
