import random
from math import gcd
from sympy import isprime, primerange


def is_coprime(a, b):
    """ Check whether given numbers are co-prime """
    return gcd(a, b) == 1


def mod_inverse(e, phi):
    """ Modulo inverse using Extended Euclidean Algorithm """
    phi0 = phi
    y = 0
    x = 1

    if phi == 1:
        return 0

    while e > 1:
        qq = e // phi
        t = phi
        phi = e % phi
        e = t
        t = y
        y = x - qq * y
        x = t

    if x < 0:
        return x + phi0


def mod_inverse2(e, phi):
    """ Cleaner modulo inverse for python 3.8+ """
    return pow(e, -1, phi)


class RSA:
    def __init__(self):
        # generate two random primes from given range -- kind of a security regulator
        p_num, q_num = random.sample(list(primerange(200, 1000)), 2)
        self.public_e = None
        phi = (p_num - 1) * (q_num - 1)
        for x in range(3, phi):
            if is_coprime(x, phi) and isprime(x):
                self.public_e = x
                break

        self.private_d = mod_inverse2(self.public_e, phi)
        self.n = p_num * q_num

    def encrypt(self, m):
        return [ord(char) ** self.public_e % self.n for char in m]

    def decrypt(self, encrypted_message):
        return [chr((char ** self.private_d) % self.n) for char in encrypted_message]
