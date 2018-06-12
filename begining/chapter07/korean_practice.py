'''
Created on 2018. 5. 8.

@author: 즤
'''

import re

title = "\n\t\t\t\t\t\t\t  \t   \n\t\t\t\t\t\t\t\t  \t\t\n\t\t\t\t\t\t\t\t\t\t초저녁 호텔 식음료를 저렴하게 이용하는 '해피아워'\n\t\t\t\t\t\t\t\t   \n\t\t\t\t\t\t\t  \t"
contents = ['\n\t\t\t\t\t\t\t 우리은행이 전산 시스템을 교체한 첫날인 8일 모바일·인터넷뱅킹 접속이 지연되는 등 이용자들이 불편을 겪었다.', 
            '이날 우리은행 등에 따르면 우리은행은 지난 5~7일 사흘간 전산 시스템 교체를 위해 금융 서비스를 중단한 뒤 이날 자정을 기해 차세대 전산시스템인 ‘위니(WINI)’를 가동했다.', 
            '하지만 이날 오전부터 모바일뱅킹인 ‘원터치개인뱅킹’ 애플리케이션(앱)에 접속하면 ‘통신 중 오류가 발생했습니다’라는 알림 메시지만 뜨고 접속이 지연되는 현상이 벌어졌다. 우리은행 측은 “전산 시스템 자체에 문제가 있는 것은 아니며 모바일뱅킹에 접속자가 몰리면서 오전 한 때 일시적으로 접속이 지연됐다”며“현재는 인터넷뱅킹·모바일뱅킹 모두 정상 가동 중”이라고 말했다.', 
            '▶ ', '[경향비즈 바로가기]', ', 경향비즈 SNS ', '[페이스북]', ' ', 
            ' ▶ ', '[인기 무료만화 보기]', '[©경향신문(', 'www.khan.co.kr', '), 무단전재 및 재배포 금지]', 
            '경향신문 관련뉴스', '언론사 페이지로 이동합니다.', '등산객이 지리산서 100년 넘은 천종산삼 발견, 가격이···', 
            "이스라엘서 '신발 디저트' 제공받은 아베···예술이냐, 경멸이냐", '김경란, 근황과 함께 셀카 공개…이혼 심경 발표 후 첫 모습', 
            '[팩트체크] 한국 스마트폰 요금, 41개국 중 2위 맞나', "[단독]남북 접경지에 '평화발전소' 건설 추진", '\n\t\t\t\t\t\t'
            ]
print(title.strip())

con = ''
for i in contents:
    i = i.strip()
    if re.findall('▶', i):
        break
    else:
        con += i
        
print(con)