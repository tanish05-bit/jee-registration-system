#(hash_pw) takes a plain password, encodes it to bytes (.encode()), runs it through SHA-256, and returns the hash as a hex string. 
# This is what gets stored in the DB — never the raw password.
#check_pw: to verify a login, you can't "decrypt" a hash, so instead you hash the password the user just typed and compare it to what's stored.
# If they match, it's the right password.
import hashlib
def hash_pw(pw):
    return hashlib.sha256(pw.encode()).hexdigest()
def check_pw(pw, hashed):
    return hash_pw(pw)==hashed
