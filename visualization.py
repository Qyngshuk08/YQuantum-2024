from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram, plot_circuit
import matplotlib.pyplot as plt

def generate_circuit_diagram():
    # Example 4-qubit circuit
    qc = QuantumCircuit(4)
    
    # Encoding
    qc.ry(1.57, 0)  # π/2 rotation
    qc.x(1)
    
    # Mixing
    qc.h(range(4))
    qc.cx(0,1)
    qc.cx(2,3)
    qc.rz(0.78, 2)  # π/4 rotation
    
    # Measurement
    qc.measure_all()
    
    # Save diagram
    qc.draw('mpl', filename='circuit_diagram.png')
    plot_histogram({'1010': 512, '0101': 512}, filename='output_dist.png')

if __name__ == '__main__':
    generate_circuit_diagram()
