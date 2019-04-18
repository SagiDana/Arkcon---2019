import socket

if __name__ == '__main__':

    TCP_IP = '54.93.40.66'
    TCP_PORT = 1337
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    
    print(s.recv(BUFFER_SIZE))
    print(s.recv(BUFFER_SIZE))
    print(s.recv(BUFFER_SIZE))
    print(s.recv(BUFFER_SIZE))
    
    s.close()