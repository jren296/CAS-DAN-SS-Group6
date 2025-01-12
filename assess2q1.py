# assessment 2 Q1
# program to encrypt and decrypt text from a file
# developed by CAS/DAN Group 6
def encrypt_text(input_text, output_text, n, m):
    with open(input_text, 'r') as infile:
        text = infile.read()
    encrypted_text = ''    
       
    for char in text:            # go through each character and encrypt to specifications
        if ord(char) in range(97,110):      # lower case a-m 
            encrypted_text += chr((ord(char) + n*m - 97)% 13 + 97)  # use modulus % 13 to ensure encrypted characters stay in the same range for decryption
        elif ord(char) in range(110, 123):  # lower case n-z
            encrypted_text += chr(((ord(char) - (n + m)) - 97)% 13 + 110)
        elif ord(char) in range(65, 78):    # upper case A-M
            encrypted_text += chr((ord(char) - n - 65)% 13 + 65)
        elif ord(char) in range(78, 91):    # upper case N-Z 
            encrypted_text += chr((ord(char) + m**2 - 65)% 13 + 78)
        else:
            encrypted_text += char          # special characters not encrypted
    with open(output_text, 'w') as outfile:
        outfile.write(encrypted_text)         # write encrypted text to file
 
def decrypt_text(input_text, output_text, n, m):
    with open(input_text, 'r') as infile:
        encrypted_text = infile.read()         # read encrypted text file
 
    decrypted_text = ''
    for char in encrypted_text:                # reverse charactor encryption
        if ((ord(char))) in range(97, 110):    # lower case a-m
            decrypted_text += chr((ord(char) - n*m - 97)% 13 + 97)
        elif ((ord(char))) in range(110, 123): # lower case n-z
            decrypted_text += chr(((ord(char) + (n + m)) - 97)% 13 + 110)
        elif (ord(char)) in range(65, 78):     # upper case A-M
            decrypted_text += chr((ord(char) + n - 65)% 13 + 65)
        elif (ord(char)) in range(78, 91):     # upper case N-Z
            decrypted_text += chr((ord(char) - m**2 - 65)% 13 + 78)
        else:
            decrypted_text += char             # special characters no decryption needed
 
    with open(output_text, 'w') as outfile:
        outfile.write(decrypted_text)              # write decrypted text to a file
 
def check_decryption(original_file, decrypted_file):
   
    # Check if the decrypted text matches the original text.
   
    with open(original_file, 'r') as orig_file:
        original_text = orig_file.read()
    with open(decrypted_file, 'r') as decr_file:
        decrypted_text = decr_file.read()
 
    return original_text == decrypted_text
 
def main():
    n = int(input('Enter an integer "n" for encryption key: '))   # enter values for encryption key
    m = int(input('Enter an integer "m" for encryption key: '))
 
    input_text = 'raw_text.txt'
    encrypted_text = 'encrypted_text.txt'
    decrypted_text = 'decrypted_text.txt'
    encrypt_text(input_text, encrypted_text, n, m)
    print('Encryption complete. Encrypted text saved to "encrypted_text.txt"')
 
    decrypt_text(encrypted_text, decrypted_text, n, m)
    print('Decryption complete. Decrypted text saved to "decrypted_text.txt"')
 
    if check_decryption(input_text, decrypted_text):
        print("Decryption is correct")
    else:
        print("Decryption failed.")
main() 
# encrypt_text('raw_text.txt', 'encrypted_text.txt', 2, 2)
# decrypt_text('encrypted_text.txt', 'decrypted_text.txt', 2, 2)
