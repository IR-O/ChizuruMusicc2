from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "8507690506:AAEs5Qff9YrjRl4lZjo6eyB9IwQhgQuFa_w")
OWNER_ID = int(getenv("OWNER_ID", "6045293810"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6045293810").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://LUSTIFYXMUSIC:Abhi77394@lustifymusic.evxnqby.mongodb.net/?retryWrites=true&w=majority&appName=LUSTIFYMUSIC")
SESSION_STRING = getenv("SESSION_STRING", "BQFZuDsAlI9PGTSv2KJ1V4LbUe7LBoNvQExsvz_7dpQnbm3Y0Hka65rjndUHb_2gD24FMaYTwiZXUzZDzyjCWMV5q0ADG6ki648XCgWOw52UIgTyRWR-PMrIQh9Um0uIJSP_EPgJ6LGAIUQ1gWMjYnAJqurqoaQqCyv_sGzKxOMGyvl6okB-kK2G5py4J7fpId6aBmYIvfH24UtU9HHz18dx2AkOKmDcffRD3yp2dkSyZW69MUGQc6vck2vlFU-tn9uRKflDAH7fAao9a97v2JLzZNPfqMjXkXUR4EjxY2rsrgwyjEZMcOlOHj04nfK1ZxCFj9P8nZ9EmOdPE_Y8NnBhMWRArAAAAAGMQVi8AA")

