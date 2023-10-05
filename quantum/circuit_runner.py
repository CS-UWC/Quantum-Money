from quantum.backend import get_backend
from qiskit.providers import JobStatus
import time

def run(circuit):
    (backend, backend_type) = get_backend()
    match backend_type:
        case 'aws':
            return _run_aws(circuit, backend)
        case _:
            return _run_local(circuit, backend)
        
# 3 seconds
wait = 5

def _run_aws(circuit, backend):
    task = backend.run(circuit, shots=10)

    while True:
        id = task.job_id()
        print(f'Job ID: {id}')
        job = backend.retrieve_job(job_id=id)
        if job.status() == JobStatus.DONE:
            return job.result()
        print(job.status())
        print('Waiting for task to complete...')
        time.sleep(wait)

def _run_local(circuit, backend):
    task = backend.run(circuit, shots=1, memory=True)
    return task.result()

def result_aggregator(results: list[str]):
    count = {}

    for result in results:
        if result in count:
            count[result] += 1
        else:
            count[result] = 1
    
    # return the most common result
    return max(count, key=count.get)
    


if __name__ == "__main__":
    from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, result as qiskit_result

    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.x(1)
    circuit.h(1)

    circuit.h(0)
    circuit.h(1)

    # Expects 01
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    result = run(circuit)
    print(result.get_memory())
    print(result.get_counts())
    print(result_aggregator(result.get_memory()))