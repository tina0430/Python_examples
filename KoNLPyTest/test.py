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

