import re
import string
import sys
import netcat


def count_matching(enc_flag, param):
    counter = 0
    for i in range(len(param)):
        if enc_flag[i] == param[i]:
            counter += 1
        else:
            return counter
    return counter


def find_max_for_prefix(flag_len, flag_prefix, port, url):
    s = netcat.Netcat(url, port)
    initial = s.read_until( "message: ")
    enc_flag = re.findall("encrypted flag: (.*)", initial)[0]
    print(initial)
    max_score = 0
    maxes = []
    for c in string.digits + "abcdef":  # charset
        data = flag_prefix + c + ('0' * (flag_len - len(flag_prefix) - 2)) + '}'
        s.write(data)
        result = s.read_until("ciphertext: .*\n")
        result = re.findall("ciphertext: (.*)\n", result)[0]
        matched = count_matching(enc_flag, result)
        print(matched, flag_prefix + c)
        if matched == len(enc_flag):
            print("Found", data)
            sys.exit(0)
        if matched > max_score:
            max_score = matched
            maxes = [c]
        elif matched == max_score:
            maxes.append(c)
        elif matched < max_score:
            break  # won't get better anymore
        s.read_until("message:")
    s.close()
    return max_score, maxes


def main():
    flag_len = 47
    flag_prefix = "TWCTF"
    maxes = ['{']
    current_score = 8
    url = "crypto.chal.ctf.westerns.tokyo"
    port = 14791
    while True:
        for c in maxes:
            flag_prefix_test = flag_prefix + c
            max_score, new_maxes = find_max_for_prefix(flag_len, flag_prefix_test, port, url)
            if (max_score > current_score) or ((max_score == current_score) and len(new_maxes) < 16):
                current_score = max_score
                maxes = new_maxes
                flag_prefix += c
                print(flag_prefix)
                break


if __name__ == '__main__' :
    main()
