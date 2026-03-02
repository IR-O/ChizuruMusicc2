from os import getenv


API_ID = int(getenv("API_ID", "26850449"))
API_HASH = getenv("API_HASH", "72a730c380e68095a8549ad7341b0608")
BOT_TOKEN = getenv("BOT_TOKEN", "8507690506:AAEs5Qff9YrjRl4lZjo6eyB9IwQhgQuFa_w")
OWNER_ID = int(getenv("OWNER_ID", "6045293810"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6045293810").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://LUSTIFYXMUSIC:Abhi77394@lustifymusic.evxnqby.mongodb.net/?retryWrites=true&w=majority&appName=LUSTIFYMUSIC")
SESSION_STRING = getenv("SESSION_STRING", "BQIQsd4AxSz6as3DlNJHw35howfMurZ6tuzFtek_DcmIZ6eCiPppo6qS6uslxLTHK2c60-Wxhc2FSlSiUa3Y4pxnAB2VJJkU4QEkc2R27e0OM_WvkRNDucr3T8ypnLdGMXtlYjToREsy74tLtkXzrNzs_IUFPX31SqJnN6btkOWHDGtSDcIbmWgo1cTl2rjQ6NmBMp1O_Z_tf43khe64IMY6ZDqhSmsVJJW8MfmzC_hiJYwph6EHoVZfez94XtDHvXKY3ZIgTEpHxVYaWWtNa9ZmdqIZkkA-TurgEzwY4LvJ0fHncK1zkGYhUJxpVvHsIAcQRYvU0rGdg3vBE02o19XhQwJ34QAAAAHWLlDtAA")
