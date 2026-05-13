import itertools, time

def guess_password(password,chars):
    found=False
    start = time.time()

    attempts = 0
    for password_length in range(1, 9):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
              found = True
              end = time.time()
              duration = end - start
              return f'password is {guess} found in {attempts} attempts in {duration} seconds'
            #print(guess)
    if found is False:
      return "Password not found"
