import hashlib

target_hash = "40be4e59b9a2a2b5dffb918c0e86b3d7"

wordlist = [
    "cipher@2026",
    "password",
    "123456",
    "@123john",
    "admin",
    "letmein",
    "astra@2025",
    "welcome",
    "jack@123"
]

for word in wordlist:
    hashed = hashlib.md5(word.encode()).hexdigest()
    if hashed == target_hash:
        print("Password found:", word)
