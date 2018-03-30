import pandas as pd

def setNewAddress(store):
    filepath = './storeinfo/'
    table = pd.read_csv(filepath+store+'.csv', encoding='utf-8', index_col=0, header=0)
    # print(table)
    sido_alias = """서울시:서울특별시 서울:서울특별시 강원:강원도 경기:경기도 충남:충청남도  
                        충북:충청북도 경남:경상남도 경북:경상북도 전남:전라남도 전북:전라북도 
                        제주도:제주특별자치도 제주:제주특별자치도 제주시:제주특별자치도
                        세종시:세종특별자치시 세종:세종특별자치시
                        대전시:대전광역시 대전:대전광역시 대구시:대구광역시 대구:대구광역시
                        인천시:인천광역시 인천:인천광역시 광주시:광주광역시 광주:광주광역시
                        울산시:울산광역시 울산:울산광역시 부산시:부산광역시 부산:부산광역시"""
                        
    gungu_alias = """고양시일산서구:고양시 고양시덕양구:고양시 고양시일산동구:고양시
                    부천시오정구:부천시 부천시소사구:부천시 부천시원미구:부천시
                    안산시단원구:안산시 안산시상록구:안산시
                    안양시동안구:안양시 안양시만안구:안양시
                    성남시중원구:성남시 성남시중원구:성남시 성남시분당구:성남시 성남시수정구:성남시 
                    양편군:양평군 여주군:여주시
                    수원시권선구:수원시 수원시장안구:수원시 수원시권선구:수원시 수원시영통구:수원시 수원시팔달구:수원시
                    용인시기흥구:용인시 용인시수지구:용인시 용인시처인구:용인시
                    포항시북구:포항시 포항시남구:포항시
                    창원시마산회원구:창원시 마산회원구:마산시 창원시진해구:창원시 진해시:창원시
                    창원시마산합포구:창원시 창원시회원구:창원시 창원시성산구:창원시 창원시의창구:창원시
                    상주시낙양동:상주시 상주시사벌면:상주시
                    청주시흥덕구:청주시 청주시서원구:청주시 청주시상당구:청주시 청주시청원구:청주시
                    천안시서북구:천안시 천안시동남구:천안시 
                    전주시덕진구:전주시 전주시완산구:전주시
                    성주읍:성주군 의성읍:의성군 강화읍:강화군 웅진군:옹진군
                    구좌읍:제주시 북제주군:제주시 신광로:제주시 용문로:제주시 천수로:제주시
                    군포시금정동79-1:군포시 군포시금정동79-1:군포시
                    세종특별자치시:세종시 조치원읍:세종시 
                    한솔동:세종시 도담동:세종시 도움3로:세종시 도움8로:세종시
                    나리로:세종시 갈매로:세종시 마음로:세종시 보듬3로:세종시 
                    소담1로:세종시 호려울로:세종시 누리로:세종시 달빛로:세종시
                    연기면:세종시 연동면:세종시 전의면:세종시
                    금남면:세종시 부강면:세종시 연서면:세종시 장군면:세종시 가름로:세종시 새롬중앙로:세종시
                    전동면:세종시 당진군:당진시 청원군:청주시 마산시:창원시"""
                        
    sido_dict = dict(aliasset.split(':') for aliasset in sido_alias.split())
    table.sido = table.sido.apply(lambda v :sido_dict.get(v, v))
    #표준화된 행정 구역 데이터로 머지 테스트
    sido_table = pd.read_csv('district.csv', encoding='utf-8', header=0)
    m = pd.merge(table, sido_table, on=['sido', 'gungu'], 
                 how='outer',suffixes=['', '_'], indicator=True)
    m_result = m.query('_merge == "left_only"')
#     m_result[['sido', 'gungu']]
    
    #군구에 대한 보정
    gungu_dict = dict( aliasset.split(':') for aliasset in gungu_alias.split())
    table.gungu = table.gungu.apply(lambda v : gungu_dict.get(v, v))
    
    #예외처리
    table = table.dropna(subset=['sido'])
    for gungu_nan in table.isnull().gungu:
        print(table.address)
    table.loc[table.sido =='세종특별자치시', 'gungu'] = '세종시'
    
    #최종 확인? - 아무런 결과가 안나와야 성공
    m = pd.merge(table, sido_table, on=['sido', 'gungu'],
                 how='outer',suffixes=['', '_'], indicator=True)
    m_result = m.query('_merge == "left_only"')
    print(m_result[['sido', 'gungu', 'address']])
    
    table.to_csv(filepath+store+'Modify.csv')
    
if __name__ == "__main__":
    setNewAddress('pelicana')