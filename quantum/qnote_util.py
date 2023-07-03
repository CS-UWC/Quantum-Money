from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer

import quantum.qnote as qnote

def gen_qnote_from_states(states: list[int]):
    n_qubits = len(states)
    if n_qubits == 0:
        return None
    circuit = QuantumCircuit(n_qubits, n_qubits)
    for idx, state in enumerate(states):
        initialise_qubit(idx, state, circuit)
    
    return circuit

def initialise_qubit(idx, state, circuit):
    match state:
        # 00 => |0>
        case 1:
            circuit.reset(idx)
        # 10 => |1>
        case 2:
            circuit.x(idx)
        # 01 => |+>
        case 3:
            circuit.h(idx)
        # 11 => |->
        case 4:
            circuit.x(idx)
            circuit.h(idx)
        case other:
            pass

def get_state_from_bit_and_basis(bit, basis):
    match [bit, basis]:
        case [0,0]:
            return 1
        case [1,0]:
            return 2
        case [0,1]:
            return 3
        case [1,1]:
            return 4
        case other:
            return 0

def verify_qnote(qnote: qnote.QNote, bits: list[int], bases: list[int]):
    qc = gen_qnote_from_states(qnote.states)
    bank_qnote = ""
    for idx, state in enumerate(qnote.states):
        bank_state = get_state_from_bit_and_basis(bits[idx], bases[idx])
        bank_qnote = str(expected_result_from_state(bank_state)) + bank_qnote
        measure_qubit(idx, bank_state, qc)

    bits_str = run_circuit(qc)
    print("Measured: ", bits_str)
    print("Expected: ", bank_qnote)
    return bits_str == bank_qnote

def expected_result_from_state(state: int):
    match state:
        case 1:
            return 0
        case 2:
            return 1
        case 3:
            return 0
        case 4:
            return 1
        case other:
            return 0

def run_circuit(qc: QuantumCircuit):
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1, memory=True).result()

    bits_str = result.get_memory()[0]
    return bits_str

def verify_qubit(idx: int, bank_state: int, qc: QuantumCircuit):

    pass
     
def verify_qnote_old(qnote: qnote.QNote, bits: list[int], bases: list[int]):
    for idx, state in enumerate(qnote.states):
        qnote_circuit = gen_qnote_from_state(state)
        bank_state = get_state_from_bit_and_basis(bits[idx], bases[idx])
        if not verify(bank_state, qnote_circuit):
            return False
    return True

def measure_qubit(idx: int, bank_state: int, qc: QuantumCircuit):
    if bank_state in [3, 4]:
        qc.h(idx)
    qc.measure(idx, idx)


def measure_qnote(idx: int, bank_state: int, qc: QuantumCircuit):
    if bank_state in [3, 4]:
        qc.h(0)
    qc.measure(0,0)
        
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend, shots=1, memory=True).result()

    bits_str = result.get_memory()

    return int(bits_str[0][0])

def verify(idx: int, bank_state: int, qnote_circuit: QuantumCircuit):
    if bank_state == 0:
        return False
    
    # if in x axis
    result = measure_qnote(idx, idx, bank_state, qnote_circuit)

    if bank_state in [2, 4]:
        return result == 1
    else:
        return result == 0
    


if __name__ == "__main__":
    ledger = [[[0,1],[0,1]], [[1],[0]], [[0],[1]], [[1],[1]]]
    expected = [b'10', b'1', b'0', b'1']
    for i in range(4):
        if i == 0:
            qn = qnote.QNote("abc", [1, 4])
        else:
            qn = qnote.QNote("abc", [i + 1])
        result = {
            "serial": qn.serial,
            "states": qn.states,
            "bank_state": ledger[i],
            "expected": expected[i],
            "verified": verify_qnote(qn, ledger[i][0], ledger[i][1])
        }
        print(result)

    


            

