from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

def gen_qnote(state):
    qreg_q = QuantumRegister(1, 'q')
    creg_c = ClassicalRegister(1, 'c')
    circuit = QuantumCircuit(qreg_q, creg_c)

    # [bit, basis]
    # [a, 0] z axis
    # [a, 1] x axis

    match state:
        # 00 
        case 0:
            circuit.reset(qreg_q[0])
        # 10
        case 1:
            circuit.x(qreg_q[0])
        # 01
        case 2:
            circuit.h(qreg_q[0])
        # 11
        case 3:
            circuit.x(qreg_q[0])
            circuit.h(qreg_q[0])
    
    return circuit



for i in range(4):
    qc = gen_qnote(i)
    qc.measure(qc.qregs[0], qc.cregs[0])
    sim = AerSimulator()
    result = sim.run(qc).result()
    counts = result.get_counts(qc)
    print(counts)
    plot_histogram(counts)
