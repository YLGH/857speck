import speck
#   import the distinguish function and B and r paramaters
#   B: number of 16-byte blocks to generate
#   r: number of Speck rounds
from distinguish import distinguish, B, r
import os
from struct import pack, unpack

"""
    `distinguish` should take a list of `B` 16-byte ciphertext blocks as
    a parameter and return `0` if it determines the bytes are output of Speck
    or `1` if the bytes are random.
"""

def challenge_distinguisher():
    coin = ord(os.urandom(1)[0]) % 2
    ctxt_blocks = []
    if coin == 0:
        #   Speck bytes (CTR mode)
        K = os.urandom(16)
        for i in range(B):
            pt = pack("<Q", i) + "\x00" * 8
            ctxt_blocks.append(speck.encrypt(pt, K, r))
    else:
        #   random bytes
        for i in range(B):
            ctxt_blocks.append(os.urandom(16))
    if distinguish(ctxt_blocks) == coin:
        return True
    return False

if __name__ == "__main__":
    print "Testing distinguisher for " + str(B) + " blocks of " + str(r) + "-round Speck"
    trials = 20
    correct = 0
    for i in range(trials):
        if challenge_distinguisher():
            correct += 1
    print "Number of correct guesses: " + str(correct) + " out of " + str(trials)
