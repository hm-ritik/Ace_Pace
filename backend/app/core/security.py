from pwdlib import PasswordHash

context = PasswordHash.recommended()


def hash_password(password:str):
    return context.hash(password)

def verify_password(password:str , hashed_password):
    return context.verify(password , hashed_password)
