def encrypt(text,n):
    result = ""
    for i in range(len(text)):
        char = text[i]

        if(char.isupper()):
            result += chr((ord(char) +n-65) % 26+65)
        
        else:
            result += chr((ord(char)+n-97) % 26 +97)

    return result

a = ""
#put the word to be encrypted in a
n = 3
print(encrypt(a,n)) 
