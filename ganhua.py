# -*- coding: utf-8 -*-
import json
import os

class GanHua:

    def __init__(self, _id, _spokes, _position, _message):
        self.id = _id
        self.spokesman = _spokes
        self.position = _position
        self.message = _message

class GanHuaDict:

    def __init__(self):
        self.__gan_hua_list = []

    def load_from_file(self, path):
        """ Parse data from given file path.
        :param path(str): File path to parse data.
        :return True if parse successfully.
        """
        if not os.path.exists(path):
            return False
        file = open(path, "r", encoding="utf-8")
        if file is not None:
            json_data = json.load(file)
            for record in json_data:
                self.__gan_hua_list.append(GanHua(record["id"], record["spokesman"], record["position"], record["message"]))