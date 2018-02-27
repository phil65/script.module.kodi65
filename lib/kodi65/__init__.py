# -*- coding: utf8 -*-

# Copyright (C) 2016 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

from __future__ import absolute_import

from kodi65.kodiaddon import Addon
addon = Addon()

from kodi65.listitem import ListItem, VideoItem, AudioItem
from kodi65.itemlist import ItemList
from kodi65.actionhandler import ActionHandler
from kodi65.busyhandler import busyhandler as busy
from kodi65.kodilogging import KodiLogHandler, config
from kodi65.dialogbaselist import DialogBaseList
from kodi65.localdb import LocalDB
from kodi65.player import VideoPlayer

local_db = LocalDB()
player = VideoPlayer()
