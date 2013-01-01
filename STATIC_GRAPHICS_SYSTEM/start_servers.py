import SimpleHTTPServer
import SocketServer
import serial2ws.serial2ws


Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", 8000), Handler)
print "serving HTTP at port 8000..."
httpd.serve_forever()
serial2ws.main()
