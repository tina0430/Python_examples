from datetime import datetime
import win32com.client
import pythoncom
import pandas as pd
import time
import json
import math 

from Xing_API import xing_login


class XQuery_t8415:
    def __init__(self):
        super().__init__()
        self.is_data_received = False

        
#     이베스트 서버에서 ReceiveData 이벤트 받으면 실행되는 event handler
    def OnReceiveData(self, tr_code):       
        self.is_data_received = True
        
        date = self.GetFieldData("t8415OutBlock1", "date", 0)
        time = self.GetFieldData("t8415OutBlock1", "time", 0)
        open_price = self.GetFieldData("t8415OutBlock1", "open", 0)
        high_price = self.GetFieldData("t8415OutBlock1", "high", 0)
        low_price = self.GetFieldData("t8415OutBlock1", "low", 0)
        close_price = self.GetFieldData("t8415OutBlock1", "close", 0)
        jdiff_vol = self.GetFieldData("t8415OutBlock1", "jdiff_vol", 0)
        
        print(date, time, open_price, high_price, low_price, close_price, jdiff_vol)
        print("TR code => {0}".format(tr_code))

#     이베스트 서버에 일회성 TR data 요청함.
    def request(self):
        self.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t8415.res"

        self.SetFieldData("t8415InBlock", "shcode", 0, "101N9000")
        self.SetFieldData("t8415InBlock", "ncnt", 0, '100')
        self.SetFieldData("t8415InBlock", "qrycnt", 0, "100")
        self.SetFieldData("t8415InBlock", "nday", 0, "0")
        self.SetFieldData("t8415InBlock", "sdate", 0, "20180715")
        self.SetFieldData("t8415InBlock", "edate", 0, "20180716")
        self.SetFieldData("t8415InBlock", "comp_yn", 0, "N")
        
        err_code = self.Request(False) # data 요청하기 -- 연속조회인경우만 True
        
        if err_code < 0:
            print("error... {0}".format(err_code)) # data 요청하기 -- 연속조회인경우만 True

    @classmethod
    def get_instance(cls):
        xq_t8415 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", cls)
        return xq_t8415

class XReal_t8415_:
    def __init__(self):
        super().__init__()
        
        self.next_time = 930   #파일을 중간 중간 저장..? append
        
        self.count = 0
        self.state = 0
        
        self.result = []
        self.result_1m = []
        self.result_30m = []
        
        self.t_pivot1 = 0
        self.t_pivot2 = 0
        
#     이베스트 서버에서 ReceiveRealData 이벤트 받으면 실행되는 event handler
    def OnReceiveRealData(self, tr_code): # event handler
        self.count += 1
        self.state = 1
        
        chetime = self.GetFieldData("OutBlock", "chetime")
        now_price = self.GetFieldData("OutBlock", "price")
        open_price = self.GetFieldData("OutBlock", "open")
        high_price = self.GetFieldData("OutBlock", "high")
        low_price = self.GetFieldData("OutBlock", "low")
        cvolume = self.GetFieldData("OutBlock", "cvolume")
        self.result.append([chetime, now_price, open_price, high_price, low_price, cvolume])
        
        if self.count > 1 :
            self.t_pivot1 = self.time_pivot2
            self.t_pivot2 = chetime
        else : 
            self.t_pivot1 = chetime
            self.t_pivot2 = chetime
        
        if self.t_pivot2 %100 == 0 :
            self.result_1m.append(self.t_pivot2, now_price, open_price, high_price, low_price, cvolume)
        elif self.t_pivot2[3] - self.t_pivot1[3] == 1 :
            self.result_1m.append(self.t_pivot2, now_price, open_price, high_price, low_price, cvolume)
            
        
        print(self.count, chetime, open_price, high_price, low_price, cvolume)
        
        #한 시간 마다 한 번씩 파일 저장
        if int(chetime)[:4] > self.next_time + 100 :
            self.file_save(0)
            self.next_time += self.next_time + 100
            
        #야간 주간 케이스 나누기
        if int(chetime) >= 235900 :
            self.state = 2
    
    def file_save(self, mode):
        columns = ['chetime', 'price', 'open', 'high', 'low', 'cvolume']
        edate = datetime.today().strftime("%Y%m%d")
        
        #실시간 데이터 저장
        if mode == 0 :
            result_df = pd.DataFrame(self.result)
            file_name = './real_{}.csv'.format(edate)
        
        if mode == 1 :
            result_df = pd.DataFrame(self.result_1m)
            file_name = './real_{}_1m.csv'.format(edate)
            
        if mode == 30 :
            result_df = pd.DataFrame(self.result_30m)
            file_name = './real_{}_30m.csv'.format(edate)
                
        result_df.to_csv(file_name, index=False, header=columns)
        
    
#     이베스트 서버에 실시간 data 요청함.
    def start(self):
        
        self.ResFileName = "C:\\eBEST\\xingAPI\\Res\\FC0.res" # RES 파일 등록
        self.SetFieldData("InBlock", "futcode", "101N9000")

        self.AdviseRealData() # 실시간데이터 요청
    
    def end(self):
        self.file_save(0)
        self.UnadviseRealData() # 실시간데이터 요청 취소
    
    @classmethod
    def get_instance(cls):
        xreal = win32com.client.DispatchWithEvents("XA_DataSet.XAReal", cls)
        return xreal

if __name__ == "__main__":
    def get_single_data():
        xq_t8415 = XQuery_t8415.get_instance()
        xq_t8415.request()
    
        while xq_t8415.is_data_received == False:
            pythoncom.PumpWaitingMessages()
    
    
    def get_real_data():
        xreal = XReal_t8415_.get_instance()
        xreal.start()

        while xreal.state < 2:
            pythoncom.PumpWaitingMessages()
            
#         while xreal.count < 1000:
#             pythoncom.PumpWaitingMessages()
#             if xreal.count == 5:
#                 xreal.add_item("003490") # 대한항공 추가
#             
#             if xreal.count == 20:
#                 xreal.remove_item("005930")
#             
#             if xreal.count == 1000:
#                 xreal.end()
#                 time.sleep(10)
#                 print("---- end -----")
#                 break
        xreal.end()
    
    with open('login.json', 'r') as loginInfo:
        login = json.load(loginInfo)
        
    id = login['id']
    passwd = login['demo_passwd']
    cert_passwd = login['cert_passwd']
    
    xsession = xing_login.XSession.get_instance()
    xsession.api_login(id, passwd, cert_passwd)
    
    get_single_data()
    get_real_data()
