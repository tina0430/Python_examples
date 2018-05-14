from konlpy.tag import Twitter
import json 
# import codecs
# “ ” …

with open('./news.json', 'r', encoding='utf-8') as f:
    jdata = json.load(f)

# print(jdata)

import platform
print(platform.architecture())
# twitter = Twitter()
# Twitter.nouns(jdata['news1']['title'])

from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()

pprint(kkma.nouns(u'명사만을 추출하여 워드 클라우드를 그려봅니다.'))