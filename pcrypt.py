
def encode_string( origin_message, crypt_key):
    i2 = 0
    encoded_string = ""

    for i in range(len( origin_message )):
    
        c = ord(origin_message[i]) + ord(crypt_key[i2]) - 97 

        if c > ord('z'): c = c- 26

        encoded_string = encoded_string + chr(c)

        if i2 == (len( crypt_key ) - 1):
            i2 = 0
        else:
            i2 = i2 + 1

    return encoded_string


crypt_key = str(input("Please input crypt key phrase: "))
# print( crypt_key )

origin_message = str(input("Please input message: "))
# print( origin_message )


print("crypted message: ", encode_string( origin_message, crypt_key))

