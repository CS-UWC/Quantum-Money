class QuantumNote:
    def __init__(self, serial: str, states: list[int] = [], amount: int = 1):
        self.serial = serial
        self.state = states
        self.amount = amount
    
    def set_serial(self, serial: str):
        self.serial = serial

    def set_state(self, states: list[int]):
        self.state = states

    def set_state_str(self, states: str):
        self.state = [int(s) for s in states]

    def set_amount(self, amount: int):
        self.amount = amount

    def get_serial(self) -> str:
        return self.serial
    
    def get_state(self) -> list[int]:
        return self.state

    def get_state_str(self) -> str:
        return "".join(str(s) for s in self.state)

    def get_amount(self) -> int:
        return self.amount

    def get_state_encoded(self) -> (list[int], list[int]):
        bits = []
        basis = []
        for s in self.state:
            # |0>
            if s == 1:
                bits.append(0)
                basis.append(0)
            # |1>
            elif s == 2:
                bits.append(1)
                basis.append(0)
            # |+>
            elif s == 3:
                bits.append(0)
                basis.append(1)
            # |->
            elif s == 4:
                bits.append(1)
                basis.append(1)
        return bits, basis

    def set_state_encoded(self, bits: list[int], basis: list[int]):
        self.state = []
        for b, s in zip(bits, basis):
            # |0>
            if b == 0 and s == 0:
                self.state.append(1)
            # |1>
            elif b == 1 and s == 0:
                self.state.append(2)
            # |+>
            elif b == 0 and s == 1:
                self.state.append(3)
            # |->
            elif b == 1 and s == 1:
                self.state.append(4)