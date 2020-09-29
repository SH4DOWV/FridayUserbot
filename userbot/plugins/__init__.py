from userbot import topfunc
from userbot.utils import admin_cmd
from var import Var 
from userbot.uniborgConfig import Config


idgen = topfunc.id_generator
findnemo = topfunc.stark_finder
issudousing = Config.SUDO_USERS
islogokay = Config.PRIVATE_GROUP_ID
isdbfine = Var.DB_URI
isherokuokay = Var.HEROKU_APP_NAME
gdriveisshit = Config.AUTH_TOKEN_DATA
wttrapi = Config.OPEN_WEATHER_MAP_APPID
rmbg = Config.REM_BG_API_KEY
hmmok = Config.LYDIA_API
currentversion = "3.0"

if issudousing:
    amiusingsudo = "Attivo ✅"
else:
    amiusingsudo = "Inattivo ❌"

if islogokay:
    logchat = "Connesso ✅"
else:
    logchat = "Disconnesso ❌"

if isherokuokay:
    riplife = "Connesso ✅"
else:
    riplife = "Disconnesso ❌"

if gdriveisshit:
    wearenoob = "Attivo ✅"
else:
    wearenoob = "Inattivo ❌"

if rmbg:
    gendu = "Aggiunto ✅"
else:
    gendu = "Non Aggiunto ❌"

if wttrapi:
    starknoobs = "Aggiunto ✅"
else:
    starknoobs = "Non Aggiunto ❌"

if hmmok:
    meiko = "Aggiunto ✅"
else:
    meiko = "Non Aggiunto ❌"

if isdbfine:
    dbstats = "Funzionante ✅"
else:
    dbstats = "Non Funzionante ❌"

inlinestats = (f"✘ STATISTICHE ✘\n"
               f"VERSIONE = {currentversion} \n"
               f"DATABASE = {dbstats} \n"
               f"SUDO = {amiusingsudo} \n"
               f"LOG-CHAT = {logchat} \n"
               f"HEROKU = {riplife} \n"
               f"G-DRIVE = {wearenoob}")
