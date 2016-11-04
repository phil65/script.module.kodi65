# -*- coding: utf8 -*-

# Copyright (C) 2016 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

import xbmcaddon
import xbmc
import os
import xbmcgui
import base64
import uuid
import hashlib

ADDON = xbmcaddon.Addon()
ID = ADDON.getAddonInfo('id').decode("utf-8")
ICON = ADDON.getAddonInfo('icon').decode("utf-8")
NAME = ADDON.getAddonInfo('name').decode("utf-8")
FANART = ADDON.getAddonInfo('fanart').decode("utf-8")
AUTHOR = ADDON.getAddonInfo('author').decode("utf-8")
CHANGELOG = ADDON.getAddonInfo('changelog').decode("utf-8")
DESCRIPTION = ADDON.getAddonInfo('description').decode("utf-8")
DISCLAIMER = ADDON.getAddonInfo('disclaimer').decode("utf-8")
VERSION = ADDON.getAddonInfo('version').decode("utf-8")
PATH = ADDON.getAddonInfo('path').decode("utf-8")
PROFILE = ADDON.getAddonInfo('profile').decode("utf-8")
SUMMARY = ADDON.getAddonInfo('summary').decode("utf-8")
TYPE = ADDON.getAddonInfo('type').decode("utf-8")
MEDIA_PATH = os.path.join(PATH, "resources", "skins", "Default", "media")
DATA_PATH = xbmc.translatePath("special://profile/addon_data/%s" % ID).decode("utf-8")
HOME = xbmcgui.Window(10000)


def setting(setting_name):
    return ADDON.getSetting(setting_name)


def set_setting(setting_name, string):
    ADDON.setSetting(str(setting_name), str(string))


def set_password_prompt(setting_name):
    password = xbmcgui.Dialog().input(LANG(12326), option=xbmcgui.ALPHANUM_HIDE_INPUT)
    if password:
        ADDON.setSetting(setting_name, encode_string(password))


def set_password(setting_name, string):
    ADDON.setSetting(setting_name, encode_string(string))


def get_password(setting_name):
    mac = str(uuid.getnode())
    mac_hash = hashlib.md5(mac).hexdigest()
    if not ADDON.getSetting("mac_hash"):
        ADDON.setSetting("mac_hash", mac_hash)
    elif ADDON.getSetting("mac_hash") != mac_hash:
        xbmcgui.Dialog().notification("Error", "MAC id changed. Please enter password again in settings.")
        return None
    setting = ADDON.getSetting(setting_name)
    if setting:
        return decode_string(setting)


def bool_setting(setting_name):
    return ADDON.getSetting(setting_name) == "true"


def reload_addon():
    global ADDON
    ADDON = xbmcaddon.Addon()


def LANG(id_):
    return ADDON.getLocalizedString(id_) if 31000 <= id_ <= 33000 else xbmc.getLocalizedString(id_)


def set_global(setting_name, setting_value):
    HOME.setProperty(setting_name, setting_value)


def get_global(setting_name):
    return HOME.getProperty(setting_name)


def clear_global(setting_name):
    HOME.clearProperty(setting_name)


def clear_globals():
    HOME.clearProperties()


def encode_string(clear):
    enc = []
    key = str(uuid.getnode())
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc))


def decode_string(enc):
    dec = []
    key = str(uuid.getnode())
    enc = base64.urlsafe_b64decode(enc)
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)
