import pygame
from projectile import Projectile

LOWER_POS = 1000
MIDDLE_POS = (720 - 72) / 2


# Create player
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 4
        self.max_health = 4
        self.lives = 3
        self.default_lives = 3
        self.max_lives = 5
        self.double_shoot = False
        # Keep track of projectile's sprite
        self.all_projectiles = pygame.sprite.Group()
        self.velocity = 6
        self.attack = 1
        self.image = pygame.image.load('assets/pngegg.png')
        # Scale sprite
        # self.image = pygame.transform.scale(self.image, (200,200))
        self.rect = self.image.get_rect()
        self.rect.x = (game.screen_width - 72) / 2
        self.rect.y = game.screen_height

    def move_right(self):
        self.rect.x += self.velocity*1.5

    def move_left(self):
        self.rect.x -= self.velocity*1.5

    def move_up(self):
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.y += self.velocity

    def shoot(self):
        # Check for double fire
        if self.double_shoot:
            # Create projectiles instance
            self.all_projectiles.add(Projectile(self, -4))
            self.all_projectiles.add(Projectile(self, 4))
        else:
            # Create projectiles instance
            self.all_projectiles.add(Projectile(self))

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            if self.lives > 0:
                self.lives -= 1
                self.health = self.max_health
            else :
                self.game.game_over()

    def update_player_lives(self, screen):

        lives_images = self.image
        lives_images = pygame.transform.scale(lives_images, (20, 20))
        for i in range(self.lives):
            screen.blit(lives_images, (20+i*25, self.game.screen_height-30))

    def life_up(self):

        if self.lives < self.max_lives:
            self.lives += 1

    def double_fire(self):

        self.double_shoot = True
