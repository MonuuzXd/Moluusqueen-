import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/92dd93f98c61c63c6f100.jpg",
        caption=f"""**๐๐ก๐ข๐ฌ ๐๐ฌ ๐๐๐ฏ๐๐ง๐๐ ๐ฅ๐๐๐ฅ๐๐ ๐ซ๐๐ฆ ๐๐ฎ๐ฌ๐ข๐ ๐ถ ๐๐จ๐ญ ๐๐ฎ๐ง ๐๐ง ๐๐ซ๐ข๐ฏ๐๐ญ๐ ๐ฅ ๐๐ฉ๐ฌ ๐ซ๐๐๐ซ๐ฏ๐๐ซ ๐ ๐๐๐๐ฅ โค๏ธ ๐๐ข๐ ๐ก ๐๐ฎ๐๐ฅ๐ข๐ญ๐ฒ ๐๐ฎ๐ฌ๐ข๐ ๐ง ๐๐ง ๐๐ ๐๐๐ฏ๐๐ฅ๐จ๐ฉ๐๐ ๐๐ฒ = [เผ๐ฆแถฆแถฐแตแญเผโฆอ๐จ๐บ๐ฏ๐น๐จ๐ญโอแถอแดฟอแดฌอแถปอแดตอแดฑอแธโโโโ ฬฬฐแดทอแตอแดฌอแตอเผเผโฐ๐โเฟ](https://t.me/itz_me_monuuz)

๐๐ซ๐๐๐ญ๐จ๐ซ :- [๐ เผ๐ฆแถฆแถฐแตแญเผโฆอ๐จ๐บ๐ฏ๐น๐จ๐ญโอแถอแดฟอแดฌอแถปอแดตอแดฑอแธโโโโ ฬฬฐแดทอแตอแดฌอแตอเผเผโฐ๐โเฟ](https://t.me/itz_me_monuuz)
๐๐ฎ๐ฉ๐ฉ๐จ๐ซ๐ญ :- [๐  ๐ฆ๐ฝ๐ผ๐ฟ๐ ๐๐ผ๐ง๐ โค๏ธ๐ธ](https://t.me/moluuzsupport)
๐๐ข๐ฌ๐๐ฎ๐ฌ๐ฌ :- [๐  ๐ฆ๐ฝ๐ผ๐ฟ๐ ๐๐น๐ฎ๐ป ๐ง](https://t.me/moluuzsupport)
๐๐จ๐ฎ๐ซ๐๐  :- [๐  ๐๐น๐ถ๐ฐ๐ธ โ๏ธ ๐ฅ๐ฒ๐ฝ๐ผ ๐](https://github.com/itzmemonuuz123/SmokerMusicX)
๐๐จ๐ฆ๐ฆ๐๐ง๐ :- [๐ ๐๐น๐ถ๐ฐ๐ธ โ๏ธ ๐ก๐ผ๐ ๐ฉ](https://telegra.ph/%EA%9C%B1%E1%B4%8D%E1%B4%8F%E1%B4%8B%E1%B4%87%CA%80-%E1%B4%8D%E1%B4%9C%EA%9C%B1%C9%AA%E1%B4%84-%CA%99%E1%B4%8F%E1%B4%9B-%E1%B4%84%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85%EA%9C%B1-08-29)
GIFSchannel :- [๐ ๐๐ผ๐ถ๐ป โค๏ธ๐ฅ](https://t.me/cutebabygif916)

๐๐ ๐๐จ๐ฎ ๐๐๐ฏ๐ ๐๐ง๐ฒ ๐๐ฎ๐๐ฌ๐ญ๐ข๐จ๐ง๐ฌ ๐๐ง๐ ๐๐๐ฅ๐ฉ ๐๐ก๐๐ง ๐๐ฆ ๐๐ฒ ๐๐จ๐ฌ๐ฌ = [เผ๐ฆแถฆแถฐแตแญเผโฆอ๐จ๐บ๐ฏ๐น๐จ๐ญโอแถอแดฟอแดฌอแถปอแดตอแดฑอแธโโโโ ฬฬฐแดทอแตอแดฌอแตอเผเผโฐ๐โเฟ](https://t.me/itz_me_monuuz)**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Jแดษชษด Hแดสแด & Sแดแดแดแดสแด โจ", url=f"https://t.me/moluuzsupport")
                ]
                
           ]
        ),
    )
    

@Client.on_message(command(["repo"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/92dd93f98c61c63c6f100.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "๐ฅ Cสษชแดแด Mแด Tแด Gแดแด Rแดแดแด ๐", url=f"https://t.me/moluuzsupport")
                ]
            ]
        ),
    )
