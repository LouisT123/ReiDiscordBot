#based on Endendragon's art_mention button repo

from keep_alive import keep_alive
import datetime 
import discord
import asyncio
import re

from discord_slash.utils.manage_components import create_actionrow, create_button, ButtonStyle

class bossPing:
  def __init__(self, client, image_channelids, thread_channelids, base_role_id, pingboard_channelid ):
    self.client = client
    self.image_channelids = image_channelids
    self.thread_channelids = thread_channelids
    self.base_role_id = base_role_id
    self.pingboard_channelid = pingboard_channelid
    self.mention_last = {}
    self.cooldown = 2 * 60
    self.re_compiled = re.compile("^!!(?<character>\w++)\W*$")
    self.pingboard_uptodate = False

    self.bg_task_delete_roles = self.client.loop.create(self.background_task_delete_roles())

    self.bg_task_update_pingboard = self.client.loop.create_task(self.background_task_update_pingboard())

  




  keep_alive();

