import model.quantum_note as qnote

import quantum.qledger
import random
import consts

from bank.banker import Bank

import time

class Brute:
    def __init__(self):
        self.verify_iterations = 4
        pass

    def calc_permutations(self, n: int):
        # 4 states for each qubit
        return 4 ** n

    def calc_success_rate(self, n: int):
        return (3/4) ** n

    def generate_random_state(self, n: int):
        bits = []
        basis = []
        for i in range(n):
            basis.append(random.randint(0, 1))
            bits.append(random.randint(0, 1))

        return bits, basis


    def brute(self, note: qnote.QuantumNote):
        n = len(note.get_state())
    
        b = Bank()
        ledger = b.get_ledger()

        print("QNote: %d qubits" % n)
        print("Number of permutations: %d" % self.calc_permutations(n))
        print("Success rate: %f" % self.calc_success_rate(n))

        count = 1
        start_time = time.time()

        matches = []
        done = False
        while not done:
            verified = True
            bits, basis = note.get_state_encoded()
            # Run N times to reduce false positives
            for i in range(self.verify_iterations):
                if not ledger.verify(note):
                    verified = False

            if verified:
                print("Found a match!")
                print("Found bits: %s" % bits)
                print("Found basis: %s" % basis)
                matches.append((bits, basis))
                #break

            # cycle state
            # if current state is |0>, change to |1>
            # if current state is |->, cycle next qubit and so on
            for i in range(n):
                if note.state[i] == 4:
                    if i == n - 1:
                        if (len(matches) == 0):
                            print("No matches found.")
                        done = True
                        break
                    note.state[i] = 1
                    continue
                note.state[i] += 1
                break
        
            count += 1
        end_time = time.time()

        print("Found %d matches" % len(matches))
        for i in range(len(matches)):
            print("Match %d" % (i + 1))
            print("Bits: %s Basis: %s" % (matches[i][0], matches[i][1]))

        if len(matches) > 1:
            print("Determining actual bits and basis")
            while len(matches) > 1:
                remaining = []
                for match in matches:
                    note.set_state_encoded(match[0], match[1])
                    if ledger.verify(note):
                        remaining.append(match)
                matches = remaining
            print("Final Match => Bits: %s Basis: %s" % (matches[0][0], matches[0][1]))


        print("Time taken: %f seconds" % (end_time - start_time))


