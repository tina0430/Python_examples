from http.server import CGIHTTPRequestHandler, HTTPServer

port = 8888
class Handler(CGIHTTPRequestHandler):
    cg_direction = ['/cgi-bin']
    
serv = HTTPServer(('127.0.0.1', port), Handler)

print('웹 서버 서비스 시작')
serv.serve_forever()