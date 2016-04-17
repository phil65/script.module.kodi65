# -*- coding: utf8 -*-

# Copyright (C) 2016 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details


class ItemList(object):

    def __init__(self, items=None, content_type="", name="", sorts=None, totals=None, properties=None):
        self.name = name
        self.content_type = content_type
        self.totals = totals
        self._items = items if items else []
        self.sorts = sorts if sorts else []
        self._properties = properties if properties else []

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, key):
        return self._items[key]

    def __nonzero__(self):
        return len(self._items) > 0

    def __str__(self):
        return "Itemlist with length %s. Content type: %s" % (len(self._items), self.content_type)

    def __add__(self, other):
        return ItemList(items=self._items + other.items(),
                        content_type=self.content_type,
                        name=self.name,
                        sorts=self.sorts,
                        properties=self._properties)

    def __iadd__(self, other):
        self._items += other.items
        return self

    def items(self):
        return self._items

    def append(self, item):
        self._items.append(item)

    def remove(self, index):
        self._items.remove(index)

    def set_name(self, name):
        self.name = name

    def set_content(self, content_type):
        self.content_type = content_type

    def set_totals(self, totals):
        self.totals = totals

    def add_sorts(self, sorts):
        self.sorts = sorts

    def set_properties(self, properties):
        self._properties = properties

    def update_properties(self, properties):
        self._properties.update({k: v for k, v in properties.iteritems() if v})

    def set_property(self, key, value):
        self._properties[key] = value

    def get_property(self, key):
        value = self._properties.get(key)
        return value if value else ""
