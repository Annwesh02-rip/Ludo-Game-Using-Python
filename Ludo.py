import random
import time
import pygame

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ludo Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

def roll_dice():
    return random.randint(1, 6)

def move_player(player, position):
    dice_roll = roll_dice()
    print(f"{player} rolled a {dice_roll}")
    position += dice_roll
    if position > 100:
        position -= dice_roll  # Cannot exceed 100
    return position, dice_roll

def draw_dice_face(dice_roll):
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, (250, 150, 100, 100), 2)
    dot_positions = {
        1: [(300, 200)],
        2: [(275, 175), (325, 225)],
        3: [(275, 175), (300, 200), (325, 225)],
        4: [(275, 175), (325, 175), (275, 225), (325, 225)],
        5: [(275, 175), (325, 175), (300, 200), (275, 225), (325, 225)],
        6: [(275, 175), (325, 175), (275, 200), (325, 200), (275, 225), (325, 225)]
    }
    for pos in dot_positions[dice_roll]:
        pygame.draw.circle(screen, BLACK, pos, 7)
    pygame.display.flip()
    time.sleep(1.5)

def draw_screen(player, dice_roll, position):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)
    text = font.render(f"{player} rolled a {dice_roll}, Position: {position}", True, BLACK)
    screen.blit(text, (50, 50))
    draw_dice_face(dice_roll)

def play_ludo():
    players = ["Player 1", "Player 2"]
    positions = {player: 0 for player in players}
    
    print("Welcome to Ludo!")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        for player in players:
            input(f"{player}, press Enter to roll the dice...")
            positions[player], dice_roll = move_player(player, positions[player])
            draw_screen(player, dice_roll, positions[player])
            print(f"{player} is now at position {positions[player]}")
            
            if positions[player] == 100:
                print(f"{player} wins!")
                pygame.quit()
                return

if __name__ == "__main__":
    play_ludo()
