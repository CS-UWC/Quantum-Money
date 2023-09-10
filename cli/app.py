import brute as brute_app
from model.quantum_note import QuantumNote
from bank.banker import Bank

class App():
    def __init__(self):
        pass

    def run(self):
        print("1\tBrute Force")
        print("2\tAdaptive Attack")

        choice = input("Enter choice: ")
        if int(choice) not in [1, 2]:
            print("Invalid choice.")
            return
        
        if int(choice) == 1:
            self.brute()
        elif int(choice) == 2:
            self.adaptive()
        
    def brute(self):
        b = brute_app.Brute()

        serial = input("Enter serial: ")
        qubits = int(input("Enter number of qubits: "))

        state = [int(i) for i in ('1' * qubits)]
        qnote = QuantumNote(serial, state)
        b.brute(qnote)

    def adaptive(self):
        print("Not implemented.")
        pass



if __name__ == "__main__":
    app = App()
    app.run()