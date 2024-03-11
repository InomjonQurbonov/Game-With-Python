import pygame
import webbrowser
import os

def play_bg_music():
    pygame.mixer.music.play(-1)

def stop_bg_music():
    pygame.mixer.music.stop()

def main():
    pygame.init()
    screen = pygame.display.set_mode((1910, 1031), pygame.RESIZABLE)
    pygame.display.set_caption('POWER AND LOVE')

    bg = pygame.image.load("img/menu.jpg")
    bg = pygame.transform.scale(bg, (1910, 1027))
    bg_music = pygame.mixer.music.load("sounds/music2.mp3")
    play_bg_music()

    clock = pygame.time.Clock()

    button1 = pygame.image.load("btn_game/btn_play.png")
    button2 = pygame.image.load("btn_game/Btn_yuk.png")
    button3 = pygame.image.load("btn_game/Btn-sett.png")
    button4 = pygame.image.load("btn_game/btn_gal.png")
    button5 = pygame.image.load("btn_game/developer.png")
    button_width, button_height = 500, 70
    button_spacing = 5
    button_x = (screen.get_width() - button_width) // 2
    button_y = (screen.get_height() - (5 * button_height + 4 * button_spacing)) // 2 + 270

    buttons = [
        pygame.Rect(button_x, button_y + i * (button_height + button_spacing), button_width, button_height)
        for i in range(5)
    ]

    right_button_width, right_button_height = 90, 90
    right_button_x = screen.get_width() - right_button_width - 10
    right_buttons = [
        pygame.Rect(right_button_x - i * (right_button_width + button_spacing), button_y - 600, right_button_width, right_button_height)
        for i in range(4)
    ]

    right_button1 = pygame.image.load("img/github.png")
    right_button2 = pygame.image.load("img/telegram.png")
    right_button3 = pygame.image.load("img/youtube.png")
    right_button4 = pygame.image.load("img/instagram.png")

    right_button_urls = [
        "https://github.com/InomjonQurbonov",
        "https://t.me/LONEWOLF_uz",
        "https://www.youtube.com/@LONEWOLF_Games",
        "https://instagram.com/inomjon6902?igshid=ZDdkNTZiNTM="
    ]

    right_button1 = pygame.transform.scale(right_button1, (right_button_width, right_button_height))
    right_button2 = pygame.transform.scale(right_button2, (right_button_width, right_button_height))
    right_button3 = pygame.transform.scale(right_button3, (right_button_width, right_button_height))
    right_button4 = pygame.transform.scale(right_button4, (right_button_width, right_button_height))

    button1 = pygame.transform.scale(button1, (button_width, button_height))
    button2 = pygame.transform.scale(button2, (button_width, button_height))
    button3 = pygame.transform.scale(button3, (button_width, button_height))
    button4 = pygame.transform.scale(button4, (button_width, button_height))
    button5 = pygame.transform.scale(button5, (button_width, button_height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                for i, button_rect in enumerate(buttons):
                    if button_rect.collidepoint(pos):
                        if i == 2:
                            stop_bg_music()
                            os.system('python settings.py')
                            exit()
                        if i == 3:
                            stop_bg_music()
                            os.system('python gallery.py')
                            exit()
                for j, right_button_rect in enumerate(right_buttons):
                    if right_button_rect.collidepoint(pos):
                        webbrowser.open(right_button_urls[j])
                if buttons[4].collidepoint(pos):
                    webbrowser.open("https://github.com/InomjonQurbonov")
        screen.blit(bg, (0, 0))
        for i, button_rect in enumerate(buttons):
            screen.blit(eval(f"button{i + 1}"), button_rect.topleft)
        for i, button_rect in enumerate(right_buttons):
            screen.blit(eval(f"right_button{i + 1}"), button_rect.topleft)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
