from SmartXMusic.core.bot import Anony
from SmartXMusic.core.dir import dirr
from SmartXMusic.core.git import git
from SmartXMusic.core.userbot import Userbot
from SmartXMusic.misc import dbb, heroku
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
