
def second_6_chars(out_of, fltr):
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # chars = "0123456789abcdefghijklmnopqrstuvwxyz"
    
    a = 0xCBF29CE484222325
    b = 0x5D929FF1619AC0C9
    c = 0x100000001B3

    i = 0
    c = 0
    for _1 in chars:
        for _2 in chars:
            for _3 in chars:
                for _4 in chars:
                    for _5 in chars:
                        for _6 in chars:
                            i += 1
                            if i % 1000000 == 0: print("{} - {}".format(i , c))
                            if i % out_of != fltr: continue
                            c += 1

                            guess = "{}{}{}{}{}{}".format(_1,_2,_3,_4,_5,_6)

                            checksum = a
                            for _ in guess:
                                checksum ^= ord(_)
                                checksum *= c
                                checksum &= 0xFFFFFFFFFFFFFFFF

                            if checksum == b:
                                print(guess)
                                return 

def first_4_chars():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789\{\}"
    
    a = 0xCBF29CE484222325
    b = 0x270163F106DBE9DD
    c = 0x100000001B3

    for _1 in chars:
        for _2 in chars:
            for _3 in chars:
                for _4 in chars:
                    guess = "{}{}{}{}".format(_1,_2,_3,_4)
                    checksum = a
                    for _ in guess:
                        checksum ^= ord(_)
                        checksum *= c
                        checksum &= 0xFFFFFFFFFFFFFFFF

                    if checksum == b:
                        print(guess)
                        return 


if __name__ == '__main__':
    # first_4_chars()

    from threading import Thread    
    num_of_threads = 4
    threads = []

    for i in range(num_of_threads):

        t = Thread(target=second_6_chars, args=(num_of_threads, i))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()