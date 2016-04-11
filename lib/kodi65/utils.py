# -*- coding: utf8 -*-

# Copyright (C) 2015 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details
from functools import wraps

import xbmc
import xbmcgui

import YDStreamExtractor
from kodi65 import addon


def log(txt):
    if isinstance(txt, str):
        txt = txt.decode("utf-8", 'ignore')
    message = u'%s: %s' % (addon.ID, txt)
    xbmc.log(msg=message.encode("utf-8", 'ignore'),
             level=xbmc.LOGDEBUG)


def merge_dicts(*dict_args):
    '''
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    '''
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result


def get_skin_string(name):
    return xbmc.getInfoLabel("Skin.String(%s)").decode("utf-8")


def set_skin_string(name, value):
    xbmc.executebuiltin("Skin.SetString(%s, %s)" % (name, value))


def busy_dialog(func):
    """
    Decorator to show busy dialog while function is running
    Only one of the decorated functions may run simultaniously
    """

    @wraps(func)
    def decorator(self, *args, **kwargs):
        xbmc.executebuiltin("ActivateWindow(busydialog)")
        try:
            result = func(self, *args, **kwargs)
        except Exception:
            result = None
        finally:
            xbmc.executebuiltin("Dialog.Close(busydialog)")
        return result

    return decorator


def download_video(youtube_id):
    vid = YDStreamExtractor.getVideoInfo(youtube_id,
                                         quality=1)
    YDStreamExtractor.handleDownload(vid)


def notify(header="", message="", icon=addon.ICON, time=5000, sound=True):
    xbmcgui.Dialog().notification(heading=header,
                                  message=message,
                                  icon=icon,
                                  time=time,
                                  sound=sound)


def millify(n):
    """
    make large numbers human-readable, return string
    """
    millnames = [' ', '.000', ' ' + addon.LANG(32000), ' ' + addon.LANG(32001), ' ' + addon.LANG(32002)]
    if not n or n <= 100:
        return ""
    n = float(n)
    char_count = len(str(n))
    millidx = (char_count / 3) - 1
    if millidx == 3 or char_count == 9:
        return '%.2f%s' % (n / 10 ** (3 * millidx), millnames[millidx])
    else:
        return '%.0f%s' % (n / 10 ** (3 * millidx), millnames[millidx])


def get_year(year_string):
    """
    return last 4 chars of string
    """
    return year_string[:4] if year_string else ""


def format_time(time, time_format=None):
    """
    get formatted time
    time_format = h, m or None
    """
    try:
        intTime = int(time)
    except Exception:
        return time
    hour = str(intTime / 60)
    minute = str(intTime % 60).zfill(2)
    if time_format == "h":
        return hour
    elif time_format == "m":
        return minute
    elif intTime >= 60:
        return hour + " h " + minute + " min"
    else:
        return minute + " min"
