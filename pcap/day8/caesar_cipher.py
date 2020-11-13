class CaesarCipher:
    """A caesar cipher encoder.

    This cipher was (probably) invented and used by Julius Caesar and his
    troops during the Gallic Wars. The idea is rather simple - every letter
    of the message is replaced by its nearest consequent (A becomes B, B
    becomes C, and so on). The only exception is Z, which becomes A.

    This concept can be extended to shift each letter any number of places.

    See: https://en.wikipedia.org/wiki/Caesar_cipher
    """

    def __init__(self, shift: int = 1):
        """Initialize a CaesarCipher with a given shift.

        Parameters
        ----------
        - shift : int, optional
            - How many places to shift each letter by, by default 1
        """
        self.shift = abs(shift)

    def encrypt(self, message: str) -> str:
        """Encrypt a message using the caesar cipher algorithm.

        Punctuation and capitalization are preserved.

        Example
        -------
            >>> cipher = CaesarCipher(shift=1)
            >>> cipher.encrypt("Randy Henry")
            'Sboez Ifosz'

        Parameters
        ----------
        - message : str
            - The message to be encrypted.

        Returns
        -------
        - str
            - The encrypted form of the message.
        """

        # Rotate each character in the message, and join them into one string.
        return "".join(self._shift_one(char) for char in message)

    def _shift_one(self, char: str) -> str:
        """Shift one single character.

        The result wraps around, e.g. `"z" + 2` would become `"b"`.

        Uses `self.shift` to determine how many places to shift by.

        Example
        --------
            >>> cipher = CaesarCipher(shift=2)
            >>> cipher._shift_one("z")
            'b'
            >>> lst = [cipher._shift_one(c) for c in "Randy Henry"]
            >>> ''.join(lst)
            'Tcpfa Jgpta'

        Parameters
        ----------
        - char : str
            - The character to rotate.
            Must be length 1.

        Returns
        -------
        - str
            - The rotated character.
        """
        if not char.isalpha():  # if the char isn't in the alphabet
            return char  # leave it as-is

        offset = ord("a" if char.islower() else "A")  # index of first letter
        code = ord(char)  # get the number that represents the char
        code -= offset  # find how many letters away from 'a' it is
        code += self.shift  # get the letter after it
        code %= 26  # if over 25 letters away, wrap around from the beginning
        code += offset  # change back from an offset into the actual letter
        return chr(code)  # return letter as a string

    def decrypt(self, message: str) -> str:
        """Decrypt an already encrypted message.

        This is the inverse of `encrypt`.

        Trying to decrypt an unencrypted message
        or a message encoded with a different shift will produce nonsense.

        Example
        -------
            >>> cipher = CaesarCipher(shift=1)
            >>> cipher.encrypt("Randy Henry")
            'Sboez Ifosz'
            >>> cipher.decrypt(cipher.encrypt("Randy Henry"))
            'Randy Henry'

        Parameters
        ----------
        - message : str
            - The message to decrypt.
            It's assumed that the message has already been encrypted.

        Returns
        -------
        - str
            - The original, unencrypted form of the message.
        """

        # Encrypting with a negative shift is the same as decrypting.  We
        # temporarily make the shift negative, "encrypt", then switch it back.
        self.shift = -self.shift
        result = self.encrypt(message)
        self.shift = -self.shift
        return result
