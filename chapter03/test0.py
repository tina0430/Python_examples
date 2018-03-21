a = 1
def kbs():
    a = 2
    print('kbs에서 출력1:', a)
    def mbc():
        global a
        print('mbc에서 출력:', a)
        a = 3
    mbc()
    print('kbs에서 출력2:', a)
kbs()