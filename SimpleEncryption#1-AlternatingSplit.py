# For building the encrypted string:
# Take every 2nd char from the string, then the other chars, 
# that are not every 2nd char, and concat them as new String.
# Do this n times!

# Examples:

# "This is a test!", 1 -> "hsi  etTi sats!"
# "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"

# Write two methods:

# def encrypt(text, n)
# def decrypt(encrypted_text, n)

# For both methods:
# If the input-string is null or empty return exactly this 
# value!
# If n is <= 0 then return the input text.

# This kata is part of the Simple Encryption Series:
# Simple Encryption #1 - Alternating Split
# Simple Encryption #2 - Index-Difference
# Simple Encryption #3 - Turn The Bits Around
# Simple Encryption #4 - Qwerty


def encrypt(text, n):

    if n >= 1:
        for i in range(n):

            text = list(text)
            even = []
            odd = []

            for i in range(len(text)):
                if (i % 2) == 0:
                    even.append(text[i])
                else:
                    odd.append(text[i])
            
            text.clear()

            text.extend(odd)
            text.extend(even)

            text = "".join(text)


    return text


def decrypt(encrypted_text, n):

    if n >= 1:
        for i in range(n):
            encrypted_text = list(encrypted_text)

            even = encrypted_text[:len(encrypted_text)//2]
            odd = encrypted_text[len(encrypted_text)//2:]
            countOdd = 0
            countEven = 0

            decrypted_text = []

            for i in range(1, len(encrypted_text)+1):
                if (i % 2) == 0:
                    decrypted_text.append(even[countEven])
                    countEven += 1
                else:
                    decrypted_text.append(odd[countOdd])
                    countOdd += 1
            
            encrypted_text = "".join(decrypted_text)
    

    return encrypted_text



    


print(encrypt("This is a test!", 0))
print("")
print("")
print(decrypt("s eT ashi tist!", 2))
