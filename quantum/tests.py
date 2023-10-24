from qrng import random
from qledger import verify

def test_qrng():
    assert random(1) in ['0', '1']

def test_qrng_8_qubits():
    assert len(random(8)) == 8

def test_measure_note():
    actual_bits = [0, 1, 1, 0, 1, 0, 1, 0]
    actual_basis = [0, 1, 0, 1, 0, 1, 0, 1]

    user_bits = [0, 1, 1, 0, 1, 0, 1, 0]
    user_basis = [0, 1, 0, 1, 0, 1, 0, 1]

    assert verify(actual_bits, actual_basis, user_bits, user_basis)

def test_measure_fail():
    actual_bits = [0, 1, 1, 0, 1, 0, 1, 0]
    actual_basis = [0, 1, 0, 1, 0, 1, 0, 1]

    user_bits = [1, 1, 1, 0, 1, 0, 1, 1]
    user_basis = [0, 1, 1, 1, 1, 1, 0, 0]

    assert not verify(actual_bits, actual_basis, user_bits, user_basis)

if __name__ == "__main__":

    tests = {
        "test_qrng": test_qrng,
        "test_qrng_8_qubits": test_qrng_8_qubits,
        "test_measure_note": test_measure_note,
        "test_measure_fail": test_measure_fail
    }
    print("Running tests...")
    for name, test in tests.items():
        print(f"Running {name}...")
        try:
            test()
            print(f"{name} passed. ✅")
        except AssertionError:
            print(f"{name} failed. ❌")
            raise
       
    print("All tests passed.")