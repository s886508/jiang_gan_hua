# -*- coding:utf-8 -*-
from .ganhua import GanHuaDict
from .text_compare.strategy import JaccardCompareStrategy, LevenshteiinCompareStrategy

class GanHuaExpert:

    def __init__(self, comp_strategy, dict):
        """
        :param comp_strategy: Strategy to compare sentence similarity.
        :param dict: GanHuaDict to compare.
        """
        self.__comp_stategy = comp_strategy
        self.__dict = dict

    def __sort_by_score(self, similar_scores):
        """
        Sort similar sentences by score.
        :param similar_scores: Similarity scores between two sentences.
        """
        if type(self.__comp_stategy) is JaccardCompareStrategy:
            return sorted(similar_scores.items(), key=lambda x: x[1])
        if type(self.__comp_stategy) is LevenshteiinCompareStrategy:
            return sorted(similar_scores.items(), key=lambda x: x[1])
        return similar_scores

    def query_similiar_from_dict(self, text, num):
        """
        Calculate text similarity from given text and dictionary.
        :param text(str): Text to calculate similarity.
        :param num(int): Top most num similar text calculated.
        :return: List of top most num text.
        """
        scores_dict = {}
        if num <= 0:
            return scores_dict

        for g in self.__dict.get_dict():
            scores_dict[g.message] = self.cal_similiarity(text, g.message)

        scores_dict = self.__sort_by_score(scores_dict)
        return list(scores_dict)[0 : num]


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

    def random_pick(self, count):
        """
        :param count: Numbers to return.
        :return: Set of gan hua.
        """
        gan_hua_set = set()
        for index in range(count):
            pick = self.__dict.random_pick()
            while pick in gan_hua_set:
                pick = self.__dict.random_pick()
            gan_hua_set.add(pick)

        return gan_hua_set
