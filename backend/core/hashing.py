# Encrypt vs Hashing
# -> Enctypt is 2 ways implementation where a psw is encrypted then decrypted.
# -> Hashing is one way there can be only hashing no de-hasing.
# By using hashing we don't store any strings directly in DB rather the hash itself, which is compared with the entered Password(string) Hash to verify.

from pwdlib import PasswordHash

pwd_hash = PasswordHash.recommended()

class Hash():
    @staticmethod #To use methods this without creating obj's
    # To verify the hased passowrd with the user provided pwd
    def pwd_verify(user_pwd, pwd_hashed):
        return pwd_hash.verify(user_pwd, pwd_hashed)

    @staticmethod
    # To get the hash of user provided pwd
    def get_pwd_hash(user_pwd):
        pwd_hashed = pwd_hash.hash(user_pwd)
        return pwd_hashed