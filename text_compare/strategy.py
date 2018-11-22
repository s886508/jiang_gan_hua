# -*- coding=utf-8 -*-
import abc
import distance
from .. import segment

class CompareStrategyAbstract(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self._last_used_tokens = []

    def _add_last_used_tokens(self, text, tokens):
        if len(self._last_used_tokens) >= 10:
            index = 9
            for i in range(0, 9):
                if self._last_used_tokens[i].first == text:
                    index = i
                    break
            del self._last_used_tokens[index]
        self._last_used_tokens.append((text, tokens))

    def _find_last_used_tokens(self, text):
        for pair in self._last_used_tokens:
            if pair.first == text:
                return pair.second
        return None

    @abc.abstractmethod
    def compare(self, t1, t2):
        pass

    @abc.abstractmethod
    def compare_tokens(self, tokens1, tokens2):
        pass

class JaccardCompareStrategy(CompareStrategyAbstract):
    def compare(self, t1, t2):
        tokens1 = self._find_last_used_tokens(t1)
        tokens2 = self._find_last_used_tokens(t2)
        if tokens1 is None:
            tokens1 = segment.tokenize(t1)
        if tokens2 is None:
            tokens2 = segment.tokenize(t2)

        return self.compare_tokens(tokens1, tokens2)

    def compare_tokens(self, tokens1, tokens2):
        return distance.jaccard(tokens1, tokens2)

class LevenshteiinCompareStrategy(CompareStrategyAbstract):
    def compare(self, t1, t2):
        return distance.levenshtein(t1, t2)

    def compare_tokens(self, tokens1, tokens2):
        pass