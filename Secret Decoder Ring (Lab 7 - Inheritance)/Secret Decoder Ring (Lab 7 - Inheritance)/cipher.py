class Cipher:
    """
    Attributes:
        alph (str): the alphabet
        shift (int): the number of positions to shift letters for encryption
        ...
    """

    def __init__(self):
        # Initialize the alphabet attribute
        # Make a list with the letters A-Z in it
        self.alph = [chr(i) for i in range(65,91)]
    
    def encrypt_message(self, message):
        # Convert the message to upper case letters
        message = message.upper()
        encrypted_message = ""

        # Loop through the string one character at a time
        for char in message:
            # If letter is A-Z, call the encrypt_letter method, otherwise ignore
            if char in self.alph:
                encrypted_message += self._encrypt_letter(char)
            else:
                encrypted_message += char

        # Return the encryption string using encrypt_letters and ignored characters
        return encrypted_message
    
    def decrypt_message(self, message):
        # Convery the message to upper case
        message = message.upper()
        decrypted_message = ""
        # Loop through the mesage string one character at a time.
        for char in message:
            if char in self.alph:
                decrypted_message += self._decrypted_letter(char)
            else:
                decrypted_message += char

        # Build the decryption string using the decrypted letters in a manner similar to the encrypt_message method above
        return decrypted_message
    
    def _encrypt_letter(self, letter):
        # look up the letter in the alphabet to find the location.
        position = self.alph.index(letter)
        # Use location to calculate the position of the encrypted letter
        encrypted_position = (position + 25) % 26

        # Return encrypted letter
        return self.alph[encrypted_position]

    def _decrypted_letter(self, letter):
        # look up the letter in the alphabet to find the location.
        position = self.alph.index(letter)
        # Use location to calculate the position of the decrypted letter
        decrypted_position = (position - 25) % 26
    
        # Return the decrypted letter
        return self.alph[decrypted_position]