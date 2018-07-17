import win32com.client
import pythoncom
import json

class XSession:
    """ 
    classmethod get_instance() 를 사용하여, instance 를 만들어야함.
    """

    def __init__(self):
        self.login_state = 0
    
    def OnLogin(self, code, msg): # event handler
        """
        Login 이 성공적으로 이베스트 서버로 전송된후,
                  로그인 결과에 대한 Login 이벤트 발생시 실행되는 event handler
        """
        if code == "0000":
            print("로그인 ok\n")
            self.login_state = 1
        else:
            self.login_state = 2
            print("로그인 fail.. \n code={0}, message={1}\n".format(code, msg))

    
    def api_login(self, id="myid", pwd="pass", cert_pwd="pass2"): 
#         self.ConnectServer('hts.ebestsec.co.kr', 20001)
        self.ConnectServer('demo.etrade.co.kr', 20001)
        is_connected = self.Login(id, pwd, cert_pwd, 0, False) # 로그인 하기
    
        if not is_connected: # 서버에 연결 안되거나, 전송 에러시
            print("로그인 서버 접속 실패... ")
            return
        
        while self.login_state == 0:
            pythoncom.PumpWaitingMessages()
    
    def account_info(self):
        """
                    계좌 정보 조회
        """
        if self.login_state != 1: # 로그인 성공 아니면, 종료
            return
        
        account_no = self.GetAccountListCount()
        
        print("계좌 갯수 = {0}".format(account_no))
            
        for i in range(account_no):
            account = self.GetAccountList(i)
            print("계좌번호 = {0}".format(account))
    
    @classmethod
    def get_instance(cls):
        # DispatchWithEvents로 instance 생성하기
        xsession = win32com.client.DispatchWithEvents("XA_Session.XASession", cls)
        return xsession
    
if __name__ == "__main__":
            
    # id, 암호 - 모의 투자
    # server_adress = 'demo.etrade.co.kr' #"hts.ebestsec.co.kr"

    with open('login.json', 'r') as loginInfo:
        login = json.load(loginInfo)
        
    id = login['id']
    passwd = login['demo_passwd']
    cert_passwd = login['cert_passwd']
    xsession = XSession.get_instance()
    xsession.api_login(id, passwd, cert_passwd)
    
    xsession.account_info()
    print("------END------")

