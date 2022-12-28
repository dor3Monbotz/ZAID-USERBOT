import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "16743442")) #optional
API_HASH = getenv("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5402276336", "2128554309").split()))
OWNER_ID = int(getenv("OWNER_ID", "5885920877"))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "5856515582:AAGP103WUjrBKrJSmwoPPJcx5z85CMYpFwI")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQD_fBIAv4QQyt9F2QuNF-wfjlUfd4oQM0PFFNNHmwFz9zXCRPKos3PngUBsxuzucmpx6Eg0SjUay-Z_YCA0hNqxBw-aFbu2cown-MHO8VldR0MuD5aMVA_sItkpM8CJ2pj_wMx_9sUtjtJBX2AXY3F2M73hRHc5RxoVV1WjzwORqifElnv7zebRgujQNEY2ahSn8XPfALrUSacAVthmL5cHFsXnbPxRyG5s_VD4LhxurbaW7SzeRJikAdvXvapX-BpCWd868iU1_PhfPTl7GyhoipYiYrN5s_X4cGGkMAc0Pz7dByRaLZ92wfJwNAXcWYta0s6aQWQ2r2M6C_XxsZARp7-iPAAAAAFe1AZtAA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
