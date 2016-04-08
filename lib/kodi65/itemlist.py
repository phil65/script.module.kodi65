# -*- coding: utf8 -*-

# Copyright (C) 2016 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details


class ItemList(object):

    def __init__(self, items, content_type="", name=""):
        self.items = items
        self.name = name
        self.content_type = content_type

    def __len__(self):
        return len(self.items)

    def add(self, item):
        self.items.append(item)

    def remove(self, index):
        self.items.remove(index)

    def set_name(self, name):
        self.name = name

    def set_content(self, content_type):
        self.content_type = content_type
