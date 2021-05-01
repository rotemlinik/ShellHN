import logging

# consts
NUM_OF_TOP_STORIES = 40
SECONDS_IN_HOUR = 3600
HOUR_FOR_CALC = 20
MIDNIGHT = 24
PROXIMITY_COLUMN = 'publish_proximity_to_8pm'
COMMENTS_AMOUNT_COLUMN = 'comments_amount'
COMMENT_CONTENT_KEY = 'text'
COMMENTS_IDS_KEY = 'kids'
TITLE_KEY = 'title'
COMMENTS_AMOUNT_KEY = 'descendants'
PUBLISH_TIME_KEY = 'time'
ID_KEY = 'id'
HN_BASE_URL = "https://hacker-news.firebaseio.com/v0/"
TEST_OUTPUT_SIZE = 3

# logging configuration
logging.basicConfig(filename='ShellHN.txt')
logger = logging.getLogger()
logger.setLevel(logging.INFO)
