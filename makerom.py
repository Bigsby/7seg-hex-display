from math import pow

digit_segments = bytearray([
   #D 6543210
   #0babcdefg
    0b1111110, # 0
    0b0110000, # 1
    0b1101101, # 2
    0b1111001, # 3
    0b0110011, # 4
    0b1011011, # 5
    0b1011111, # 6
    0b1110000, # 7
    0b1111111, # 8
    0b1111011, # 9
    0b1110111, # A
    0b0011111, # b
    0b0001101, # c
    0b0111101, # d
    0b1001111, # E
    0b1000111 # F 
])

class Point():
    def __init__(self, x: int, y: int, char: str):
        self.x = x
        self.y = y
        self.char = char


positions = [
    Point(0, 1, "-"), # seg Afacefffffffasdf
    Point(1, 2, "|"), # seg B
    Point(3, 2, "|"), # seg C
    Point(4, 1, "-"), # seg D
    Point(3, 0, "|"), # seg E
    Point(1, 0, "|"), # seg F
    Point(2, 1, "-") # seg G
]

def printSegments(segments):
    for row in range(0, 5):
        for column in range(0, 3):
            print(segments[row][column], end="")
        print()

def displayDigit(digit):
    segments = [[' ' for j in range(3)] for i in range(5)]
    for segment in range(0, 7):
        bit = (digit >> (6 - segment)) & 1
        position = positions[segment]
        if bit:
            segments[position.x][position.y] = position.char
    printSegments(segments)
    print("-------------")

def showDigitOutput():
    for digit in digit_segments:
        displayDigit(digit)

def showBinaryResult():
    for digit in range(0,8):
        for index in range(0, len(digit_segments)):
            segments = digit_segments[index]
            print("{0:04x} {0:07b} {1:08b}".format(digit * 0x10 + index, segments))

def showOutput():
    for address in range(0x80):
        value = digit_segments[address % 0x10]
        print("{0:04x} {0:07b} {1:08b}".format(address, value))

def createRom():
    romSize = int(pow(2, 11))
    digitCount = len(digit_segments)
    print("Creating ROM for {0} charaters and size {1}".format(digitCount, romSize))
    rom = bytearray([ 0 ] * romSize)
    for address in range(digitCount):
        rom[address] = digit_segments[address % digitCount]

    return rom

def printRom(rom):
    for address in range(0, len(rom)):
        print("{0:010b} {0:03x} {1:08b}".format(address, rom[address]))

def createRomFile(rom, fileName):
    print("Creating ROM file as '{0}'".format(fileName))
    with open(fileName, "wb") as file:
        file.write(rom)
    
def main():
    rom = createRom()
    # printRom(rom)
    createRomFile(rom, "rom.bin")


if __name__ == "__main__":
    main()


# 4 digit display pin-out
# 12 11 10  9  8  7
#  1  A  F  2  3  B
#  1  2  3  4  5  6
#  E  D  P  C  G  4

# 2 digit display pin-out
# 10  9  8  7  6
#  A  B  1  2  F
#  1  2  3  4  5
#  C  P  E  D  G