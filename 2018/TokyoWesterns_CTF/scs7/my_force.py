from netcat import *
from time import sleep
import  re
import string

def count_matching(str1, str2) :
    count = 0
    for i in range(len(str1)) :
        if str1[i] != str2[i] : 
            break

        count +=1 

    return count

def test_for_100_time(prefix) :
    nc = Netcat('crypto.chal.ctf.westerns.tokyo', 14791)

    first = nc.read_until('message: ')
    enc_flag = re.findall("encrypted flag: (.*)", first)[0]

    # filter for pure enc string
    temp_string = ''
    for c in enc_flag :
        if c == "\\" : 
            break
        
        temp_string += c
    enc_flag = temp_string

    max_count = 0
    max_c = list()

    for c in string.digits + "abcdef" :
        data = prefix + c + ('0' * (47 - len(prefix) - 2)) + '}'
        
        print('trying: ' + data)

        nc.write(data + '\n')
        encryption_result = nc.read_until('message: ')
        enc_res = re.findall("ciphertext: (.*)", encryption_result)[0]

        # filter for pure enc string
        temp_string = ''
        for temp_c in enc_res :
            if temp_c == "\\"  : 
                break
            temp_string += temp_c
        enc_res = temp_string

        match_length = count_matching(enc_res, enc_flag)
        print(enc_res, enc_flag)

        if match_length > max_count :
            max_count = match_length
            max_c = [c]
        elif match_length == max_count :
            max_c.append(c)

    return max_c, max_count

    nc.close()

def main() :
    # prefix = "TWCTF{"

    # count = 0
    
    # while True :
    #     max_list, max_count = test_for_100_time(prefix)

    #     if max_count > count :
    #         prefix += c
    #         count = max_count

    #     print(count, prefix)

    #     if len(prefix.replace('0', '')) == 47 :
    #         print(prefix)
    #         break

    # return 0

    flag_len = 47
    flag_prefix = "TWCTF"
    maxes = ['{']
    current_score = 8
    url = "crypto.chal.ctf.westerns.tokyo"
    port = 14791
    while True:
        for c in maxes:
            flag_prefix_test = flag_prefix + c
            new_maxes, max_score = test_for_100_time(flag_prefix_test)
            if (max_score > current_score) or ((max_score == current_score) and len(new_maxes) < 16):
                current_score = max_score
                maxes = new_maxes
                flag_prefix += c
                print(flag_prefix)
                break


if __name__ == '__main__' :
    main()
