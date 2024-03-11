import pygame
import os

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1031
TARGET_WIDTH = 350
TARGET_HEIGHT = 150
GRID_ROWS = 2
GRID_COLS = 6

BUTTON_WIDTH = 100
BUTTON_HEIGHT = 100
BUTTON_MARGIN = 10

IMAGE_DIRECTORY = "gallery"
full_screen_image = None
def resize_image(image, new_width, new_height):
    return pygame.transform.scale(image, (new_width, new_height))

def play_bg_music():
    pygame.mixer.music.load("sounds/music1.mp3")
    pygame.mixer.music.play(-1)

def draw_button(screen, button_img, x, y, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_MARGIN, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, (255, 255, 255), (x-5, y-5, BUTTON_WIDTH+10, BUTTON_HEIGHT+10), 3)

    if x + BUTTON_WIDTH > mouse[0] > x and y + BUTTON_HEIGHT > mouse[1] > y:
        if click[0] == 1 and action != None:
            action()
    screen.blit(button_img, (x, y))

def go_back():
    pygame.quit()
    os.system("python menu.py")
    exit()

def handle_events(current_index, resized_images, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_MARGIN):
    global full_screen_image
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, current_index
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                current_index = (current_index - 1) % len(resized_images)
            elif event.key == pygame.K_RIGHT:
                current_index = (current_index + 1) % len(resized_images)
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_x, mouse_y = event.pos
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    index = row * GRID_COLS + col
                    if index < len(resized_images):
                        x = SCREEN_WIDTH // 2 - (GRID_COLS * TARGET_WIDTH) // 2 + col * TARGET_WIDTH
                        y = SCREEN_HEIGHT // 2 - (GRID_ROWS * TARGET_HEIGHT) // 2 + row * TARGET_HEIGHT
                        if x <= mouse_x <= x + TARGET_WIDTH and y <= mouse_y <= y + TARGET_HEIGHT:
                            if full_screen_image is not None:
                                # Rasm kattalashtirilgan, uni kichiklashtirish
                                full_screen_image = None
                            else:
                                # Rasm kichik, uni kattalashtirish
                                full_screen_image = pygame.transform.scale(resized_images[index], (SCREEN_WIDTH, SCREEN_HEIGHT))
    return True, current_index
def main():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("POWER AND LOVE/gallery")

    play_bg_music()

    background = pygame.image.load("img/gallery_menu.jpg")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

    image_files = [file for file in os.listdir(IMAGE_DIRECTORY) if file.endswith(('.png', '.jpg', '.jpeg'))]
    images = [pygame.image.load(os.path.join(IMAGE_DIRECTORY, file)) for file in image_files]
    resized_images = [resize_image(image, TARGET_WIDTH, TARGET_HEIGHT) for image in images]

    back_button_img = pygame.image.load("btn_game/back.png")
    back_button_img = pygame.transform.scale(back_button_img, (BUTTON_WIDTH, BUTTON_HEIGHT))

    current_index = 0

    clock = pygame.time.Clock()
    FPS = 60

    running = True
    while running:
        running, current_index = handle_events(current_index, resized_images, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_MARGIN)

        screen.blit(background, (0, 0))

        if full_screen_image is not None:
            screen.blit(full_screen_image, (0, 0))
        else:
            for row in range(GRID_ROWS):
                for col in range(GRID_COLS):
                    index = row * GRID_COLS + col
                    if index < len(resized_images):
                        current_image = resized_images[index]
                        x = SCREEN_WIDTH // 2 - (GRID_COLS * TARGET_WIDTH) // 2 + col * TARGET_WIDTH
                        y = SCREEN_HEIGHT // 2 - (GRID_ROWS * TARGET_HEIGHT) // 2 + row * TARGET_HEIGHT
                        screen.blit(current_image, (x, y))

        draw_button(screen, back_button_img, BUTTON_MARGIN, BUTTON_MARGIN, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_MARGIN, go_back)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
