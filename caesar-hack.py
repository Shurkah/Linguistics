def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    

def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


def getCipherKey():
    shiftAmount = input('Please enter a key number (1 < integer < 26): ')
    return shiftAmount
    

def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ''
    uppercaseMessage = message.upper()
    for char in uppercaseMessage:
        pos = alphabet.find(char)
        newpos = pos + int(cipherKey)
        if char in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newpos]
        else:
            encryptedMessage = encryptedMessage + char
    return encryptedMessage
    
    
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)
    

def runCaesarHacker(key):
    englishAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(f'Using alphabet: {englishAlphabet}')
    alphabet = getDoubleAlphabet(englishAlphabet)
    message = messageToHack
    decryptKey = key
    decryption = decryptMessage(message, decryptKey, alphabet)
    print(f'{key}: {decryption} \n')


messageToHack = input('Please provide a message to hack: ')
for i in range(1, 26):
    runCaesarHacker(i)
    i += 1