import random

def generate_serial():
    """
        Generate a random serial number for a QNote
    """
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # genereate 10 random chars
    serial = ""
    for i in range(10):
        serial += chars[random.randint(0, len(chars) - 1)]
    return serial

def generateBits(size):
    """
        Generate a series of random binary bits of a given size

        Returns a string of 0s and 1s
        
        Example: generateBits(10) -> "0101010101"
    """
    result = ""
    for i in range(size):
        result += str(random.randint(0, 1))
    return result

# generate 10 bit and 10 basis qnote
def generate_qnote():
    """
        Generate a random QNote
    """
    serial = generate_serial()
    bits = []
    basis = []
    for i in range(10):
        result = generateBits(10)

    

