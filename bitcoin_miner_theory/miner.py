from hashlib import sha256
MAX_NONCE = 42330

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
    if new_hash.startswith(prefix_str):
        print(f"You have successfully mined bitcoin with nonce valued {nonce} !!!")
        return new_hash


        raise BaseException(f"Could not find the correct hash after trying {MAX_NONCE} times !!!")
    


if __name__=='__main__':
    transactions='''
    Miggy -> Monica -> 20, 
    Raven -> Ash -> 30
    '''

    difficulty=6
    import time 
    #Measuring time to take how much time would it take to mine a bitcoin
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'0000000212wx002420',difficulty)
    total_time = str((time.time() - start))
    print(f"End mining. The mining process took: {total_time} seconds")
    print(new_hash)
