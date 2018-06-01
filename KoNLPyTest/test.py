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
# 
# from konlpy.tag import Kkma
# from konlpy.utils import pprint
# 
# kkma = Kkma()
# 
# pprint(kkma.nouns(u'명사만을 추출하여 워드 클라우드를 그려봅니다.'))






from konlpy.tag import Twitter
# from ckonlpy.tag import Twitter
import time

def write_list(data, fileobj):
    for i, line in enumerate(data):
        fileobj.write(line)
        if i > 0 and i % 5 == 0:
            fileobj.write('\n')
        else:
            fileobj.write('  ')

def write_pos(pos_data, fileobj):
    for i, line in enumerate(pos_data):
        txt = '('
        for j, cell in enumerate(line):
            if j == 0:
                txt = txt + ' %s' %cell
            else:
                txt = txt + ' %s )'%cell
        
        fileobj.write(txt)

        if i > 0 and i % 5 == 0:
            fileobj.write('\n')
        else:
            fileobj.write('  ')

def  run_twitter(news):
    twitter = Twitter()
    start_time = time.time()
    print('twitter 시작')
    twitter_nouns = twitter.nouns(news)
    end_time = time.time()
    print('twitter 끝 - %s 초' % str(end_time - start_time) )
    
    #저장할 txt 파일 경로 및 이름 설정
    with open('twitter_noun.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('twitter_nouns\n')
        write_list(twitter_nouns, fstream)
        fstream.write('\n\n')

if __name__ == '__main__':
    twitter = Twitter()
    #읽어올 json 파일 경로 및 이름 설정
    with open('./news20171221.json', 'r', encoding='utf-8') as f:
        jdata = json.load(f)
    cnt = len(jdata)
    news = ''
    for i in range(1, cnt-1):
        news += jdata['news'+str(i+1)]['title'] + ' '
        news += jdata['news'+str(i+1)]['contents'] + ' '
 
    run_twitter(news)


