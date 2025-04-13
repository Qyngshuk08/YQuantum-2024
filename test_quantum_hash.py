import unittest
from main import quantum_hash
import numpy as np

class TestQuantumHash(unittest.TestCase):
    def test_determinism(self):
        """Same input produces same output"""
        h1 = quantum_hash(b"test")
        h2 = quantum_hash(b"test")
        self.assertEqual(h1, h2)

    def test_avalanche_effect(self):
        """1-bit change produces >40% different bits"""
        h1 = quantum_hash(b"hello")
        h2 = quantum_hash(b"hellp")
        xor = int.from_bytes(h1, 'big') ^ int.from_bytes(h2, 'big')
        changed_bits = bin(xor).count('1')
        self.assertGreater(changed_bits/256, 0.4)

    def test_output_size(self):
        """Output is exactly 32 bytes (256 bits)"""
        for length in [1, 16, 64]:
            data = np.random.bytes(length)
            self.assertEqual(len(quantum_hash(data)), 32)

if __name__ == '__main__':
    unittest.main()
