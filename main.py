import random
from math import fmod, gcd, sqrt
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
    def __init__(self, p_num, q_num):
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


if __name__ == '__main__':
    # generate two random primes from given range -- kind of a security regulator
    p, q = random.sample(list(primerange(500, 1500)), 2)
    print(p, q)
    rsa = RSA(p, q)
    print(f"d = {rsa.private_d} \ne = {rsa.public_e} \nn = {rsa.n}")
    mess_to_encrypt = "AlAma Kot4  !@#$"
    print(f"message to encrypt: {mess_to_encrypt}")
    encrypted_mess = rsa.encrypt(mess_to_encrypt)
    print(f"encrypted message: {encrypted_mess}")
    decrypted_mess = ''.join(rsa.decrypt(encrypted_mess))
    print(f"decrypted message: {decrypted_mess}")
