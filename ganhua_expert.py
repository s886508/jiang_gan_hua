# -*- coding:utf-8 -*-
from .ganhua import GanHuaDict
from .text_compare.strategy import CompareStrategyAbstract, JaccardCompareStrategy

class GanHuaExpert:

    def __init__(self, comp_strategy):
        self.__comp_stategy = comp_strategy

    def query_similiar_from_dict(self, text, num, dict):
        """
        Calculate text similarity from given text and dictionary.
        :param text(str): Text to calculate similarity.
        :param num(int): Top most num similar text calculated.
        :param dict: GanHuaDict to compare.
        :return: List of top most num text.
        """
        ret = []
        if num <= 0:
            return ret

        for g in dict.get_dict():
            score = self.cal_similiarity(text, g.message)
            ret.append(g.message)
        return ret[0 : num]

    def cal_similiarity(self, t1, t2):
        """
        Calculate the similarity between two texts.
        :param t1(str): First text.
        :param t2(str): Second text.
        :return: Similarity score between the two texts.
        """
        if self.__comp_stategy is not None:
            return self.__comp_stategy.compare(t1, t2)
        return 0