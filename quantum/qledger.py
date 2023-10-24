from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, result as qiskit_result

from quantum.backend import get_backend
from quantum.circuit_runner import run, result_aggregator

def _setup(n: int) -> QuantumCircuit:
    return QuantumCircuit(n, n)

def initialise_note(bits: list[int], basis: list[int], circuit: QuantumCircuit) -> QuantumCircuit:
    for idx, (b, s) in enumerate(zip(bits, basis)):
        # |0>
        if b == 0 and s == 0:
            continue
            # circuit.reset(idx)
        # |1>
        elif b == 1 and s == 0:
            circuit.x(idx)
        # |+>
        elif b == 0 and s == 1:
            circuit.h(idx)
        # |->
        elif b == 1 and s == 1:
            circuit.x(idx)
            circuit.h(idx)
    return circuit

def measure_note(bits: list[int], basis: list[int], circuit: QuantumCircuit) -> QuantumCircuit:
    for idx, (b, s) in enumerate(zip(bits, basis)):
        if s == 1:
            circuit.h(idx)
        
        circuit.measure(idx, idx)
    return circuit

def get_measurement_bits(result: qiskit_result.Result):
    # choose key with most common value
    bits = max(result.get_counts().keys(), key=(lambda key: result.get_counts()[key]))
    
    # reverse the bits
    return bits[::-1]

def _run(circuit: QuantumCircuit):
    result = run(circuit)
    return result

def verify_measurement(measured_bits: str, bits: list[int], basis: list[int]) -> bool:
    for idx, bit in enumerate(measured_bits):
        if bits[idx] == 0 and int(bit) != 0:
            return False
        elif bits[idx] == 1 and int(bit) != 1:
            return False
    return True
            

def verify(bits: list[int], basis: list[int], actual_bits: list[int], actual_basis: list[int]) -> bool:
    circuit = _setup(len(bits))
    circuit = initialise_note(bits, basis, circuit)
    circuit = measure_note(actual_bits, actual_basis, circuit)
    result = _run(circuit)
    measured_bits = get_measurement_bits(result)
    return verify_measurement(measured_bits, actual_bits, actual_basis)

if __name__ == "__main__":
    actual_bits = [1, 0]
    actual_basis = [0, 1]

    user_bits = [1, 0]
    user_basis = [0, 1]

    circuit = _setup(len(user_bits))
    circuit = initialise_note(user_bits, user_basis, circuit)
    circuit = measure_note(actual_bits, actual_basis, circuit)
    result = _run(circuit)
    measured_bits = get_measurement_bits(result)
    print(measured_bits)
    print(verify_measurement(measured_bits, actual_bits, actual_basis))
    