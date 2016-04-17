# -*- coding: utf8 -*-

# Copyright (C) 2016 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details


class ItemList(object):

    def __init__(self, items, content_type="", name=""):
        self.items = items
        self.name = name
        self.content_type = content_type
        self.sorts = []
        self.properties = []

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __add__(self, other):
        return ItemList(items=self.items + other.items,
                        content_type=self.content_type,
                        name=self.name,
                        sorts=self.sorts,
                        properties=self.properties)

    def __iadd__(self, other):
        self.items += other.items
        return self

    def append(self, item):
        self.items.append(item)

    def remove(self, index):
        self.items.remove(index)

    def set_name(self, name):
        self.name = name

    def set_content(self, content_type):
        self.content_type = content_type

    def add_sorts(self, sorts):
        self.sorts = sorts

    def set_properties(self, properties):
        self.properties = properties

    def update_properties(self, properties):
        self.properties.update({k: v for k, v in properties.iteritems() if v})

    def set_property(self, key, value):
        self.properties[key] = value

    def get_property(self, key):
        value = self.properties.get(key)
        return value if value else ""
