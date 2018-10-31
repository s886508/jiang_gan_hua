# -*- coding: utf-8 -*-
import json
import os
import jieba
import random

jieba.set_dictionary("dict.txt.big")

class GanHua:

    def __init__(self, _id, _spokes, _position, _message, _tokens):
        self.id = _id
        self.spokesman = _spokes
        self.position = _position
        self.message = _message
        self.tokens = _tokens

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
        if file is None:
            return False

        json_data = json.load(file)
        self.__gan_hua_list.clear()
        for record in json_data:
            tokens = self.__tokenize(record["message"])
            self.__gan_hua_list.append(GanHua(record["id"], record["spokesman"], record["position"], record["message"], tokens))

        return True


    def __tokenize(self, message):
        """
        Use Jieba to tokenize given message.
        :param message(str): String to tokenize.
        :return: Return list of tokens.
        """
        tokens = []
        for t in jieba.cut(message, cut_all=False):
            tokens.append(t)
        return tokens

    def random_pick(self):
        """
        Return a random pick Gan Hua(幹話).
        :return: None if list is empty, otherwise a instance of GanHua
        """
        if len(self.__gan_hua_list) > 0:
            index = random.randint(0, len(self.__gan_hua_list) - 1)
            return self.__gan_hua_list[index]
        return None

    def get_dict_len(self):
        return len(self.__gan_hua_list)

    def get_dict(self):
        return self.__gan_hua_list.copy()

