from vidstream import StreamingServer
import threading

sender = StreamingServer('4.tcp.ngrok.io', 9999)

t = threading.Thread(target=sender.start_server)
t.start()

while input("") != 'STOP':
    continue

sender.stop_server()