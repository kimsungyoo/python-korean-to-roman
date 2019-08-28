import urllib
from urllib import parse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup

NAVER_NAME_TO_ROMAN_URL = 'https://dict.naver.com/name-to-roman/translation/?query='


def korean_to_roman(text):
    name_url = NAVER_NAME_TO_ROMAN_URL + urllib.parse.quote(text)
    req = Request(name_url)
    res = urlopen(req)
    html = res.read().decode('utf-8')
    bs = BeautifulSoup(html, 'html.parser')
    name_tags = bs.select('#container > div > table > tbody > tr > td > a')

    return [name_tag.text for name_tag in name_tags]
