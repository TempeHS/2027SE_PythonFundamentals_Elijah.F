from twttr import shorten


def test_LetterA():
    assert shorten("Sarahnannynanny") == "Srhnnnynnny"


def test_ShortLetter():
    assert shorten("Heya") == "Hy"
    assert shorten("Cricket") == "Crckt"
