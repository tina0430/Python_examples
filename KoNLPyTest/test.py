from konlpy.tag import Kkma
from konlpy.utils import pprint

kkma = Kkma()

pprint(kkma.nouns(u'명사만을 추출하여 워드 클라우드를 그려봅니다.'))