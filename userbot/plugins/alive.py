"""Check if userbot alive."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time
from uniborg.util import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME
from datetime import datetime
from userbot import Lastupdate
from userbot.plugins import currentversion

#Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
pm_caption = "➥ **UserBot:** `ONLINE`\n\n"
pm_caption += "➥ **INFORMAZIONI **\n"
pm_caption += f"➥ **Online da** : `{uptime}` \n"
pm_caption += "➥ **Database:**  `Attivo`\n"
pm_caption += f"➥ **Versione** : `{currentversion}`\n"


@borg.on(admin_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ Con .alive, vedi se il Bot funziona.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()
