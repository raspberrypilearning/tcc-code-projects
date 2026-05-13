import string
from passwordmatch import guess_password

#ascii letters and digitals
alpha = chars = string.ascii_letters + string.digits

#ascii letters, digits, special characters and whitespace
extended = string.ascii_letters + string.digits + string.punctuation + string.whitespace

#password to check
password = "ab"


#call function and print return value
print(guess_password(password,alpha))