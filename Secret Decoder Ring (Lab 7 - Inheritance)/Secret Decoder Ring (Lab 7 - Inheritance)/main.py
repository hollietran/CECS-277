from cipher import Cipher
from caesar import Caesar 
import check_input

def main():
  """Have the user choose to encrypt or decrypt a message, then have them choose
an encryption/decryption method (Atbash or Caesar cipher). If they choose to encrypt, then
prompt them to enter a message to encrypt, then write the encrypted message to the file
‘message.txt’. If they choose to decrypt a message, read the message from the file ‘message.txt’
and then display the decrypted message to the console. If they choose to use a Caesar Cipher for
either encryption or decryption, then prompt the user to enter a shift value (0-25)"""
  while True:
    print('Secret Decoder Ring:')
    print('1. Encrypt')
    print('2. Decrypt')
    action=check_input.get_int_range('Enter choice: ',1,2)
  
    if action==1:
      #encrypt
      print('Enter encryption type:')
      print('1. Atbash\n2. Caesar')
      cipher_type=check_input.get_int_range('Enter choice: ',1,2)
  
      if cipher_type == 2:
      #caeser
        message = input('Enter message: ')
        shift = check_input.get_int_range('Enter shift value: ',0,25)
        cipher = Caesar(shift)
        encrypted_message = cipher.encrypt_message(message)
        with open('message.txt', 'w') as f:
          f.write(encrypted_message) #write to file
        print('Encrypted message saved to “message.txt”.')

      if cipher_type==1:
        #atbash
        message = input('Enter message: ')
        cipher = Cipher()
        encrypted_message = cipher.encrypt_message(message)
        with open('message.txt', 'w') as f:
          f.write(encrypted_message) #write to file
        print('Encrypted message saved to “message.txt”.')
  
    elif action==2:
      #decrypt
      print('Enter encryption type:\n1. Atbash\n2. Caesar')
      cipher_type=check_input.get_int_range('Enter choice: ',1,2)
  
      if cipher_type==2:
        #caesar cipher
        shift = check_input.get_int_range('Enter shift value: ',0,25)
        print('Reading encrypted message from “message.txt".')
        with open("message.txt",'r') as f:
          encrypted_message = f.read()
        cipher = Caesar(shift)
        decrypted_message = cipher.decrypt_message(encrypted_message)
        print("Decryted message: " + decrypted_message)

      if cipher_type==1:
        #atbash cipher
        print('Reading encrypted message from “message.txt".')
        with open("message.txt",'r') as f:
          encrypted_message = f.read()
        cipher = Cipher()
        decrypted_message = cipher.decrypt_message(encrypted_message)
        print("Decryted message: " + decrypted_message)

main()