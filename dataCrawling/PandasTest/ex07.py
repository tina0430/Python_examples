#board.csv / member.csv 이용
# 회원 데이터를 DataFrame으로 만들되, 신사임당은 목록에서 제외
# 급여가 300원 이상인 사람만 조회 - 이 데이터를 이용하여 수평 막대 그래프 그리기
# 게시물 데이터를 DataFrame으로 만들어 보기
# 게시물 남긴 사람들의 이름, 성별, 제목, 글 내용을 DataFrame으로 만들어보기
# 성별 급여의 총합을 pie 그래프로 만들기

import pandas as pd
import csv

f = open('member.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    print(line)
f.close()   