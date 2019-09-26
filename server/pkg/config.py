'''
config file
'''

import os

from os.path import join, dirname, abspath
from dotenv import load_dotenv

DOTENV_PATH = join(
    os.path.abspath(dirname(dirname(dirname(abspath(__file__))))),
    '.env'
)

load_dotenv(DOTENV_PATH)

ACCESS_TOKEN = str(os.getenv('ACCESS_TOKEN'))
ARENA_USERNAME = str(os.getenv('ARENA_USERNAME'))
EMAIL_FUNCTION_PW = str(os.getenv('EMAIL_FUNCTION_PW'))
EMAIL_FUNCTION_ID = str(os.getenv('EMAIL_FUNCTION_ID'))
