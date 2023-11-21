import hashlib

# Create a string to hash
input_string = "Hello, World!"

# Create a SHA-256 hash object
sha256_hash = hashlib.sha512()

# Update the hash object with the input string (UTF-8 encoded)
sha256_hash.update(input_string.encode('utf-8'))

# Get the hexadecimal representation of the digest
digest = sha256_hash.hexdigest()

print("SHA-256 Digest:", digest)
