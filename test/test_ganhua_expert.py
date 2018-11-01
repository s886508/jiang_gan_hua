# -*- coding=utf-8 -*-
from ..ganhua import GanHuaDict
from ..ganhua_expert import GanHuaExpert
from ..text_compare.strategy import JaccardCompareStrategy

class TestGanHuaExpert:

    def test_similarity_dict(self):
        dict = GanHuaDict()

        # Dictionary has not loaded.
        text = "薪水高低很重要"
        analyzer = GanHuaExpert(JaccardCompareStrategy())
        similars = analyzer.query_similiar_from_dict(text, 1, dict)
        assert len(similars) == 0

        # Load dictionary and query.
        dict.load_from_file("data/ganhua_dict.json")
        similars = analyzer.query_similiar_from_dict(text, 1, dict)
        assert len(similars) == 1

        similars = analyzer.query_similiar_from_dict(text, 30, dict)
        assert len(similars) == 30

        # Query more than dictionary.
        similars = analyzer.query_similiar_from_dict(text, 60, dict)
        assert len(similars) != 60

    def test_similarity_single_sentence(self):
        text_src = "反對修法假新聞，政府自己不要造謠"
        text_exmine = "假新聞要關三天"


        analyzer = GanHuaExpert(JaccardCompareStrategy())
        score = analyzer.cal_similiarity(text_src, text_exmine)
        assert score > 0

        score = analyzer.cal_similiarity(text_src, "")
        assert score == 0

        score = analyzer.cal_similiarity("", text_exmine)
        assert score == 0
