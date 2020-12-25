puzzle_input = [int(line.strip()) for line in open('puzzle_input.txt').readlines()]


class Device:
    def __init__(self, public_key):
        self.public_key = public_key
    
    def handshake(self, loop_size, subject_number):
        value = 1
        for _ in range(loop_size):
            value *= subject_number
            value = value % 20201227
        return value
    
    def crack_handshake(self):
        value = 1
        loop_size = 0
        while True:
            loop_size += 1
            value *= 7
            value = value % 20201227

            if value == self.public_key:
                self.loop_size = loop_size
                return self.loop_size

        # i = 0
        # while True:
        #     i += 1
        #     value = self.handshake(i, 7)
        #     if value == self.public_key:
        #         self.loop_size = i
        #         return i


card = Device(puzzle_input[0])
door = Device(puzzle_input[1])

print(card.public_key)
print(card.crack_handshake())
print(door.public_key)
print(door.crack_handshake())
print(card.handshake(card.loop_size, door.public_key))