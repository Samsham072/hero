import asyncio
from pyrogram import Client
from pyrogram import filters

from log import log


apiid = 7239207
apihash = "ed44780dedd182084f2133b16944cf34"
bottoken = "5277760588:AAFIb-z-V6VGZ6hzldX4K6_QweoobsBcm8k" #bot token here


client = Client(
    'lana',
    apiid,
    api_hash= apihash,
    bot_token = bottoken,
    plugins=dict(root="plugins"),
    
)


client.run()