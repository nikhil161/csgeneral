import math

def main():
    message =  "Common sense is not so common."
    key = 8

    ciphertext = encrypt(message, key)
    print ciphertext
    plaintext = decrypt(ciphertext, key)
    print plaintext

def encrypt(m, k):
    ciphertext = ''
    for i in range(k):
        ciphertext += m[i::k]

    return ciphertext

def decrypt(m, k):
    k2 = int( math.ceil( float(len(m)) / k))
    print k2
    plaintext = ''

    f = k - (len(m) % k)
    print f 

    for i in range(k2):
        j = i
        while j < len(m):
            plaintext += m[j]
            if len(plaintext) >= len(m):
                break
            if (j / k2) >= f:
                print (j % k), f
                j += k2 - 1
            else:
                j += k2
                


    return plaintext

if __name__ == "__main__":
    main()
