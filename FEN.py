import Pieces
class Node:
    def __init__ (self, id):
        self.id = id; self.name = None
    
    def print(self):
        print(self.id, ", ", self.name)

BASE_LAYOUT = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
index = 0
list = []
for i in range(8):
    for j in range(8):
        
        list.append(Node( (index) ))
        index += 1

index = 0
for char in BASE_LAYOUT:
    print(index)
    if char.isalpha():
        list[index].name = char
        index += 1

    if char.isdigit():
        index += int(char)

    if char == "/":
       index =  (index - index%8)
    
    if char == " ":
        break

    
for a in list:
    a.print()