from client import PaillierHomomorphic

def main():
    print("=== Testing Paillier Homomorphic Encryption ===")
    pail = PaillierHomomorphic()
    
    m1, m2 = 120, 80
    c1 = pail.encrypt(m1, r=7)
    c2 = pail.encrypt(m2, r=11)
    
    # Homomorphic addition: Decrypt(c1 * c2) = m1 + m2
    c_sum = pail.add_encrypted(c1, c2)
    dec_sum = pail.decrypt(c_sum)
    print(f"Encrypted addition: {m1} + {m2} = {dec_sum}")
    assert dec_sum == 200
    
    # Scalar multiplication: Decrypt(c1 ^ 3) = 3 * m1
    c_mult = pail.scalar_mult(c1, 3)
    dec_mult = pail.decrypt(c_mult)
    print(f"Encrypted scalar multiplication: {m1} * 3 = {dec_mult}")
    assert dec_mult == 360
    print("=== Paillier Homomorphic Verification Complete ===")

if __name__ == "__main__":
    main()
