alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # alphabet set

def encrypt(message, key):
    message = message.lower()           # make the message lowercase
    key = key.lower()                   # make the key lowercase
    code = ''

    if len(message) > len(key):
        # make the key the same length as the message
        repeat = (len(message) // len(key)) + 1
        key = key * repeat
        key = key[:len(message)]
    elif len(message) < len(key) or len(message) == len(key):
        # truncate the key to match the length of the message
        key = key[:len(message)]

    # the encryption algorithm
    #
    # Ca = Ma + Kb (mod 26)
    #
    # where C = Code, M = Message, K = Key, and where a = the ath character
    # of the message bounded by the message, and b is the bth character of
    # the key bounded by the length of the key
    for i, item in enumerate(message):
        tmp = (ord(item) - 97) + ((ord(key[i]) - 96) % 26)
        if tmp > 26:
            tmp -= 26
        code = code + alphabet[tmp-1]

    return code

def decrypt(code, key):
    code = code.lower()                 # make the code lowercase
    key = key.lower()                   # make the key lowercase
    message = ''

    if len(code) > len(key):
        # make the key the same length as the message
        repeat = (len(code) // len(key)) + 1
        key = key * repeat
        key = key[:len(code)]
    elif len(code) < len(key) or len(code) == len(key):
        # truncate the key to match the length of the message
        key = key[:len(code)]

    # the decryption algorithm
    #
    # Ma = Ca – Kb (mod 26)
    #
    # where C = Code, M = Message, K = Key, and where a = the ath character
    # of the message bounded by the message, and b is the bth character of
    # the key bounded by the length of the key
    for i, item in enumerate(code):
        tmp = 26 + (ord(item) - 95) - ((ord(key[i]) - 96) % 26)
        if tmp > 26:
            tmp -= 26
        message = message + alphabet[tmp-1]

    return message

def check(answer):
    n = input("Code/Message? ")
    k = input("Key? ")
    # remove all spaces
    n = "".join(n.split())
    k = "".join(k.split())
    # the strings only accept alphabets
    # no numbers or some shit please, for the love of god!! >_<
    if n.isalpha() and k.isalpha():
        if int(answer) == 1:
            result = encrypt(n, k)
        elif int(answer) == 2:
            result = decrypt(n, k)
    else:
        result = 'ERROR'
    print(result)

def main():
    print('Select one:')
    print('(1) Encrypt')
    print('(2) Decrypt')
    inp = input('> ')
    answer = inp
    check(answer)

if __name__ == "__main__":
    main()
