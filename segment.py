import jieba

jieba.set_dictionary("data/dict.txt.big")

def tokenize(text):
    """
    Do segmentation of given text.
    :param text(str): Text to segment.
    :return: List of tokens.
    """
    return jieba.lcut(text, cut_all=False)