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
    max_c = ''

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
            max_c = c

    return max_c, max_count

    nc.close()

def main() :
    prefix = "TWCTF{67ced5346146c105075443add26fd7efd72763d"

    count = 0
    
    while True :
        c, max_count = test_for_100_time(prefix)

        if max_count > count :
            prefix += c
            count = max_count

        print(count, prefix)

        if len(prefix.replace('0', '')) == 47 :
            print(prefix)
            break

    return 0

if __name__ == '__main__' :
    main()
