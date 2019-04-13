import itertools

import subprocess
import os

if __name__ == "__main__":
    flag = "{}{}{}"
    flag = "33333333{}"

    i = 0
    a_chars = "23579A"
    b_chars = "3467BC"
    c_chars = "123589a"

    # for a in itertools.product(a_chars, repeat=4):
    #     a = "".join(a)
    #     for b in itertools.product(b_chars, repeat=4):
    #         b = "".join(b)
    for c in itertools.product(c_chars, repeat=4):
        c = "".join(c)
        
        i += 1
        if i % 1000 == 0: print("Iteration: {}".format(i))

        test_flag = flag.format(c)
        # print(test_flag)

        output = subprocess.Popen(["Puzzle.exe", test_flag], stdout=subprocess.PIPE).communicate()[0]

        if "Good job!" in output:
            print(test_flag)
            exit()
