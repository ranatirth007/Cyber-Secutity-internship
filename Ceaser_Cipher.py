alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encryption(M,N):
    ct=""
    for char in m:
        if char in alphabet:
            Position=alphabet.index(char)
            N_P = (Position + N)%26
            ct+=alphabet[N_P]
        else:
            ct+=char
    print(f"Cipher text for your message is: {ct}")

def decryption(M,N):
    pt=""
    for char in m:
        if char in alphabet:
            Position=alphabet.index(char)
            N_P = (Position - N)%26
            pt+=alphabet[N_P]
        else:
            pt+=char
    print(f"Plain text for your Encrypted message is: {pt}")
    




w=input("Enter E for Encryption adn D for Decryption: ")
m=input("Enter your Message: ")
n=int(input("Enter shift Key: "))

if w=="e":
    encryption(M=m,N=n)
elif w=="d":
    decryption(M=m,N=n)