import os
import dotenv


dotenv.load_dotenv(dotenv.find_dotenv())

PREFIX = os.environ['PREFIX']
WELCOME_MESSAGE = os.environ['WELCOME_MESSAGE']
STARTED_ROLE = os.environ['STARTED_ROLE']
TOKEN_BOT = os.environ['TOKEN_BOT']