class PaillierHomomorphic:
    """
    Paillier Additive Homomorphic Cryptosystem.
    Allows computation over encrypted ciphertexts without private key decryption.
    """
    def __init__(self, p=61, q=53):
        self.n = p * q
        self.n_sq = self.n * self.n
        self.g = self.n + 1
        self.lambda_val = (p - 1) * (q - 1)
        self.mu = pow(self.lambda_val, -1, self.n)

    def encrypt(self, m, r=3):
        c1 = pow(self.g, m, self.n_sq)
        c2 = pow(r, self.n, self.n_sq)
        return (c1 * c2) % self.n_sq

    def decrypt(self, c):
        u = pow(c, self.lambda_val, self.n_sq)
        l_u = (u - 1) // self.n
        return (l_u * self.mu) % self.n

    def add_encrypted(self, c1, c2):
        return (c1 * c2) % self.n_sq

    def scalar_mult(self, c, k):
        return pow(c, k, self.n_sq)
