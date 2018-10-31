# -*- coding=utf-8 -*-
from ..ganhua import GanHuaDict, GanHua

class TestGanHua():

    def test_ganhua_load(self):
        dict = GanHuaDict()
        ret = dict.load_from_file("")
        assert ret == False

        ret = dict.load_from_file("ganhua_dict.json")
        assert ret == True

        ret = dict.load_from_file("not_exist.json")
        assert ret == False

    def test_ganhua_randompick(self):
        dict = GanHuaDict()
        ganhua = dict.random_pick()
        assert ganhua is None

        dict.load_from_file("ganhua_dict.json")
        ganhua = dict.random_pick()
        assert ganhua is not None

