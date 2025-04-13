#!/bin/bash

echo "Quantum Hash Benchmark Suite"
echo "==========================="

for size in 8 16 32 64 128 256
do
    echo -n "Input ${size} bits: "
    python -c "
import timeit
from main import quantum_hash
data = bytes([0]*${size//8})
t = timeit.timeit(lambda: quantum_hash(data), number=10)
print(f'{t/10:.5f} sec')
"
done

echo "Memory Usage Profile:"
python -m memory_profiler main.py
