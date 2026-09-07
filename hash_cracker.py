import hashlib
import sys

def input_func():

    wordlist = sys.argv[1]
     
    hash_val = input("Hash to Solve:")
    hash_type = input("Hash Type of Hash:")

    with open(wordlist, 'r') as f:
        line = f.readline()
        for line in f:
            clear_line = line.rstrip('\n')
            text_to_hash(clear_line, hash_type, hash_val)
        f.close()


def text_to_hash(plaintext, hash_type, hash_input):

    #UTF-8 because it supports every type of input
    #encode func is for encoding txt -> bytes.
    #bytes because hashes work with bytes.
    try:
        byte = plaintext.encode('utf-8')
        hash_method = getattr(hashlib, hash_type.lower())
        hash_val = hash_method(byte).hexdigest()

        if hash_input == hash_val:
            print(f"Match Found: {plaintext} - {hash_val}")

    except (AttributeError, TypeError):
        print(f"'{hash_type}' is not a valid algorithm.")


if __name__ == '__main__':
    input_func()
