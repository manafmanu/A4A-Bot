import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://beingtek.com/ref/GreyMatter658')
    START_TXT = """𝑯𝒆𝒍𝒍𝒐 👋  {}  \n𝑯𝒆𝒓𝒆 𝒀𝒐𝒖 𝑪𝒂𝒏 𝑺𝒆𝒂𝒓𝒄𝒉 𝒀𝒐𝒖𝒓𝒔 𝑴𝒐𝒔𝒕 𝑷𝒐𝒑𝒖𝒍𝒂𝒓 𝑺𝒆𝒓𝒊𝒆𝒔.  \n𝑱𝒖𝒔𝒕 𝑻𝒚𝒑𝒆 𝒀𝒐𝒖𝒓 𝑺𝒆𝒓𝒊𝒆𝒔 𝑵𝒂𝒎𝒆 𝑨𝒏𝒅 𝑺𝒆𝒏𝒅 𝑻𝒐 𝑴𝒆 𝑶𝒓 𝑮𝒓𝒐𝒖𝒑...   \n\n𝑴𝒖𝒔𝒕 𝒀𝒐𝒖 𝑩𝒆 𝑨 𝑴𝒆𝒎𝒃𝒆𝒓 𝑶𝒇 <a href=https://t.me/freakers_series><b></b>ғʀᴇᴀᴋᴇʀs sᴇʀɪᴇs</a> 𝑻𝒐 𝑼𝒔𝒆 𝑴𝒆. \n\n 𝑭𝒐𝒓 𝑴𝒐𝒓𝒆 𝑫𝒆𝒕𝒂𝒊𝒍𝒔 𝑪𝒍𝒊𝒄𝒌 <u>𝑯𝑬𝑳𝑷</u> 𝑩𝒖𝒕𝒕𝒐𝒏 𝑩𝒆𝒍𝒐𝒘. 👇  \n\n𝑰𝒇 𝒚𝒐𝒖 𝒏𝒆𝒆𝒅 𝒂𝒏𝒚 𝒐𝒕𝒉𝒆𝒓 𝒃𝒐𝒕𝒔 / 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 / 𝒈𝒓𝒐𝒖𝒑 𝑪𝒍𝒊𝒄𝒌 𝒕𝒉𝒆 <u>𝑨𝑩𝑶𝑼𝑻</u> 𝒃𝒖𝒕𝒕𝒐𝒏...   \n\n𝑴𝒂𝒊𝒏𝒕𝒂𝒊𝒏𝒆𝒅 𝒃𝒚 : <a href=https://t.me/naughty_nonsense><b></b>ɴᴀᴜɢʜᴛʏ ɴᴏɴsᴇɴsᴇ</a>\n𝑷𝒐𝒘𝒆𝒓𝒆𝒅 𝒃𝒚 : <a href=https://t.me/FF_Series_Only><b></b>ғʀᴇᴀᴋᴇʀs sᴇʀɪᴇs</a>\n\n100% ғᴀꜱᴛ & ϙᴜᴀʟɪᴛʏ\n▬▬▬▬▬▬▬▬▬▬▬▬ """

    HELP_TXT = """<b><u>How To Request A Series💡</b></u>

𝐷𝑜𝑛𝑡 𝑇𝑦𝑝𝑒 𝑆𝑒𝑟𝑖𝑒𝑠 𝐿𝑎𝑛𝑔𝑢𝑎𝑔𝑒𝑠 𝑊𝑖𝑡ℎ 𝑡ℎ𝑒 𝑇𝑖𝑡𝑙𝑒..❗️
𝐷𝑜𝑛'𝑡 𝑇𝑦𝑝𝑒 𝑊𝑜𝑟𝑑𝑠 𝐿𝑖𝑘𝑒 (𝑆𝑒𝑎𝑠𝑜𝑛, 𝐸𝑝𝑖𝑠𝑜𝑑𝑒  &  𝑒𝑡𝑐..)\n
 <u>𝑈𝑠𝑒 𝑇ℎ𝑖𝑠 𝐷𝑒𝑚𝑜 𝑊𝑖𝑡ℎ 𝑇ℎ𝑒 𝑇𝑖𝑡𝑙𝑒 </u>\n
 <b>Ex:</b>  S01E01, S02E05, S10E09 𝐹𝑜𝑟 𝐵𝑒𝑡𝑡𝑒𝑟 𝑅𝑒𝑠𝑢𝑙𝑡...❕

<b><u>Examples</b></u>
stranger things Season 2 ❌
Stranger things season 02 Episode 4 ❌\n
 Stranger things ✔️
 Stranger things S01✔️
Stranger things S01E05✔️\n▬▬▬▬▬▬▬▬▬▬▬▬"""
    ABOUT_TXT = """<b><i>🤖 ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/ffseriesbot><b>sᴇʀɪᴇs ʙᴏᴛ</b></a>\n
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://www.instagram.com/naughty__nonsense/><b>ᴍᴀɴᴀғ</b></a>\n
🎞 ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ : <a href=https://t.me/freakersfilmy><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🎙 ᴍᴏᴠɪᴇ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/freakersmovie><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
📺 sᴇʀɪᴇs ɢʀᴏᴜᴘ : <a href=https://t.me/FF_Series_Only><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🎙 sᴇʀɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/freakers_series><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🔞 18+ ʙᴏᴛ : <a href=https://t.me/A4_Adultsbot><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🎞 ᴍᴏᴠɪᴇs ʙᴏᴛ  : <a href=https://t.me/freakersfilterbot><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
✍🏼 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏʀᴏɢʀᴀᴍ\n
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3\n
📡 ʜᴏsᴛᴇᴅ ᴏɴ : <a href=https://railway.app/><b></b>ʀᴀɪʟᴡᴀʏ</a>\n
⚙ sᴏᴜʀᴄᴇ  : <a href=https://github.com/><b></b>ɢɪᴛʜᴜʙ</a>\n
⚡️ ᴠᴇʀsɪᴏɴ : <a href=https://t.me/naughty_nonsense><b></b>ᴠ4.0</a>\n</b></i>"""
    SOURCE_TXT = """<b>𝐂𝐫𝐞𝐚𝐭𝐞 𝐎𝐧𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬:</b>
» I will Create One Bot For You<b>
» Contact Me @GreyMatter_Owner<b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Search Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Search Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Search Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Search Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/GreyMatter_Owner)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {}(<code>{}</code>)</b>
<b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ <code>{}</code></b>
<b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› 𝐈𝐃 - <code>{}</code></b>
<b>᚛› 𝐍𝐚𝐦𝐞 - {}</b>
"""
