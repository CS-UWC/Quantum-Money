from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

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
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(circuit, simulator, shots=1, memory=True)
    result = job.result()
    return result
    

def _get_measurement_result(result) -> str:
    return result.get_memory()[0]

def random(length: int = 1):
    """
    Generates a random sequence of bits of length `length`.
    """
    circuit = _setup(length)
    result = _run(circuit)
    return _get_measurement_result(result)

if __name__ == "__main__":
    print(random(2))