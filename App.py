#https://www.youtube.com/watch?v=U4ogK0MIzqk
# TRANSFORM BACK TO SINGLE IDs
# calculate allowed knight moves with distance to center
# implement all rules
# get a "def (allowedMoves(board): [ListOfMoves]" function for deep search)
import pygame
import Pieces
import math

# PYGAME SETUP
pygame.init()
font = pygame.font.Font('seguisym.ttf', 40)
font_small = pygame.font.Font('seguisym.ttf', 10)
SCREEN_WIDTH = 640; SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock() 
running = True

# CLASSES
class Board:
    background_color = (189, 189, 189)
    selected_node = None; target_node = None
    KQkq = None
    nodes = []
    allowed_moves_ids = []
    borderIds = [0,1,2,3,4,5,6,7,
                 8,16,24,32,40,48,56,
                 57,58,59,60,61,62,63,
                 15,23,31,39,47,55]

    def create_fen_layout(self, layout):
        index = 0
        for char in layout:
            if char.isalpha():
                chess_board.nodes[index].name = char
                index += 1

            if char.isdigit():
                index += int(char)

            if char == "/":
                index = (index - index%8)
            
            if char == " ":
                break
            
    def checkOffsetMove(self,startId, offset):
        a = chess_board.nodes
        for i in range(1,8):
            newId = startId + (offset*i)

            # out of bounds
            if newId < 0 or newId > 63:
                break

            # empty 
            if a[newId].name == "":
                self.allowed_moves_ids.append(newId)
            
            # own peace
            elif a[newId].name.isupper() == a[startId].name.isupper():
                break
            
            # enemy piece
            elif a[newId].name.isupper() != a[startId].name.isupper():
                self.allowed_moves_ids.append(newId)
                break

            if newId in chess_board.borderIds:
                break

    def get_move(self):
        print("calling get_move()")
        slidingOffsetBishops = [-9, -7, +9, +7]
        slidingOffsetRooks = [-8,+1,+8,-1]
        self.allowed_moves_ids.clear()
        a = chess_board.nodes
        index = self.selected_node

        match a[index].name:
            # black pawn
            case "p":
                print("p")
                if a[index+8].name == "":
                        self.allowed_moves_ids.append(index+8)

                for offset in [7,9]:
                    if a[index+offset].name != "" and (a[index+offset].name.isupper() != a[index].name.isupper()):
                        self.allowed_moves_ids.append(index+offset)

                if a[index].id >= 8 and a[index].id <= 15:
                     self.allowed_moves_ids.append(index+16)
            
            # white pawn
            case "P":
                print("P")
                if a[index-8].name == "":
                        self.allowed_moves_ids.append(index-8)

                for offset in [-7,-9]:
                    if a[index+offset].name != "" and (a[index+offset].name.isupper() != a[index].name.isupper()):
                        self.allowed_moves_ids.append(index+offset)

                if a[index].id >= 46 and a[index].id <= 55:
                     self.allowed_moves_ids.append(index-16)

            case "B" | "b":
               print("case: Bishop")
               for i in slidingOffsetBishops:
                   self.checkOffsetMove(index, i)
                   
            case "R" | "r":
                for i in slidingOffsetRooks:
                   self.checkOffsetMove(index, i)

            case "Q" | "q":
                for i in slidingOffsetBishops + slidingOffsetRooks:
                   self.checkOffsetMove(index, i)

            # movement for knight 
            case "N" | "n":
                offsetIds = [-17,-15, -6,10, 15,17, -10,6]
                pos1 = a[index].rect.center
                for x in offsetIds:
                    pos2 = a[index+x].rect.center
                    distance = int(math.sqrt( (pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2))
                    if distance == 122:
                        if a[index+x].name == "" or (a[index+x].name.isupper() != a[index].name.isupper()):

                            self.allowed_moves_ids.append(index+x)
 
        # move allowed
        #print("selected:", node_list[startId].name, "on",startId)
        print(self.allowed_moves_ids)
        self.colorize_targets()
        return self.allowed_moves_ids

    def execute_move(self):
        print("calling: excute_move()")
        selected = chess_board.selected_node; target = chess_board.target_node
        self.nodes[target].name = self.nodes[selected].name
        self.nodes[selected].name = ""

        # end of move
        self.allowed_moves_ids.clear()
        self.colorize_targets()

    def colorize_targets(self):
        for a in self.nodes:
            if a.id in self.allowed_moves_ids:
                a.isTarget = True
            else:
                a.isTarget = False

        draw()
class Node:
    def __init__(self,x,y,isWhite,id):
        self.rect = pygame.Rect(x,y,50,50)        
        self.color =  (200,200,255) if isWhite else (255,255,255)
        self.name = ""
        self.id = id
        self.isTarget = False

# METHODS
def draw():
    screen.fill(chess_board.background_color)

    for a in chess_board.nodes:
        pygame.draw.rect(screen, a.color, a.rect, 0, 5)
        screen.blit(font_small.render(str(a.id), False, (22,22,22)), (a.rect.bottomright[0]-40,a.rect.bottomright[1]-10 ))
        if a.name != "":
            screen.blit(font.render(str(Pieces.chess_pieces[a.name].symbol), False, (22,22,22)), (a.rect.x+5, a.rect.y))
        
        if a.isTarget:
             pygame.draw.rect(screen, (200,0,0), a.rect, 1, 5)

    screen.blit(font.render("sel: "+str(chess_board.selected_node), False, (255,255,255)), (SCREEN_WIDTH-200, 0 ))
    screen.blit(font.render("target: "+str(chess_board.target_node), False, (255,255,255)), (SCREEN_WIDTH-200, 50 ))
    pygame.display.flip()
    
# GAME SETUP
chess_board = Board()
BASE_LAYOUT = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
BASE_LAYOUT = "NnNnNnNn/pprppppb/8/3N4/2P1n3/1R1p4/P3PP1P/2QK1B1R w KQkq - 0 1"

index = 0
for i in range(8):
    for j in range(8):
        isWhite = False if (i+j) %2 == 0 else True
        chess_board.nodes.append(Node(5 + j*55, 5 +  i*55 , isWhite, index))
        index += 1
chess_board.create_fen_layout(BASE_LAYOUT)

# GAME LOOP
draw()
while running:
    clock.tick(30)
    # GETTING KEYS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_r:
                chess_board.nodes.create_fen_layout(BASE_LAYOUT)
                draw()
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            selected = [a.id for a in chess_board.nodes if a.rect.collidepoint(pos)][0]

            if chess_board.selected_node == None:
                chess_board.selected_node = selected
            else:
                chess_board.target_node = selected

            # execute (possible) move
            if chess_board.selected_node != None and chess_board.target_node == None:
                allowed_moves = chess_board.get_move()
            if chess_board.target_node != None:
                if allowed_moves:
                    chess_board.execute_move()
                chess_board.selected_node = None; chess_board.target_node = None
                
            draw()
  
pygame.quit()