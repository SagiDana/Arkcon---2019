from requests import *

import hashlib
import binascii


def decode_php(php):
    decoded = ""
    for c in php:
        if 97 <= ord(c) <= 122:
            new_char = ord(c) - 20
            if new_char < 97:
                new_char = 123 - (97 - new_char)
            decoded += chr(new_char)
        elif 65 <= ord(c) <= 90:
            new_char = ord(c) - 20
            if new_char < 65:
                new_char = 91 - (65 - new_char)
            decoded += chr(new_char)
        else:
            decoded += c
    return decoded

def xor(s, k):
    ciphered = ""
    for i in range(len(s)):
        new_c = chr(ord(s[i]) ^ ord(k[i%len(k)]))

        ciphered += new_c
    return ciphered

def calc_basket(coach, jersey):
    r = "20190429_71070_e7707_1312_3_14159265359"
    r_1 = r[jersey:] + r[:jersey]
    r_2 = r_1.replace('_', coach)
    return r_2

def calc_harame_1(harame):
    # return hashlib.md5(harame[::-1]).hexdigest()1
    return "3d30a444"

def calc_harame_2(harame, basket):
    _ = xor(harame, basket)
    return _

def calc_ball_1(basket):
    return hashlib.md5(basket).hexdigest()

def calc_ball_2(server_ball, jersey):
    return ""

def create_ball(server_ball, end_result):
    _hash = server_ball

    ret_s = ""
    for i in range(len(_hash)):
        _ = ord(_hash[i]) ^ ord(end_result[i])
        ret_s += "{:02x}".format(_)
    
    # print(ret_s)
    return ret_s

def apost():
    hints = []
    while True:
        url = "http://18.185.240.42"

        # print(binascii.crc32("8"))

        key = "17d978cb"
        harame = "aaaaa"
        coach = "0"
        jersey = 14

        basket = calc_basket(coach, jersey)
        print(basket)
        server_ball = calc_ball_1(basket)
        # print(server_ball)

        ball = create_ball(server_ball, "00000000000000000000000000000593")

        server_harame_1 = calc_harame_1(harame)

        server_ball = calc_ball_2(server_ball, jersey)
        
        server_harame_2 = calc_harame_2(server_harame_1, basket)
        # print(server_harame_2.encode('hex'))
        server_harame_3 = "17cfef08"
        server_harame_3 = "17d978cb"


        # ball = "000000000000"

        data = {
            "key":key,
            "harame":harame,
            "coach":coach,
            "jersey":jersey,
            "ball":ball
        }

        r = post(url, data=data)
        print("Response: {}".format(r.text))
        
        break
        
        # if "A hint:" in r.text:
        #     hints.append(r.text[r.text.find('A hint:') + 7:-1])
    
        # if len(hints) > 100:
        #     break

    for hint in hints:
        print(hint)



import zlib
import gzip
from crccheck.crc import Crc32Bzip2
from crccheck.checksum import Checksum32
import array

def find_crc32_bz2():
    # print(dir(gzip.zlib.crc32))
    i = 0
    while True:
        if i % 10**5 == 0: print(i)
        
        data = list(array.array('B', str(i)))

        crc_bz2 = Crc32Bzip2.calc(data)
        # crc_bz2 = Checksum32.calc(data)
        print("Checksum of {} is : {}".format(i, crc_bz2))
        # type(crc_bz2)
        # crc_bz2 = zlib.crc32(str(i))
        # print(crc_bz2)
        # crc_bz2 = gzip.zlib.crc32(str(i))
        # print(crc_bz2)

        if crc_bz2 == 0:
            print("Checksum of {} is : {}".format(i, crc_bz2))
            break
        i += 14

if __name__ == '__main__':
    # php = """zohwncih r0l($mnlcha, $guacw_eys) { #bnnjm://mnuweipylzfiq.wig/koymncihm/14673551/yhwlsjn-xywlsjn-qcnb-ril-ch-jbj } $zfua = "UleWih{?}"; $fcmn = ullus('wlw32', 'gx5', 'mbu1'); $ufai = $fcmn[ullus_luhx($fcmn)]; cz (!ygjns($_JIMN['eys']) || !ygjns($_JIMN['bulugy'])){ $vumeyn = bumb($ufai, r0l($zfua, $_JIMN['eys'])); $bulugy = bumb($ufai, mnllyp($_JIMN['bulugy'])); } yfmy{ ywbi ("Jfyumy wfimyx nby xiil vybchx sio\h"); yrcn; } $wixy = "20190429_71070_y7707_1312_3_14159265359"; cz (!ygjns($_JIMN['wiuwb']) || !ygjns($_JIMN['dylmys'])) $vumeyn = mnl_lyjfuwy("_", $_JIMN['wiuwb'], movmnl($wixy, $_JIMN['dylmys']).movmnl($wixy, 0, $_JIMN['dylmys'])); ywbi ("BULUGY!\h"); $vuff = bumb('gx5', $vumeyn); cz (cmmyn($_JIMN['vuff']) && cmmyn($_JIMN['dylmys']) ){ $vuff = movmnl(r0l(juwe("B*", $_JIMN['vuff']), $vuff), -8) * $_JIMN['dylmys']; $bulugy = bumb($ufai, r0l($bulugy, $vumeyn)); } cz( $vumeyn != bumb($ufai, $vuff)) yrcn; $eys = bumb($ufai, $bulugy); ywbi ("U bchn:" . mnl_mbozzfy($eys . $zfua) . "\h"); cz ($eys == $_JIMN['eys']) ywbi ("Sio uly nby AIUN: " . $zfua); yrcn;"""    
    # print(decode_php(php))

    apost()

    # print(calc_harame_1("harame"))
    # print(calc_basket('a', 2))

    # print(hashlib.md5('\x00').hexdigest())
    
    # print(xor("aaaaaaaaaaaaa", "abcabcabc"))

    # find_crc32_bz2()

