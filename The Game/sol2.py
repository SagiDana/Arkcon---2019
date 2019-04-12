def reverse_server_logic(guess, magic):
    magics = ""
    for i in range(len(guess)):
        magics += magic[i % len(magic)]

    bufs = []
    for i in range(len(guess)):
        

        c = ord(guess[i])

        if 65 <= c <= 90:
            c -= 65
            c = c - (ord(magics[i]) - 65)

            c %= 26

            c += 65
            bufs += chr(c)
        elif 97 <= c <= 122:
            c -= 97

            if guess[i] == 'u':
                print(c)
            c = c - (ord(magics[i].lower()) - 97)
            
            if guess[i] == 'u':
                print(c)
            
            c %= 26
            c += 97
            
            if guess[i] == 'u':
                print(c)

            bufs += chr(c)
        else:
            bufs += chr(c)

    print(''.join(bufs))


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

    print("".join(bufs))

if __name__ == '__main__':
    magic = ["M", "A", "G", "I", "C"]

    flag = "t3@zf_u_t!w3_0x3rcz1faa_r01t73d5"
    reverse_server_logic(flag, magic)

    _ = "h3@rd_u_l!k3_0v3rwr1tAUSp01n73r5"
    server_logic(_, magic)


#ArkCon{L3@rd_u_l!k3_0v3rwr173d_p01n73r5}