import random
import time

# Initialize the game variables
score = 0
speed = 100
snake_length = 5
snake_x = 20
snake_y = 20
food_x = random.randint(0, 40)
food_y = random.randint(0, 40)
direction = "right"

# Define the snake and food objects
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = snake_length
        self.color = (0, 255, 0)

class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (255, 0, 0)

# Define the game loop
while True:
    # Update the snake position based on the direction
    if direction == "right":
        snake_x += 1
    elif direction == "left":
        snake_x -= 1
    elif direction == "up":
        snake_y -= 1
    elif direction == "down":
        snake_y += 1

    # Check for collisions with the walls or the snake itself
    if snake_x < 0 or snake_x > 40 or snake_y < 0 or snake_y > 40:
        break
    elif snake_x == food_x and snake_y == food_y:
        # Increase the score and regenerate the food position
        score += 1
        food_x = random.randint(0, 40)
        food_y = random.randint(0, 40)

    # Render the game state
    screen = pygame.display.set_mode((800, 600))
    screen.fill((0, 0, 0))
    snake = Snake(snake_x, snake_y)
    food = Food(food_x, food_y)
    pygame.draw.rect(screen, snake.color, pygame.Rect(snake.x, snake.y, 
10, 10))
    pygame.draw.rect(screen, food.color, pygame.Rect(food.x, food.y, 10, 
10))
    text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, (800/2 - 100, 600/2))
    pygame.display.update()
    time.sleep(speed)