import sys

def decrypt(str):
    """ Takes a string as input and decrement each character by it's index """
    res = ""
    cpt = 0
    for c in str:
        res = res + chr(ord(c) - cpt)
        cpt += 1
    return res

if __name__ == "__main__":
    result = decrypt(sys.argv[1])
    print(result)

