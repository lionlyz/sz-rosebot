from dotenv import load_dotenv
from os import environ

load_dotenv("config.env")

BOT_TOKEN = environ.get("5043144008:AAFU1_FVgISkei0f-Q-d2NW1-Wc_Wdo6BPw")
API_ID = int(environ.get("1973181"))
API_HASH = environ.get("f2424789557a9519f5949d95b85b3985")
API_ID1 = int(environ.get("16779136"))
API_HASH1 = environ.get("e8b360c14dc0dcfef3a0ae88d7a3b089")
SUDO_USERS_ID = environ.get("SUDO_USERS_ID")
LOG_GROUP_ID = environ.get("-1001602745155")
BASE_DB = environ.get("BASE_DB")
MONGO_URL = environ.get("MONGO_URL")
ARQ_API_URL = environ.get("ARQ_API_URL")
ARQ_API_KEY = environ.get("ARQ_API_KEY")
COMMAND_PREFIXES = environ.get("COMMAND_PREFIXES")
F_SUB_CHANNEL = environ.get("F_SUB_CHANNEL")
