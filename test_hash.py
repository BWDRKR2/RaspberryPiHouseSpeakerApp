from werkzeug.security import generate_password_hash, check_password_hash

hash1 = generate_password_hash('Editors100')
hash2 = generate_password_hash('Editors100')
print hash1
print hash2


check_hash1 =  check_password_hash(hash1, 'Editors100')
check_hash2 =  check_password_hash(hash2, 'Editors100')


print check_hash1
print check_hash2
