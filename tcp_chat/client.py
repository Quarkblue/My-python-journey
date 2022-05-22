import socket
import threading

nickname = input("Choose a nickname: ")

if nickname == 'admin':
    password = input("Enter admin password: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 12))

stop_thread = False

def recieve():
    while True:
        global stop_thread
        if stop_thread:
            break
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
                next_message = client.recv(1024).decode('ascii')
                if next_message == 'PASS':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'DECLINE':
                        print('[ACCESS DENIED] Wrong password')
                        stop_thread = True

                elif next_message == 'BAN':
                    print('Connection Refusedbecause of ban')
                    client.close()
                    stop_thread = True
            else:
                print(message)

        except:
            print("[ERROR]An error occured")
            client.close()
            break


def write():
    while True:
        if stop_thread:
            break
        message = f'{nickname}: {input("=>")}'
        if message[len(nickname)+2:].startswith('/'):
            if nickname == 'admin':
                if message[len(nickname)+2:].startswith('/kick'):
                    client.send(f'KICK {message[len(nickname)+2+6:]}'.encode('ascii'))
                elif message[len(nickname)+2:].startswith('/ban'):
                    client.send(f'BAN {message[len(message)+2+5:]}'.encode('ascii'))
            else:
                print("Commands can only be executed by the admin")
        else:
            client.send(message.encode('ascii'))


recieve_thread = threading.Thread(target=recieve)
recieve_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
