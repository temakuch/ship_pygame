import pygame
import sys
from ship import Ship
from bullet import Bullet
from alien import Alien

WIDTH = 1920
HEIGHT = 1080
BACKGROUNG = (230, 230, 230)

class StarWars:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _update_screen(self):
        self.screen.fill(BACKGROUNG)
        self.ship.blit_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        pygame.display.flip()


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet() 

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _fire_bullet(self):
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x =  alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
        self.aliens.add(alien)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space = WIDTH - (2*alien_width)
        number_aliens = available_space // (2 * alien_width)
        ship_height = self.ship.rect.height
        available_space_y = (HEIGHT - (3*alien_height) - ship_height)
        number_rows = available_space_y // (3*alien_height)
        for row_number in range(number_rows):
            for alien_number in range(number_aliens):
                self.create_alien(alien_number, row_number)

    def update_alien(self):
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            print("EZ FREE FOR ME")

    def _update_bullets(self):
        self.bullets.update() #gg wp
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

        pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)                    
    def run_game(self):
        """
        Запуск програми
        """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            #self.update_alien()
            self._update_screen()



if __name__ == "__main__":
    game = StarWars()
    game.run_game()