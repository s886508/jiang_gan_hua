# -*- coding=utf-8 -*-
from ..ganhua import GanHuaDict, GanHua

class TestGanHua():

    def test_ganhua_load(self):
        dict = GanHuaDict()
        ret = dict.load_from_file("")
        assert ret == False

        ret = dict.load_from_file("not_exist.json")
        assert ret == False

        ret = dict.load_from_file("data/ganhua_dict.json")
        assert ret == True
        assert dict.get_dict_len() == 54

        # Load will reset list to empty.
        ret = dict.load_from_file("data/ganhua_dict.json")
        assert dict.get_dict_len() == 54

    def test_ganhua_randompick(self):
        dict = GanHuaDict()
        ganhua = dict.random_pick()
        assert ganhua is None

        dict.load_from_file("data/ganhua_dict.json")
        ganhua = dict.random_pick()
        assert ganhua is not None

