from werkzeug.security import generate_password_hash,check_password_hash

hashed_pass = generate_password_hash('sudam@123')
print(hashed_pass)
wrong_check = check_password_hash(hashed_pass,'sudam@321')
print(wrong_check)
right_check = check_password_hash(hashed_pass,'sudam@123')
print(right_check)

"""
pbkdf2:sha256:260000$PHbbeTpFkNAGdtga$769292127820efc2b10951d9d11400a61fe75fc5a9705b8f1d95541378a1e712
False
True

"""
