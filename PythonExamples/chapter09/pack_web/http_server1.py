from http.server import SimpleHTTPRequestHandler, HTTPServer

port = 7777
handler = SimpleHTTPRequestHandler
serv = HTTPServer(('127.0.0.1', port), handler)
print('웹 서비스 시작')
serv.serve_forever()    #심플 서버 서비스가 시작됨