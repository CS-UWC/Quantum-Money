import qiskit as qiskit

circuit = qiskit.QuantumCircuit(5)

for i in range(5):
    circuit.h(i)

circuit.measure_all()

result = qiskit.execute(circuit, backend=qiskit.Aer.get_backend('qasm_simulator'), shots=1, memory=True).result()
counts = result.get_counts(circuit)
roll = list(counts.keys())[0]
# parse to binary then to dec % 21
print((int(roll, 2) % 20) + 1)