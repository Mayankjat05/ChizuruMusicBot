from Chizuru.core.bot import Chizuru
from Chizuru.core.dir import dirr
from Chizuru.core.git import git
from Chizuru.core.userbot import Userbot
from Chizuru.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

Chizuru = Chizuru()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
