,xz# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from FallenMusic import BOT_NAME

PM_START_TEXT = """
merhaba {0}, 🥀
๏ bu ɪs** {1} !

🇹🇷 telegram Türkiye müzik botu.
"""

START_TEXT = """
**merhaba** {0}, 🥀
  {1} @Mehmetbeydiyeceksinizzz tarafından geliştirildim {2}.

──────────────────
🇹🇷 destek grubumuz [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({3}).
"""

HELP_TEXT = f"""
<u>❄ **bunlar benim komutlarım {BOT_NAME} :**</u>

๏ /oynat : şarkı başlatır.
๏ /dur : şarki durdurur.
๏ /devam : şarkıyı calmaya devam eder.
๏ /atla : sıradaki parçaya atlatır.
๏ /son : şarkıyı kapatır.

/dongu : şarkıyı tekrarlar

๏ /ping : sʜᴏᴡ ᴛʜᴇ ᴩɪɴɢ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /sudolist : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ sᴜᴅᴏ ᴜsᴇʀs ᴏғ ᴛʜᴇ ʙᴏᴛ.

๏ /bul : /vbul şarkıyı arar bulur indirir.

๏ /search : bilgi arar.
"""

HELP_SUDO = f"""
<u>✨ **sᴜᴅᴏ ᴄᴏᴍᴍᴀɴᴅs ɪɴ {BOT_NAME} :**</u>

๏ /activevc : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs.
๏ /eval or /sh : ʀᴜɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴏᴅᴇ ᴏɴ ᴛʜᴇ ʙᴏᴛ's ᴛᴇʀᴍɪɴᴀʟ.
๏ /speedtest : ʀᴜɴs ᴀ sᴘᴇᴇᴅᴛᴇsᴛ ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /sysstats : sʜᴏᴡs ᴛʜᴇ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.

๏ /setname [ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ɴᴀᴍᴇ.
๏ /setbio [ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙɪᴏ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
๏ /setpfp [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴘғᴘ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
๏ /delpfp : ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘғᴘ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
"""

HELP_DEV = f"""
<u>✨ **ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅs ɪɴ {BOT_NAME} :**</u>

๏ /config : ᴛᴏ ɢᴇᴛ ᴀʟʟ ᴄᴏɴꜰɪɢ ᴠᴀʀɪᴀʙʟᴇꜱ ᴏꜰ ʙᴏᴛ.
๏ /broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] : ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /rmdownloads : ᴄʟᴇᴀʀs ᴛʜᴇ ᴄᴀᴄʜᴇ ғɪʟᴇs ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /leaveall : ᴏʀᴅᴇʀs ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴀʟʟ ᴄʜᴀᴛs.

๏ /addsudo [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ᴀᴅᴅ ᴛʜᴇ ᴜsᴇʀ ᴛᴏ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.
๏ /rmsudo [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ʀᴇᴍᴏᴠᴇ ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.
"""
