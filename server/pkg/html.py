'''
html waiting to be subbed
'''

JINJA_HTML = '''
<html>
  <head></head>
  <body style="font-family: Arial; font-size: 28px; width: 600px;">
  <br>
    <table cellspacing="0" cellpadding="1" width="100%" margin-top="25px">
      <tr>
        <td width="100%">
          <div id='rectangle'  style="
            width: 600px;
            height: 100px;
            border: 3px solid #A4E4A1;
            margin-bottom: 25px;
            color: #17AC10;"
          >
            <p id='header-title' style="
              font-size: 28px;
              margin-left: 60px;
              float: left;
              font-weight: bold;
              text-decoration: none;
              ">
              <a href='https://www.github.com/adi-txt/re.are.na'
                 style="text-decoration: none;">
                <span style="color: #17AC10; text-decoration: none;">
                  re.are.na
                </span>
              </a>
            </p>
            <p id='header-blocks' style="
              margin-left: 60px;
              float: left;
              font-size: 16px;
              margin-top: 39px;
              ">
                3 blocks
            </p>
            <p id='header-author' style="
              font-size: 16px;
              float: right;
              margin-top: 39px;
              margin-right: 39px;
            ">
              <a href='https://are.na/adi' style="
                color: #17AC10;
                text-decoration: none;
              ">
                <span style="color: #17AC10">by adi /</span>
              </a>
            </p>
          </div>
        </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <div id='header-info'>
          <p id='header-info-text' style="
            font-size: 18px;
            color: #AEAEAE;
            margin-bottom: 0;
          ">Info</p>
        </div>
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <hr style="
          border-color: #E5E5E5;
          background-color: #E5E5E5;
          color: #E5E5E5;
          width: 50%;
          float: left;
          height: 1px;
          border: 0;"
        >
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <p id='header-info-description' style="
          font-size: 18px;
          color: #9A9696;
          margin-top: 0;
          text-decoration: none;
          "> <span style="text-decoration: none;">Three blocks picked at
            random from your <a href='https://www.are.na' style="color: #9A9696; text-decoration: none;">are.na</a> profile.</span>
        </p>
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <div id='block-1' style="
          border: 3px solid #F6F6F6;
          width: 600px;
          height: 600px;
          margin-top: 8%;
        ">
          {{ block1 }}
        </div>
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <div id='block-1-info' style="
            font-size: 18px;
        ">
          {{ block1_info }}
        </div>
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <div id='block-2' style="
          border: 3px solid #F6F6F6;
          width: 600px;
          height: 600px;
          margin-top: 8%;
        ">
          {{ block2 }}
        </div>
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <div id='block-1-info' style="
            font-size: 18px;
        ">
          {{ block2_info }}
        </div>
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <div id='block-3' style="
          border: 3px solid #F6F6F6;
          width: 600px;
          height: 600px;
          margin-top: 8%;
        ">
          {{ block3 }}
        </div>
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <div id='block-1-info' style="
            font-size: 18px;
        ">
          {{ block3_info }}
        </div>
      </td>
      </tr>
    </table>
    <table cellspacing="0" cellpadding="1" width="100%">
      <tr>
      <td>
        <div>
          <footer style="
            font-size: 16px;
            margin-top: 10%;
            margin-bottom: 10%;
            color: #9A9696;
          ">
            see you tomorrow,<br><br>-A
          </footer>
        </div>
      </td>
      </tr>
    </table>
  </body>
</html>
'''
