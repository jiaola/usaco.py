import sys

sys.stdin = open("digits.in", "r")
sys.stdout = open("digits.out", "w")


def convert_to_base_10(s, base):
    l = len(s)
    ret = 0
    for i in range(0, l):
        d = s[l-i-1]
        ret += int(d) * base ** i
    return ret


n1 = input()
n2 = input()


for i in range(0, len(n1)):
    s1 = list(n1)
    s1[i] = str((1 + int(n1[i])) % 2)
    x1 = convert_to_base_10(s1, 2)
    for j in range(0, len(n2)):
        s2 = list(n2)
        for k in range(1, 3):
            s2[j] = str((k + int(n2[j])) % 3)
            if x1 == convert_to_base_10(s2, 3):
                print(x1)
                sys.exit(0)

