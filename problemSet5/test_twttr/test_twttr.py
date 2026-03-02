# test_twttr.py
# Andrew


from twttr import shorten


def test_vowel_replace_noSpace():
    """ no space """
    assert shorten("heythere") != "hey there"


def test_vowel_replace_low():
    """ vowel replacement """
    assert shorten("HEY THERE") != "HEY THERE"


def test_vowel_replace_cap():
    """ vowel replace without cap """
    assert shorten("hey there") != "hey there"


def test_shorten_noNum():
    """ We don't want numbers anymore """
    assert shorten("H3y th3r3") != "Hy thr"


def test_shorten_Cap():
    """ No Cap """
    assert shorten("hey there") != "HY THR"


def test_shorten_noPun():
    """ lets get ride of puncutation """
    assert shorten("Hey there!") != "Hy thr"
