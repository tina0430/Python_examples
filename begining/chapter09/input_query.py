import urllib.parse

def input_query_plus():
    q = urllib.parse.quote_plus('가나다 라')
    return "&query="+q

print('결과 1 :', input_query_plus())

def input_query():
    q = urllib.parse.quote('가나다 라')
    return "&query="+q

print('결과 2 :', input_query())