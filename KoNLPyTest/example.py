from konlpy.tag import Kkma
from konlpy.tag import Komoran
# from konlpy.tag import Twitter
from ckonlpy.tag import Twitter
from konlpy.tag import Hannanum

import time
import json
from itertools import count

news1 = '''
[fn 오후시황]코스피 개인 및 외국인 매도에 2470선으로 밀려

코스피가 개인 및 외국인 매도에 2470선으로 밀렸다. 

코스피는 14일 오후 1시 40분 전거래일 대비 3.46포인트(0.14%) 내린 2474.25에 거래되고 있다. 

이날 코스피는 전 거래일 대비 5.26포인트(0.21%) 오른 2482.97에 개장했다. 

기관은 1133억원을 순매수했다. 하지만 개인과 외국인이 각각 701억원, 563억원을 순매도하며 지수를 끌어내렸다. 

규모별로 대형주(-0.44%)는 하락세다. 반면 중형주(1.46%), 소형주(1.03%)는 상승세다. 업종별로 철강 및 금속(3.42%), 기계(1.35%), 비금속광물(9.13%) 등이 상승세다. 반면 전기 전자(-1.78%), 의약품(-1.87%)은 하락세다. 

시가총액 상위종목별로 삼성전자(-2.53%), SK하이닉스(-1.05%), 삼성물산(-1.54%) 등은 하락세다. 반면 포스코(3.21%), LG화학(2.17%) 등은 상승세다. 

코스닥은 전거래일 대비 4.78포인트(0.55%) 내린 861.15에 거래되고 있다. 

ggg@fnnews.com 강구귀 기자 
'''

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
        
def run_kkma():
    kkma = Kkma()
    start_time = time.time()
    print('kkma 시작')
    kkma_morphs = kkma.morphs(news1)
    kkma_nouns = kkma.nouns(news1)
    kkma_pos = kkma.pos(news1)
    end_time = time.time()
    print('kkma 끝 - %s 초' % str(end_time - start_time) )
    kkma_sentences = kkma.sentences(news1)
    
    with open('kkma.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('kkma time : %s s\n' % str(end_time - start_time) )
        fstream.write('kkma_morphs\n')
        write_list(kkma_morphs, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_nouns\n')
        write_list(kkma_nouns, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_pos\n')
        write_pos(kkma_pos, fstream)
        fstream.write('\n\n')
        
        fstream.write('kkma_sentences\n')
        write_list(kkma_sentences, fstream)
        fstream.write('\n')

def run_komoran():
    komoran = Komoran()
    start_time = time.time()
    print('komoran 시작')
    komoran_morphs = komoran.morphs(news1)
    komoran_nouns = komoran.nouns(news1)
    komoran_pos = komoran.pos(news1)
    end_time = time.time()
    print('komoran 끝 - %s 초' % str(end_time - start_time) )
    
    
    with open('komoran.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('komoran time : %s s\n' % str(end_time - start_time) )
        fstream.write('komoran_morphs\n')
        write_list(komoran_morphs, fstream)
        fstream.write('\n\n')
        
        fstream.write('komoran_nouns\n')
        write_list(komoran_nouns, fstream)
        fstream.write('\n\n')
        
        fstream.write('komoran_pos\n')
        write_pos(komoran_pos, fstream)
        fstream.write('\n')
    
def run_hannanum():
    hannanum = Hannanum()
    start_time = time.time()
    print('hannanum 시작')
    hannanum_morphs = hannanum.morphs(news1)
    hannanum_nouns = hannanum.nouns(news1)
    hannanum_pos = hannanum.pos(news1)
    end_time = time.time()
    print('hannanum 끝 - %s 초' % str(end_time - start_time) )
    
    with open('hannanum.txt', 'w', encoding = 'utf-8') as fstream:
        fstream.write('hannanum time : %s s\n' % str(end_time - start_time) )
        fstream.write('hannanum_morphs\n')
        write_list(hannanum_morphs, fstream)
        fstream.write('\n\n')
        
        fstream.write('hannanum_nouns\n')
        write_list(hannanum_nouns, fstream)
        fstream.write('\n\n')
        
        fstream.write('hannanum_pos\n')
        write_pos(hannanum_pos, fstream)
        fstream.write('\n')
        
def  run_twitter(news):
    twitter = Twitter()
    start_time = time.time()
    print('twitter 시작')
#     twitter_morphs = twitter.morphs(news)
    twitter_nouns = twitter.nouns(news)
#     twitter_pos = twitter.pos(news)
    end_time = time.time()
#     print(twitter_pos)
    print('twitter 끝 - %s 초' % str(end_time - start_time) )
    
    with open('twitter_noun.txt', 'w', encoding = 'utf-8') as fstream:
#         fstream.write('twitter time : %s s\n' % str(end_time - start_time) )
#         fstream.write('twitter_morphs\n')
#         write_list(twitter_morphs, fstream)
#         fstream.write('\n\n')
#         
        fstream.write('twitter_nouns\n')
        write_list(twitter_nouns, fstream)
        fstream.write('\n\n')
        
#         fstream.write('twitter_pos\n')
#         write_pos(twitter_pos, fstream)
#         fstream.write('\n')


if __name__ == '__main__':
    twitter = Twitter()
#     twitter.add_dictionary('멍멍이', 'Noun')
    with open('./news20171221.json', 'r', encoding='utf-8') as f:
        jdata = json.load(f)
    cnt = len(jdata)
    news = ''
    for i in range(1, cnt-1):
        news += jdata['news'+str(i+1)]['title'] + ' '
        news += jdata['news'+str(i+1)]['contents'] + ' '
 
    run_twitter(news)
#     run_twitter('만복이는 뛰기도하고 걷기도 하지만 날지는 못하는 멍멍이다')
#     run_kkma()
#     run_komoran()
#     run_hannanum()