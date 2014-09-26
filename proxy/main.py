import time
import httplib
from websocket import create_connection

WS_URL = "ws://localhost:9000/_ws/test"

def run():
    socket = create_connection(WS_URL)
    while True:
        msg = socket.recv().decode("utf-8").split("\n")
        conn = httplib.HTTPConnection("icplayer.com")
        conn.request(msg[0], msg[1], msg[2])
        response = conn.getresponse()
        if response.status == 301:
            conn = httplib.HTTPConnection("bluenotepad.com")
            conn.request(msg[0], response.getheader("location", msg[1]), msg[2])
            response = conn.getresponse()
            
        headers = str(response.status) + "\n"
        for (k,v) in response.getheaders():
            headers += k + ":" + v + "\n"
        headers += "\n" 
        body = response.read() 
        resp = bytes(headers + body)
        socket.send_binary(resp)


if __name__ == "__main__":
    while True:
        try:
            run()
        except Exception as e:
            print(type(e))
        time.sleep( 5 )
    
