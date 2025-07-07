import pygame
import random

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Set title
pygame.display.set_caption("Scenario Card")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 191, 255)
light_blue = (0, 255, 255)

# Font
font = pygame.font.Font(None, 36)

# Text elements
main_scenario_text = font.render("MAIN SCENARIO #1", True, white)
proof_of_value_text = font.render("(PROOF OF VALUE)", True, white)
kill_one_or_more_lives_text = font.render("KILL ONE OR MORE LIVES.", True, white)
category_text = font.render("CATEGORY: MAIN", True, white)
difficulty_text = font.render("DIFFICULTY: F", True, white)
time_limit_text = font.render("TIME LIMIT: 30 MINUTES", True, white)
reward_text = font.render("REWARD: 300 COINS", True, white)
failure_text = font.render("FAILURE: DEATH", True, white)

# Position text elements
main_scenario_text_rect = main_scenario_text.get_rect(center=(screen_width // 2, 50))
proof_of_value_text_rect = proof_of_value_text.get_rect(center=(screen_width // 2, 100))
kill_one_or_more_lives_text_rect = kill_one_or_more_lives_text.get_rect(center=(screen_width // 2, 150))
category_text_rect = category_text.get_rect(center=(screen_width // 2, 200))
difficulty_text_rect = difficulty_text.get_rect(center=(screen_width // 2, 250))
time_limit_text_rect = time_limit_text.get_rect(center=(screen_width // 2, 300))
reward_text_rect = reward_text.get_rect(center=(screen_width // 2, 350))
failure_text_rect = failure_text.get_rect(center=(screen_width // 2, 400))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill(black)

    # Draw text
    screen.blit(main_scenario_text, main_scenario_text_rect)
    screen.blit(proof_of_value_text, proof_of_value_text_rect)
    screen.blit(kill_one_or_more_lives_text, kill_one_or_more_lives_text_rect)
    screen.blit(category_text, category_text_rect)
    screen.blit(difficulty_text, difficulty_text_rect)
    screen.blit(time_limit_text, time_limit_text_rect)
    screen.blit(reward_text, reward_text_rect)
    screen.blit(failure_text, failure_text_rect)

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()