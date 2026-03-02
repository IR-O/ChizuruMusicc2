from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "8507690506:AAEs5Qff9YrjRl4lZjo6eyB9IwQhgQuFa_w")
OWNER_ID = int(getenv("OWNER_ID", "6045293810"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6045293810").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://LUSTIFYXMUSIC:Abhi77394@lustifymusic.evxnqby.mongodb.net/?retryWrites=true&w=majority&appName=LUSTIFYMUSIC")
SESSION_STRING = getenv("SESSION_STRING", "BQIQsd4AeISY7fCq-EGnhmz225GKLSF5NYHIpCIZpd2jZWV7Xi-49y1wpCXBhJwMKHRSBly17Z3iJ94hA344bGZT9aRTlv2MHU__LOrb9hXOtk9JHQJlWZoAPNIxEIKJ4zIHV1h_QeBqab2_ZiSkAe8kYdNNoznWUyAfEbxeKKTSB_ajJEGLugwh8S3Qhv8HJgBdmU0Wsd2oZ3onJ8tLSrJrfmUNkPyp3FgmmcjNG_aJIX95TUi0fh8oTZ7A_u3Nt6cZ6mBg24VIdTSwpN-dK02TnWeXTC5uNsv4yCdA63vDG1SjcOBFbqVNx-uwqII-mo_1Hf3GkTJ0Tl7PPzgND2_Fe9SooAAAAAGfyn-lAA")

