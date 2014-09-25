
import httplib
from websocket import create_connection

WS_URL = "ws://localhost:9000/_ws/test"

def run():
    socket = create_connection(WS_URL)
    conn = httplib.HTTPConnection("bluenotepad.com")
    while True:
        msg = socket.recv()
        conn.request("GET",msg)
        response = conn.getresponse()
        headers = ""
        for (k,v) in response.getheaders():
            headers += k + ":" + v + "\n"
        headers += "\n" 
        body = response.read() 
        socket.send(headers + body)


if __name__ == "__main__":
    run()
