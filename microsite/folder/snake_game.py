import pygame
import sys
import random
import json

# --- Inicializace Pygame ---
pygame.init()

# --- Nastavení hry ---
GRID_WIDTH = 15
GRID_HEIGHT = 15
BLOCK_SIZE = 50  # Zvětšíme bloky, aby byla hra na malé mřížce vidět

# Vypočítané rozměry
GAME_AREA_WIDTH = GRID_WIDTH * BLOCK_SIZE
GAME_AREA_HEIGHT = GRID_HEIGHT * BLOCK_SIZE
UI_AREA_WIDTH = 300  # Šířka panelu pro skóre a tlačítka
WINDOW_WIDTH = GAME_AREA_WIDTH + UI_AREA_WIDTH
WINDOW_HEIGHT = GAME_AREA_HEIGHT

# Barvy (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (40, 40, 40) # Barva mřížky
BLUE = (50, 153, 213) # Barva tlačítka

# Rychlost hada (kroky za sekundu)
SNAKE_SPEED = 5
FPS = 60

# Soubor pro ukládání skóre
SCORE_FILE = "snake_high_scores.json"

# --- Vytvoření okna ---
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
main_font = pygame.font.SysFont('Consolas', 24)
title_font = pygame.font.SysFont('Consolas', 30, bold=True)

# --- Funkce pro práci se skóre ---
def load_high_scores():
    """Načte nejlepší skóre ze souboru."""
    try:
        with open(SCORE_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_high_scores(score, scores):
    """Přidá nové skóre, seřadí a uloží 5 nejlepších."""
    scores.append(score)
    scores.sort(reverse=True)
    with open(SCORE_FILE, 'w') as f:
        json.dump(scores[:5], f)
    return scores[:5]

# --- Funkce pro vykreslování ---
def draw_grid():
    """Vykreslí mřížku na herní plochu."""
    for x in range(0, GAME_AREA_WIDTH, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, GAME_AREA_HEIGHT))
    for y in range(0, GAME_AREA_HEIGHT, BLOCK_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (GAME_AREA_WIDTH, y))

def draw_ui_panel(current_score, high_scores):
    """Vykreslí pravý panel s informacemi."""
    ui_rect = pygame.Rect(GAME_AREA_WIDTH, 0, UI_AREA_WIDTH, WINDOW_HEIGHT)
    pygame.draw.rect(screen, BLACK, ui_rect)
    
    # Aktuální skóre
    score_text = title_font.render(f"Score: {current_score}", True, WHITE)
    screen.blit(score_text, (GAME_AREA_WIDTH + 20, 20))

    # Nejlepší skóre
    hs_title_text = title_font.render("High Scores", True, WHITE)
    screen.blit(hs_title_text, (GAME_AREA_WIDTH + 20, 100))
    
    y_offset = 140
    for i, score in enumerate(high_scores):
        hs_text = main_font.render(f"{i+1}. {score}", True, WHITE)
        screen.blit(hs_text, (GAME_AREA_WIDTH + 20, y_offset))
        y_offset += 30

def draw_game_elements(snake_body, food_pos):
    """Vykreslí hada a jídlo."""
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0] * BLOCK_SIZE, pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0] * BLOCK_SIZE, food_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# --- Herní stavy ---
def game_loop():
    """Hlavní herní smyčka."""
    # Reset stavu hry
    snake_pos = [GRID_WIDTH // 2, GRID_HEIGHT // 2]
    snake_body = [[snake_pos[0], snake_pos[1]], [snake_pos[0] - 1, snake_pos[1]]]
    food_pos = [random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)]
    
    direction = 'RIGHT'
    change_to = direction
    score = 0
    
    high_scores = load_high_scores()

    last_move_time = pygame.time.get_ticks()
    move_interval = 1000 / SNAKE_SPEED

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                if event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'
        
        direction = change_to

        current_time = pygame.time.get_ticks()
        if current_time - last_move_time > move_interval:
            last_move_time = current_time

            # Pohyb hada
            if direction == 'UP': snake_pos[1] -= 1
            if direction == 'DOWN': snake_pos[1] += 1
            if direction == 'LEFT': snake_pos[0] -= 1
            if direction == 'RIGHT': snake_pos[0] += 1

            # Kolize s okrajem
            if not (0 <= snake_pos[0] < GRID_WIDTH and 0 <= snake_pos[1] < GRID_HEIGHT):
                return score # Konec hry, vrátí skóre

            # Růst a pohyb těla
            snake_body.insert(0, list(snake_pos))
            if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
                score += 1
                while food_pos in snake_body: # Zajistí, že se jídlo neobjeví v hadovi
                    food_pos = [random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)]
            else:
                snake_body.pop()

            # Kolize se sebou samým
            if snake_pos in snake_body[1:]:
                return score # Konec hry, vrátí skóre

        # Vykreslování
        screen.fill(BLACK)
        draw_grid()
        draw_game_elements(snake_body, food_pos)
        draw_ui_panel(score, high_scores)
        pygame.display.update()

        clock.tick(FPS)

def game_over_screen(score):
    """Obrazovka po skončení hry s možností hrát znovu."""
    high_scores = load_high_scores()
    high_scores = save_high_scores(score, high_scores)

    button_rect = pygame.Rect(GAME_AREA_WIDTH + 50, WINDOW_HEIGHT - 100, 200, 50)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return # Návrat do hlavní smyčky pro novou hru

        # Vykreslení obrazovky
        screen.fill(BLACK)
        draw_ui_panel(score, high_scores)

        # Text "Game Over" na herní ploše
        title_text = title_font.render("GAME OVER", True, RED)
        title_rect = title_text.get_rect(center=(GAME_AREA_WIDTH / 2, GAME_AREA_HEIGHT / 2 - 50))
        screen.blit(title_text, title_rect)

        # Tlačítko "Play Again"
        pygame.draw.rect(screen, BLUE, button_rect)
        button_text = main_font.render("Play Again", True, WHITE)
        button_text_rect = button_text.get_rect(center=button_rect.center)
        screen.blit(button_text, button_text_rect)

        pygame.display.update()
        clock.tick(15)

# --- Spuštění hry ---
if __name__ == "__main__":
    while True:
        final_score = game_loop()
        game_over_screen(final_score)