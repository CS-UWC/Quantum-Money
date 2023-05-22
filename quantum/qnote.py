class QNote:
    def __init__(self, serial: str, states: list[int] = []):
        self.serial = serial
        self.states = states
    
    def set_serial(self, serial: str):
        self.serial = serial

    def set_states(self, states: list[int]):
        self.states = states