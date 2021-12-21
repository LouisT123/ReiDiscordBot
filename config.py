import os
from keep_alive import keep_alive
my_secret = os.environ['TOKEN']
CONFIG = {
  "bot_token": "my_secret",
  "notification_channelid": 791804582442434590,
}
keep_alive()