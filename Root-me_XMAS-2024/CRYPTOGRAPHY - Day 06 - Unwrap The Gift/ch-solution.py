from pwn import *
import binascii

URL = "163.172.68.42"
PORT = 10006
r = remote(URL, PORT)

def decrypt_ctr(enc_flag, enc_ret, clear_text):
    # Ciphertext1 = Flag XOR AES(Key, IV) 
    # Ciphertext2 = Input XOR AES(Key, IV) 
    # => Flag XOR Ciphertext1 = Input XOR Ciphertext2
    # => Flag = Input XOR Ciphertext1 XOR Ciphertext2
    return bytes([a ^ b ^ c for a, b, c in zip(enc_flag, enc_ret, clear_text)])

full_text_flag = r.recvuntil("Y/N)\n")
print(full_text_flag)
# --------------------------------------------------
#   .-""-.
#  /,..___\
# () {_____}
#   (/-@-@-\)
#   {`-=^=-'}
#   {  `-'  } Oh Oh Oh! Merry Root-Xmas to you!
#    {     }
#     `---'
# --------------------------------------------------
# [SANTA]: Hello player, welcome! Here is your gift for this christmas: b913951862d00c918fb014cd6f57117f1951901b5c6b0c9deccae92d4a2c6609d147ed74aadb422d83d5b267eb52a21724e4ac1bf9ecc5e1e5eb4706fb8269f8
# [SANTA]: Oh, I forgot to tell you, you will only be able to unwrap it on the 25th, come back to me on that date to get the key!
# --------------------------------------------------
# [SANTA]: While I\'m at it, do you wish to wrap a present for someone? (Y/N)'

enc_flag = binascii.unhexlify(full_text_flag.split(b'christmas: ')[1].split(b'\n')[0])

# Send Y to send a clear text
r.sendline("Y")

tmp_message = r.recv()
print(tmp_message)
# [SANTA]: Enter the message you wish to wrap:

send_input = b'a'* len(enc_flag)

r.sendline('{}'.format(send_input.decode()))

full_text_ret = r.recv()
print(full_text_ret)
# [SANTA]: Here is your wrapped present: e59d73b4360f232e08ee25fe66eb5a59e8d12f528649fbfd61e0653b099170b9784716792ab1e51d877ead7be1e2a21976e6cf6d4341209852e6ed31353998f4f8071bdd7db045999f1e4b74a1f66ba7
# [SANTA]: Merry Christmas!

enc_ret = binascii.unhexlify(full_text_ret.split(b'present: ')[1].split(b'\n')[0])

flag = decrypt_ctr(enc_flag, enc_ret, send_input)

print(flag)
# RM{D0NT_WR4P_YOUR_GIFTS_W1TH_W3AK_CRYPTOGRAPHY:(}\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f\x0f

r.close()