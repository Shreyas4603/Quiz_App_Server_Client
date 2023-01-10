import socket
import time

# IP=socket.gethostbyname(socket.gethostname())
# print(f"Client host : {IP}")


SIZE = 1024 * 2
FORMAT = 'utf-8'
DISCONNECT_MSG = '!DISCONNECT'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connect(IP):
    print(f'[IN CONNECT INTERFACE]{IP}')
    PORT = 5555
    ADDR = (IP, PORT)
    global client
    client.connect(ADDR)
    print(f'[CONNECTED] Client connected at {IP} : {PORT}')


def load(path, cmd="!LOAD"):
    command = cmd + "$" + str(path)
    command = command.encode(FORMAT)
    client.send(command)
    print('[LOAD AND PATH SENT TO SERVER]')


def fetch(cmd='!FETCH'):
    command = cmd + "$" + '_'
    command = command.encode(FORMAT)
    client.send(command)
    print('[FETCH SENT TO SERVER]')

    fetchData = client.recv(SIZE).decode(FORMAT)
    print('[DATA RECIEVED FROM SERVER] = ', fetchData)
    return fetchData


def result(alias, score, cmd='!RESULTS'):
    print('[RESULT INTERFACE]')
    command = cmd + "$" + alias + '#' + score
    command = command.encode(FORMAT)
    client.send(command)
    print("RESULT CMD SENT TO SERVER")


def dis(cmd='!DC'):
    command = cmd + "$" + '_'
    client.send(command.encode(FORMAT))


def stopServer(quizname,cmd='!STOP$'):
    print('[STOP SENT]')
    command=cmd+quizname
    client.send(command.encode(FORMAT))

