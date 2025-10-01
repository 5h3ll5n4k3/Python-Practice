from passlib.hash import md5_crypt

password = "coldplay1995"

# Generate the hash using md5-crypt
hashed_password = md5_crypt.hash(password)

print(hashed_password)
