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
    START_TXT = """𝘏𝘪 🙋🏻{} 😀
       <i>ഇനിമുതൽ എല്ലാ ഗ്രൂപ്പിലും കേറി </i>🤤𝘗𝘢𝘢𝘭𝘱𝘢𝘢𝘺𝘢𝘴𝘢𝘮 , 𝘓𝘢𝘥𝘪𝘦𝘴 𝘏𝘰𝘴𝘵𝘦𝘭 <i>എന്നൊന്നും ചോദിച്ചു നടക്കണ്ട.. 🫣ഇവിടെ വന്ന് </i>𝘤𝘶𝘳𝘳𝘦𝘤𝘵 𝘚𝘱𝘦𝘭𝘭𝘪𝘯𝘨 ✍🏼<i>ൽ ടൈപ്പ് ചെയ്തു വിട്ടോ..
     😟ആ പിന്നൊരു കാര്യം എൻ്റെ കൈയ്യിൽ </i>𝘠𝘦𝘴𝘴𝘮𝘢 , 𝘚𝘶𝘯𝘥𝘢𝘺 𝘩𝘰𝘭𝘪𝘥𝘢𝘺 <i>അങ്ങനെയുള്ള കുറെ </i>𝘖𝘛𝘛 𝘗𝘭𝘢𝘵𝘧𝘰𝘳𝘮 <i>ൽ 😜വരുന്ന</i> 🔞𝘈𝘥𝘶𝘭𝘵 𝘊𝘰𝘯𝘵𝘦𝘯𝘵 𝘍𝘪𝘭𝘦𝘴 <i>മാത്രം മാണ്🤷 ഉള്ളത്... 
   സീരിസും സിനിമയൊന്ന എന്നോട് ചോദിക്കല്ലേ...🤐
   (ക്ഷമിക്കണം എൻ്റെ മൊയലാളി 🫠 എന്നെ ഏൽപ്പിച്ച പണി ഇതാണ്..)

   സിനിമ, സീരിസുകൾക്ക് വേറെ ആളുണ്ട്...🤗
    നിങ്ങ ദേ താഴെ👇</i> 𝘏𝘦𝘭𝘱, 𝘈𝘣𝘰𝘶𝘵 <i>എന്നീ രണ്ട് </i>𝘉𝘶𝘵𝘵𝘰𝘯 <i>കണ്ട..🧐
  അതിൽ</i> 𝘈𝘣𝘰𝘶𝘵 <i>ൽ</<i> 𝘤𝘭𝘪𝘤𝘬 <i>ചെയ്താൽ ഞങ്ങളുടെ മറ്റു </i>𝘉𝘰𝘵𝘴 & 𝘎𝘳𝘰𝘶𝘱/ 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 <i>എന്നീ </i>𝘋𝘦𝘵𝘢𝘪𝘭𝘴 <i>കിട്ടും ...!🤩

   അപ്പൊ ഓക്കെ</i> 𝘌𝘯𝘫𝘰𝘺 😍
             👍𝘏𝘢𝘷𝘦 𝘈 𝘕𝘪𝘤𝘦 𝘋𝘢𝘺..!🫠

<i>ആഹ്! 🙋പിന്നെ</i> 𝘜𝘱𝘥𝘢𝘵𝘦 𝘊𝘩𝘢𝘯𝘯𝘦𝘭 ൽ 𝘑𝘰𝘪𝘯 <i>ആവാൻ മറക്കല്ലേ...!</i> """

    HELP_TXT = """<b><u>Send Your File Name Only.</b></u>
"""
    ABOUT_TXT = """<b><i>🤖 ᴍʏ ɴᴀᴍᴇ : <a href=https://t.me/A4_Adultsbot><b>18+ ʙᴏᴛ</b></a>\n
👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/A4_AdultsGroup><b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</b></a>\n
🎞 ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ : <a href=https://t.me/freakersfilmy><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🎙 ᴍᴏᴠɪᴇ ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/freakersmovie><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
📺 sᴇʀɪᴇs ɢʀᴏᴜᴘ : <a href=https://t.me/FF_Series_Only><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🎙 sᴇʀɪᴇs ᴜᴘᴅᴀᴛᴇs : <a href=https://t.me/freakers_series><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
📺 sᴇʀɪᴇs ʙᴏᴛ : <a href=https://t.me/ffseriesbot><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🎞 ᴍᴏᴠɪᴇs ʙᴏᴛ  : <a href=https://t.me/freakersfilterbot><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
✍🏼 ʟᴀɴɢᴜᴀɢᴇ : ᴘʏᴛʜᴏɴ 3\n
📚 ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏʀᴏɢʀᴀᴍ\n
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
<code>[Button Text](buttonurl:https://t.me/FF_Series_Only)</code>

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
