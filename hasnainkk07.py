from telegram import InlineKeyboardMarkup, InlineKeyboardButton

PM_START_TEXT = """
*Hello* {}[✨]({}) 👋 I'm your 𝗘𝗱𝗶𝘁 𝗚𝘂𝗮𝗿𝗱𝗶𝗮𝗻 𝗕𝗼𝘁, here to maintain a secure environment for our discussions.

🚫 𝗘𝗱𝗶𝘁𝗲𝗱 𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗗𝗲𝗹𝗲𝘁𝗶𝗼𝗻: 𝗜'𝗹𝗹 𝗿𝗲𝗺𝗼𝘃𝗲 𝗲𝗱𝗶𝘁𝗲𝗱 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝘁𝗼 𝗺𝗮𝗶𝗻𝘁𝗮𝗶𝗻 𝘁𝗿𝗮𝗻𝘀𝗽𝗮𝗿𝗲𝗻𝗰𝘆.

📣 𝗡𝗼𝘁𝗶𝗳𝗶𝗰𝗮𝘁𝗶𝗼𝗻𝘀: 𝗬𝗼𝘂'𝗹𝗹 𝗯𝗲 𝗶𝗻𝗳𝗼𝗿𝗺𝗲𝗱 𝗲𝗮𝗰𝘁𝗶𝗺𝗲 𝘁𝗶𝗺𝗲 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 𝗶𝘀 𝗱𝗲𝗹𝗲𝘁𝗲𝗱.

🌟 𝗚𝗲𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱:
1. Add me to your group.
2. I'll start protecting instantly.

➡️ Click on 𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽 to add me and keep our group safe!
"""
    
buttons = [
    [
        InlineKeyboardButton(
            text="𝗔𝗱𝗱 𝗠𝗲 𝗧𝗼 𝗬𝗼𝘂𝗿 𝗚𝗿𝗼𝘂𝗽",
            url=f"https://t.me/GuardianDivine_bot?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ 𝐂ʜᴀɴɴᴇʟ", url=f"t.me/anime_india_divi"),
        InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ 𝐂ʜᴀᴛ", url=f"https://t.me/anime_india_divine"),
    ],    
    [
        InlineKeyboardButton(text="𝗢𝘄𝗻𝗲𝗿", url=f"https://t.me/UR_NEO"),
    ],
    
]

IMG = [
"",
"",
"",
"",
"",
"",
"",
"",
"",
"",
]
PM_START_IMG = ""
