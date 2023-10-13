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
    

def runCaesarCipher():
    englishAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print(f'Using alphabet: {englishAlphabet}')
    alphabet = getDoubleAlphabet(englishAlphabet)
    message = getMessage()
    print(f'The following message will be en-/decrypted: {message}')
    cipherKey = getCipherKey()
    print(f'Key: {cipherKey}')
    encryption = encryptMessage(message, cipherKey, alphabet)
    print(f'Encrypted message: {encryption}')
    decryption = decryptMessage(message, decryptKey, alphabet)
    print(f'Decrypted message: {decryption}')
    
    
runCaesarCipher()
