from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

from quantum.circuit_runner import run

# Quantum Random Number Generation

def _setup(length: int = 1) :
    if length < 1:
        length = 1
    circuit = QuantumCircuit(length, length)
    for idx in range(length):
        circuit.h(idx)
        circuit.measure(idx, idx)
    return circuit

def _run(circuit: QuantumCircuit):
    result = run(circuit)
    return result
    

def _get_measurement_result(result) -> str:
    bits = max(result.get_counts().keys(), key=(lambda key: result.get_counts()[key]))
    
    return bits

def random(length: int = 1):
    """
    Generates a random sequence of bits of length `length`.
    """
    circuit = _setup(length)
    result = _run(circuit)
    return _get_measurement_result(result)

if __name__ == "__main__":
    print(random(2))