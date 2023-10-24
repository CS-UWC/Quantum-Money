from qiskit_braket_provider import AWSBraketProvider, BraketLocalBackend
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, execute, Aer, result as qiskit_result

USE_SIMULATOR = True

# returns (backend, backend_type)
# where backend_type is either 'local' or 'aws'
def get_backend():
    simulator = Aer.get_backend('qasm_simulator')
    if USE_SIMULATOR:
        # print('Using local simulator.')
        return (simulator, 'local')

    try:
        # print('Connecting to AWS Braket.')
        backend = _get_aws_backend()
        # print('Connected to AWS Braket.')
        return (backend, 'aws')
    except:
        # print('Could not connect to AWS Braket. Using local simulator instead.')
        return (simulator, 'local')


def _get_aws_backend():
    provider = AWSBraketProvider()
    return provider.get_backend('Lucy')