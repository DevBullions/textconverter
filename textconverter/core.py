from urllib.parse import unquote
import codecs
import html

def decode_url(text: str) -> str:
    """Decode URL-encoded text (%22 → ")"""
    return unquote(text)

def decode_escapes(text: str) -> str:
    """Decode hex/unicode escapes (\x22 → ")"""
    return codecs.escape_decode(text.encode('latin-1'))[0].decode('utf-8')

def decode_html(text: str) -> str:
    """Decode HTML entities (&quot; → ")"""
    return html.unescape(text)

def decode_all(text: str) -> str:
    """Universal decoder (handles URL, escapes, HTML in one pass)"""
    text = decode_url(text)
    text = decode_escapes(text)
    text = decode_html(text)
    return text