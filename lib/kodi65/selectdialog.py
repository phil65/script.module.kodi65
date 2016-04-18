# -*- coding: utf8 -*-

# Copyright (C) 2015 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

import xbmcgui
import xbmc

from kodi65 import addon

C_LIST_SIMPLE = 3
C_LIST_DETAIL = 6
C_BUTTON_GET_MORE = 5
C_LABEL_HEADER = 1


class SelectDialog(xbmcgui.WindowXMLDialog):

    def __init__(self, *args, **kwargs):
        xbmcgui.WindowXMLDialog.__init__(self)
        self.items = kwargs.get('listing')
        self.header = kwargs.get('header')
        self.listitems = [i.get_listitem() for i in self.items] if self.items else []
        self.index = -1

    def onInit(self):
        self.list = self.getControl(C_LIST_DETAIL)
        self.getControl(C_LIST_SIMPLE).setVisible(False)
        self.getControl(C_BUTTON_GET_MORE).setVisible(False)
        self.getControl(C_LABEL_HEADER).setLabel(self.header)
        self.list.addItems(self.listitems)
        self.setFocus(self.list)

    def onClick(self, control_id):
        if control_id in [C_LIST_SIMPLE, C_LIST_DETAIL]:
            self.index = int(self.list.getSelectedPosition())
            self.close()

    def onFocus(self, control_id):
        pass


def open(listitems, header):
    """
    open selectdialog, return index
    """
    xbmc.executebuiltin("Dialog.Close(busydialog)")
    w = SelectDialog('DialogSelect.xml', addon.PATH,
                     listing=listitems,
                     header=header)
    w.doModal()
    return w.index
