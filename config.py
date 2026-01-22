#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", '6286894502')) 
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "LunaBotCreator")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "Luna_Flix_Chat")
CAPTION = os.environ.get("CAPTION", "hi")
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
DOWNLOAD_LOCATION = "./DOWNLOADS"
group = environ.get('GROUP', '-1002987928500')
GROUP = int(group) if group and id_pattern.search(group) else None
SUNRISES_PIC= "https://graph.org/file/bd91761f6e938e2e6d23a.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '6286894502'))



