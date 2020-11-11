import os

key = os.urandom(24)
#key = os.urandom(24).hex()

if __name__ == '__main__':
    print(key)