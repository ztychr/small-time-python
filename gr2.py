import time
import random
import os

os.system('color 9') #lyseblå

cases = [

#one = 0.25
"""
      5
      |
      4          *             *
      |
      3       *     *     *
      |
      2  *                *
      |
      1    *     *
      |
-----------1-----2-----3-----4-----5
      |
      |
""",

#two = 0.2
"""
      5  *
      |    *
      4  *       *  *
      |
      3                   *
      |                            *
      2          *        *
      |             *
      1
      |                         *
-----------1-----2-----3-----4-----5
      |
      |
""",

#three = 0.77
"""
      5
      |                   *  *
      4             *
      |          *
      3       *     *  *
      |
      2    *     *
      |  *
      1
      |  *
-----------1-----2-----3-----4-----5
      |
      |
""",

#four = 0.39
"""
      5
      |             *
      4                         *
      |          *     *  *
      3
      |          *        *
      2       *     *
      |
      1             *
      |  *
-----------1-----2-----3-----4-----5
      |
      |
""",

#five = 0.86
"""
      5
      |             *  *
      4                *
      |                *  *
      3                   *
      |                      *
      2                     * *
      |                      *  *
      1                      *
      |                            *
-----------1-----2-----3-----4-----5
      |
      |
""",

#six = 0.03
"""
      5
      |
      4                *
      |                *  *
      3                   *
      |                      *
      2                     * *
      |  *                   *  *
      1                      *
      |  *                         *
-----------1-----2-----3-----4-----5
      |
      |
"""]

print("Welcome to GR^2")

def play():
    sp = (random.choice(cases))
    print(sp)
    if sp == cases[0]:
        sv = input("What is the correlation?\n")
        if sv == "20" or "21" or "22" or "23" or "24" or "25" or "26" or "27" or "28" or "29" or "30":
            print("It is 0.25")
            play()
        else:
            print("It is 0.25")
            play()
    elif sp == cases[1]:
        sv1 = input("What is the correlation?\n")
        if sv1 == ["15" or "16" or "17" or "18" or "19" or "20" or "21" or "22" or "23" or "24" or "25"]:
            print(print("It is 0.20"))
            play()
        else:
            print("It is 0.20")
            play()
    elif sp == cases[2]:
        sv2 = input("What is the correlation?\n")
        if sv2 == ["72" or "73" or "74" or "75" or "76" or "77" or "78" or "79" or "80" or "81" or "82"]:
            print(print("It is 0.77"))
            play()
        else:
            print("It is 0.77")
            play()
    elif sp == cases[3]:
        sv3 = input("What is the correlation?\n")
        if sv3 == ["34" or "35" or "36" or "37" or "38" or "39" or "40" or "41" or "42" or "43" or "44"]:
            print(print("It is 0.39"))
            play()
        else:
            print("It is 0.39")
            play()
    elif sp == cases[4]:
        sv4 = input("What is the correlation?\n")
        if sv4 == ["81" or "82" or "83" or "84" or "85" or "86" or "87" or "88" or "89" or "90" or "91"]:
            print(print("It is 0.86"))
            play()
        else:
            print("It is 0.86")
            play()
    elif sp == cases[5]:
        sv5 = input("What is the correlation?\n")
        if sv5 == ["1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10"]:
            print(print("It is 0.03"))
            play()
        else:
            print("It is 0.03")
            play()

play()
