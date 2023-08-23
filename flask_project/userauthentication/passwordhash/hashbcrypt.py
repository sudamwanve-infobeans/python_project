from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

hashed_pass = bcrypt.generate_password_hash('sudam@123')
print(hashed_pass)
wrong_check = bcrypt.check_password_hash(hashed_pass, 'sudam@321')
print(wrong_check)
right_check = bcrypt.check_password_hash(hashed_pass, 'sudam@123')
print(right_check)

"""
Output :
b'$2b$12$2EUA1T2FEPuA6LU1SrD..enkPO3qv2zEv3TAJkKNHETRjsZwCrvTq'
False
True
"""
