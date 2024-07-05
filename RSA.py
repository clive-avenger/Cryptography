import random
from sympy import isprime

class RSA:
    def __init__(self):
        self.p = self.generate_prime()
        self.q = self.generate_prime()
        while self.p == self.q:
            self.q = self.generate_prime()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.choose_e()
        self.d = self.mod_inverse(self.e, self.phi)

    def generate_prime(self):
        while True:
            num = random.randint(100, 999)
            if isprime(num):
                return num

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def choose_e(self):
        e = random.randint(2, self.phi - 1)
        while self.gcd(e, self.phi) != 1:
            e = random.randint(2, self.phi - 1)
        return e

    def mod_inverse(self, e, phi):
        d = 0
        x1, x2, x3 = 1, 0, phi
        y1, y2, y3 = 0, 1, e
        while y3 != 1:
            q = x3 // y3
            t1, t2, t3 = x1 - q * y1, x2 - q * y2, x3 - q * y3
            x1, x2, x3 = y1, y2, y3
            y1, y2, y3 = t1, t2, t3
        return y2 % phi

    def encrypt(self, plaintext):
        ciphertext = [pow(ord(char), self.e, self.n) for char in plaintext]
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''.join([chr(pow(char, self.d, self.n)) for char in ciphertext])
        return plaintext

# Example usage
rsa = RSA()
print(f"Generated primes: p = {rsa.p}, q = {rsa.q}")
print(f"Public key: (e = {rsa.e}, n = {rsa.n})")
print(f"Private key: (d = {rsa.d}, n = {rsa.n})")

message = "Hello, RSA!"
print(f"Original message: {message}")
encrypted_message = rsa.encrypt(message)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = rsa.decrypt(encrypted_message)
print(f"Decrypted message: {decrypted_message}")
