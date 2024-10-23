from cipher import Cipher

class Caesar(Cipher):
    """
        Attributes:
            shift (int): the number of positions to shift letters for encryption
    """
    def __init__(self, shift):
        # passes in caesar chiper's shif value.
        # Call super to initialize the alphabet, then set the shift value.
        super().__init__()
        self.shift = shift

    def _encrypted_letter(self, letter):
        # Look up the letter in the alphabet to find the location
        if letter in self.alph:
            # Use the location to calculate the position of the encrypted letter
            position = self.alph.index(letter)
            encrypted_position = (position + self.shift) % 26
            return self.alph[encrypted_position]
        
        # Return the encrypted letter
        return letter

    def _decrypted_letter(self, letter):
        # Look up the letter in alphabet to find its location
        if letter in self.alph:
            # Use the location to calculate the position of the decrypted letter
            position = self.alph.index(letter)
            decrypted_position = (position - self.shift + 26) % 26
            return self.alph[decrypted_position]
        
        # Return the decrypted letter
        return ord(letter)
