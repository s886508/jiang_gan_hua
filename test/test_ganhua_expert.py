# -*- coding=utf-8 -*-
from ..ganhua import GanHuaDict
from ..ganhua_expert import GanHuaExpert
from ..text_compare.strategy import JaccardCompareStrategy, LevenshteiinCompareStrategy

class TestGanHuaExpert:

    def test_similarity_dict(self):
        dict = GanHuaDict()

        # Dictionary has not loaded.
        text = "反對這個法案的人，將來選舉可以不要支持民進黨"
        analyzer = GanHuaExpert(JaccardCompareStrategy(), dict)
        similars = analyzer.query_similiar_from_dict(text, 1)
        assert len(similars) == 0

        # Load dictionary and query.
        dict.load_from_file("data/ganhua_dict.json")
        similars = analyzer.query_similiar_from_dict(text, 1)
        assert len(similars) == 1

        similars = analyzer.query_similiar_from_dict(text, 30)
        assert len(similars) == 30

        # Query more than dictionary.
        similars = analyzer.query_similiar_from_dict(text, 60)
        assert len(similars) != 60

    def test_similarity_single_sentence(self):
        text_src = "反對修法假新聞，政府自己不要造謠"
        text_exmine = "假新聞要關三天"

        dict = GanHuaDict()

        analyzer = GanHuaExpert(LevenshteiinCompareStrategy(), dict)
        score = analyzer.cal_similiarity(text_src, text_exmine)
        assert score > 0

        score = analyzer.cal_similiarity(text_src, "")
        assert score == len(text_src)

        score = analyzer.cal_similiarity("", text_exmine)
        assert score == len(text_exmine)

        analyzer = GanHuaExpert(JaccardCompareStrategy(), dict)
        diff_score = analyzer.cal_similiarity(text_src, text_exmine)
        assert diff_score > 0.8

        diff_score = analyzer.cal_similiarity(text_src, "")
        assert diff_score == 1.0

        diff_score = analyzer.cal_similiarity("", text_exmine)
        assert diff_score == 1.0

    def test_random_pick(self):
        dict = GanHuaDict()
        dict.load_from_file("data/ganhua_dict.json")
        analyzer = GanHuaExpert(LevenshteiinCompareStrategy(), dict)

        gan_hua = analyzer.random_pick(1)
        assert len(gan_hua) == 1

        gan_hua = analyzer.random_pick(5)
        assert len(gan_hua) == 5

        gan_hua = analyzer.random_pick(0)
        assert len(gan_hua) == 0