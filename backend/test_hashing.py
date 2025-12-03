from werkzeug.security import generate_password_hash, check_password_hash

password = 'admin123'
print(f"Testing password: {password}")

# Test Default (scrypt)
try:
    hash_default = generate_password_hash(password)
    print(f"Default Hash: {hash_default}")
    is_valid = check_password_hash(hash_default, password)
    print(f"Default Check: {is_valid}")
except Exception as e:
    print(f"Default Error: {e}")

# Test pbkdf2:sha256
try:
    hash_sha256 = generate_password_hash(password, method='pbkdf2:sha256')
    print(f"SHA256 Hash: {hash_sha256}")
    is_valid_sha256 = check_password_hash(hash_sha256, password)
    print(f"SHA256 Check: {is_valid_sha256}")
except Exception as e:
    print(f"SHA256 Error: {e}")
