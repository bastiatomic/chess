#https://www.youtube.com/watch?v=U4ogK0MIzqk
import pygame
import Pieces

# PYGAME SETUP
pygame.init()
font = pygame.font.Font('seguisym.ttf', 40)
font_small = pygame.font.Font('seguisym.ttf', 10)
screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock() 
running = True

# CLASSES
class Board:
    background_color = (189, 189, 189)
    selected_node = None; target_node = None

class Node:
    def __init__(self,x,y,isWhite,id):
        self.rect = pygame.Rect(x,y,50,50)
                        # dark                      # light
        self.color = (161,	136	,127) if isWhite else (188	,170	,164)
        self.symbol = None
        self.name = None
        self.id = id

# METHODS
def create_fen_layout(node_list, layout):
    index = 0
    for char in layout:
        if char.isalpha():
            node_list[index].name = char
            node_list[index].symbol = Pieces.chess_pieces[char].symbol
            index += 1

        if char.isdigit():
            index += int(char)

        if char == "/":
            index =  (index - index%8)
        
        if char == " ":
            break

    return node_list

def draw(node_list):
    screen.fill(BOARD.background_color)

    for a in node_list:
        pygame.draw.rect(screen, a.color, a.rect, 0, 5)
        screen.blit(font_small.render(str(a.id), False, (22,22,22)), (a.rect.bottomright[0]-10,a.rect.bottomright[1]-10 ))
        if a.symbol != None:
            screen.blit(font.render(str(a.symbol), False, (22,22,22)), (a.rect.x+5, a.rect.y))

    pygame.display.flip()
    
# GAME SETUP
BOARD = Board()
node_list = []
BASE_LAYOUT = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
index = 0
for i in range(8):
    for j in range(8):
        
        isWhite = False if (i+j) %2 == 0 else True
        node_list.append(Node(5 + j*55,5 +  i*55 , isWhite, index))
        index += 1

node_list = create_fen_layout(node_list, BASE_LAYOUT)

# GAME LOOP
draw(node_list)
while running:
    clock.tick(30)
    # GETTING KEYS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               print("SPACE")
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print([a.name for a in node_list if a.rect.collidepoint(pos)][0])
                
                    
  
pygame.quit()