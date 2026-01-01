import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (44, 62, 80) # Dark Blue-Grey
TEXT_COLOR = (236, 240, 241)
ACCENT_A = (231, 76, 60)   # Red
ACCENT_B = (52, 152, 219)  # Blue
STICK_COLOR = (241, 196, 15) # Yellow/Gold
STICK_HOVER = (243, 156, 18)
BTN_COLOR = (149, 165, 166)
BTN_HOVER = (127, 140, 141)

# Stick Dimensions
STICK_WIDTH = 10
STICK_HEIGHT = 150
STICK_SPACING = 25

class Button:
    def __init__(self, x, y, width, height, text, value, color=BTN_COLOR):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.value = value
        self.color = color
        self.hover_color = BTN_HOVER
        self.is_hovered = False
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=5)
        
        text_surf = self.font.render(self.text, True, TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def is_clicked(self, mouse_pos, mouse_pressed):
        return self.is_hovered and mouse_pressed[0]

class StickMindPygame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Stick Mind - Pygame Edition")
        self.clock = pygame.time.Clock()
        self.font_title = pygame.font.Font(None, 64)
        self.font_text = pygame.font.Font(None, 36)
        
        self.reset_game()
        
        # Create buttons for picking 1-4 sticks
        btn_y = HEIGHT - 100
        btn_w, btn_h = 150, 60
        gap = 20
        start_x = (WIDTH - (4 * btn_w + 3 * gap)) // 2
        
        self.buttons = []
        for i in range(1, 5):
            x = start_x + (i-1) * (btn_w + gap)
            self.buttons.append(Button(x, btn_y, btn_w, btn_h, f"Pick {i}", i))

    def reset_game(self):
        self.total_sticks = 21
        self.current_player = "A"
        self.game_over = False
        self.winner = None
        self.message = ""

    def handle_input(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    # Click anywhere to restart
                    self.reset_game()
                else:
                    for btn in self.buttons:
                        if btn.rect.collidepoint(mouse_pos):
                            self.play_turn(btn.value)

    def play_turn(self, sticks_to_take):
        if sticks_to_take > self.total_sticks:
            self.message = f"Only {self.total_sticks} sticks left!"
            return

        self.total_sticks -= sticks_to_take
        self.message = ""

        if self.total_sticks == 0:
            self.game_over = True
            # Current player took the last stick, so the OTHER player wins
            self.winner = "B" if self.current_player == "A" else "A"
        else:
            self.current_player = "B" if self.current_player == "A" else "A"

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.buttons:
            btn.check_hover(mouse_pos)

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)

        # Title
        title_surf = self.font_title.render("STICK MIND", True, TEXT_COLOR)
        title_rect = title_surf.get_rect(center=(WIDTH//2, 50))
        self.screen.blit(title_surf, title_rect)

        # Game Over Screen
        if self.game_over:
            win_text = f"GAME OVER! Player {self.winner} Wins!"
            win_surf = self.font_title.render(win_text, True, (46, 204, 113)) # Green
            win_rect = win_surf.get_rect(center=(WIDTH//2, HEIGHT//2))
            self.screen.blit(win_surf, win_rect)

            restart_surf = self.font_text.render("Click anywhere to play again", True, TEXT_COLOR)
            restart_rect = restart_surf.get_rect(center=(WIDTH//2, HEIGHT//2 + 60))
            self.screen.blit(restart_surf, restart_rect)
            
            pygame.display.flip()
            return

        # Game Info
        turn_color = ACCENT_A if self.current_player == "A" else ACCENT_B
        turn_text = f"Player {self.current_player}'s Turn"
        turn_surf = self.font_text.render(turn_text, True, turn_color)
        turn_rect = turn_surf.get_rect(center=(WIDTH//2, 100))
        self.screen.blit(turn_surf, turn_rect)

        if self.message:
            msg_surf = self.font_text.render(self.message, True, (231, 76, 60))
            msg_rect = msg_surf.get_rect(center=(WIDTH//2, 140))
            self.screen.blit(msg_surf, msg_rect)

        # Draw Sticks
        # Center the group of sticks
        total_width = (21 * STICK_WIDTH) + (20 * STICK_SPACING)
        start_x = (WIDTH - total_width) // 2
        
        for i in range(self.total_sticks):
            x = start_x + i * (STICK_WIDTH + STICK_SPACING)
            y = (HEIGHT - STICK_HEIGHT) // 2
            rect = pygame.Rect(x, y, STICK_WIDTH, STICK_HEIGHT)
            pygame.draw.rect(self.screen, STICK_COLOR, rect, border_radius=3)
            # Add a little shine
            pygame.draw.rect(self.screen, (255, 255, 255), (x+2, y+5, 2, STICK_HEIGHT-10), border_radius=1)

        # Draw Count
        count_surf = self.font_title.render(str(self.total_sticks), True, STICK_COLOR)
        count_rect = count_surf.get_rect(center=(WIDTH//2, (HEIGHT - STICK_HEIGHT)//2 - 40))
        self.screen.blit(count_surf, count_rect)

        # Draw Buttons
        for btn in self.buttons:
            btn.draw(self.screen)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_input()
            self.update()
            self.draw()
            self.clock.tick(60)

if __name__ == "__main__":
    game = StickMindPygame()
    game.run()
