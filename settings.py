import pygame
import os

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.5)

def play_bg_music():
    pygame.mixer.music.play(-1)

def stop_bg_music():
    pygame.mixer.music.stop()

def go_back():
    pygame.quit()
    os.system("python menu.py")
    exit()

def main():
    screen = pygame.display.set_mode((1910, 1031), pygame.RESIZABLE)
    pygame.display.set_caption('POWER AND LOVE/settings')
    bg = pygame.image.load("img/gallery_menu.jpg")
    bg = pygame.transform.scale(bg, (1910, 1027))
    bg_music = pygame.mixer.music.load("sounds/music.mp3")

    # Define buttons with width of 600 pixels
    button_width = 600
    mute_button = pygame.Rect((1910 - button_width) // 2, 515, button_width, 50)  # Mute/Unmute button
    volume_up_button = pygame.Rect((1910 - button_width) // 2, 565, button_width, 50)  # Increase volume button
    volume_down_button = pygame.Rect((1910 - button_width) // 2, 615, button_width, 50)  # Decrease volume button
    language_button = pygame.Rect((1910 - button_width) // 2, 665, button_width, 50)  # Change language button
    back_button = pygame.Rect((1910 - button_width) // 2, 965, button_width, 50)  # Back button

    # Define language buttons
    uzb_button = pygame.Rect((1910 - button_width) // 2, 715, button_width, 50)  # Uzb button
    rus_button = pygame.Rect((1910 - button_width) // 2, 765, button_width, 50)  # Rus button
    language_buttons_visible = False

    # Define button labels
    font = pygame.font.Font(None, 36)
    mute_label = font.render("Mute/Unmute", 1, (255,255,255))
    volume_up_label = font.render("Volume Up", 1, (255,255,255))
    volume_down_label = font.render("Volume Down", 1, (255,255,255))
    language_label = font.render("Change Language", 1, (255,255,255))
    back_label = font.render("Back", 1, (255,255,255))
    uzb_label = font.render("Uzb", 1, (255,255,255))
    rus_label = font.render("Rus", 1, (255,255,255))

    play_bg_music()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if mute_button.collidepoint(event.pos):
                    if pygame.mixer.music.get_busy():
                        stop_bg_music()
                    else:
                        play_bg_music()
                elif volume_up_button.collidepoint(event.pos):
                    volume = min(pygame.mixer.music.get_volume() + 0.1, 1)
                    pygame.mixer.music.set_volume(volume)
                elif volume_down_button.collidepoint(event.pos):
                    volume = max(pygame.mixer.music.get_volume() - 0.1, 0)
                    pygame.mixer.music.set_volume(volume)

                elif language_button.collidepoint(event.pos):
                    language_buttons_visible = not language_buttons_visible
                elif back_button.collidepoint(event.pos):
                    go_back()  # Call go_back function when back button is pressed

                if language_buttons_visible:
                    if uzb_button.collidepoint(event.pos):
                        # Add your code here to change the language to Uzbek
                        pass
                    elif rus_button.collidepoint(event.pos):
                        # Add your code here to change the language to Russian
                        pass

        screen.blit(bg, (0, 0))

        # Draw buttons
        pygame.draw.rect(screen, (255, 0, 0), mute_button)  # Red mute/unmute button
        pygame.draw.rect(screen, (0, 255, 0), volume_up_button)  # Green volume up button
        pygame.draw.rect(screen, (0, 0, 255), volume_down_button)  # Blue volume down button
        pygame.draw.rect(screen, (255, 255, 0), language_button)  # Yellow language button
        pygame.draw.rect(screen, (255, 0, 255), back_button)  # Magenta back button

        # Draw language buttons if visible
        if language_buttons_visible:
            pygame.draw.rect(screen, (0, 0, 0), uzb_button)  # Yellow Uzb button
            pygame.draw.rect(screen, (0, 0, 0), rus_button)  # Yellow Rus button

        # Draw button labels
        screen.blit(mute_label, (mute_button.centerx - mute_label.get_width() // 2, mute_button.centery - mute_label.get_height() // 2))
        screen.blit(volume_up_label, (volume_up_button.centerx - volume_up_label.get_width() // 2, volume_up_button.centery - volume_up_label.get_height() // 2))
        screen.blit(volume_down_label, (volume_down_button.centerx - volume_down_label.get_width() // 2, volume_down_button.centery - volume_down_label.get_height() // 2))
        screen.blit(language_label, (language_button.centerx - language_label.get_width() // 2, language_button.centery - language_label.get_height() // 2))
        screen.blit(back_label, (back_button.centerx - back_label.get_width() // 2, back_button.centery - back_label.get_height() // 2))

        # Draw language button labels if visible
        if language_buttons_visible:
            screen.blit(uzb_label, (uzb_button.centerx - uzb_label.get_width() // 2, uzb_button.centery - uzb_label.get_height() // 2))
            screen.blit(rus_label, (rus_button.centerx - rus_label.get_width() // 2, rus_button.centery - rus_label.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
