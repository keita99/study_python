def decode_string( crypt_message, crypt_key):
    i2 = 0
    decoded_string = ""

    for i in range(len( crypt_message )):
    
        c = ord(crypt_message[i]) - ord(crypt_key[i2]) + ord('a')

        if c < ord('a'): c = c + 26
#        print(c)
        decoded_string = decoded_string + chr(c)

        if i2 == (len( crypt_key ) - 1):
            i2 = 0
        else:
            i2 += 1

    return decoded_string


crypt_key = str(input("Please input crypt key phrase: "))
# print( crypt_key )

crypt_message = str(input("Please input crypt message: "))
# print( origin_message )


print("original message: ", decode_string( crypt_message, crypt_key))
