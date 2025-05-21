from textconverter.core import *

def test_decode_url():
    assert decode_url("%20") == " "
    assert decode_url("%22Hi%22") == '"Hi"'

def test_decode_escapes():
    assert decode_escapes("\\x22Hi\\x22") == '"Hi"'
    assert decode_escapes("\\u0020") == " "

def test_decode_html():
    assert decode_html("&quot;Hi&quot;") == '"Hi"'
    assert decode_html("&amp;") == "&"

def test_decode_all():
    assert decode_all("%22\\x22Hi\\x22%22") == '"Hi"'
    assert decode_all("&quot;Hi&quot;") == '"Hi"'