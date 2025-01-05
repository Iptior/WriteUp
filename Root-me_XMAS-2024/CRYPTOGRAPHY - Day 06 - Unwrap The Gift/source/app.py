from os import environ, urandom
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from binascii import hexlify

SANTA="""  .-""-.
 /,..___\\
() {_____}
  (/-@-@-\)
  {`-=^=-'}
  {  `-'  } Oh Oh Oh! Merry Root-Xmas to you!
   {     }
    `---'"""

FLAG = environ.get('FLAG', 'RM{REDACTED_FAKE_FLAG_DONT_SUBMIT}')

class Gift:
    """
    A custom class to wrap and unwrap gifts
    """
    def __init__(self):
        self.key = urandom(16)
        self.iv = urandom(12)
    
    def wrap(self, data):
        """
        Wrap the data with strong AES encryption
        """
        cipher = AES.new(self.key, 6, nonce=self.iv)
        data = data.encode()
        return hexlify(cipher.encrypt(pad(data, 16))).decode()
    
    def unwrap(self, data):
        """
        Unwrap the data
        """
        cipher = AES.new(self.key, 6, nonce=self.iv)
        return cipher.decrypt(bytes.fromhex(data)).decode()
    
def santa_says(message):
    print(f"[SANTA]: {message}")

if __name__ == '__main__':
    print("-"*50)
    print(SANTA)
    print("-"*50)

    gift = Gift()
    
    santa_says(f"Hello player, welcome! Here is your gift for this christmas: {gift.wrap(FLAG)}")
    santa_says("Oh, I forgot to tell you, you will only be able to unwrap it on the 25th, come back to me on that date to get the key!")
    print("-"*50)

    santa_says("While I'm at it, do you wish to wrap a present for someone? (Y/N)")
    ans = input().lower()
    if ans == 'y':
        santa_says("Enter the message you wish to wrap:")
        message = input()
        santa_says(f"Here is your wrapped present: {gift.wrap(message)}")
    else:
        santa_says("Alright, have a nice day!")
    santa_says("Merry Christmas!")
    exit(0)