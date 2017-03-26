"""
Speck128/128
https://en.wikipedia.org/wiki/Speck_(cipher)
"""

from struct import pack, unpack

uint64 = lambda x: x & ((1 << 64) - 1)
ROR = lambda x, r: (x >> r) | uint64(x << (64 - r))
ROL = lambda x, r: uint64(x << r) | (x >> (64 - r))

def R(x, y, k):
    x = ROR(x, 8)
    x = uint64(x + y)
    x = x ^ k
    y = ROL(y, 3)
    y = y ^ x
    return (x, y, k)

def encrypt(pt, K, r):
    y = unpack("<Q", pt[:8])[0]
    x = unpack("<Q", pt[8:])[0]
    b = unpack("<Q", K[:8])[0]
    a = unpack("<Q", K[8:])[0]
    x, y, b = R(x, y, b)
    for i in range(r - 1):
        a, b, i = R(a, b, i)
        x, y, b = R(x, y, b)
    return pack("<Q", y) + pack("<Q", x)
