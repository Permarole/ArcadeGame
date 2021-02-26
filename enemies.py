import pygame
import random
from projectile import Projectile
from bonus import Bonus, bonus_sprite
import random

DROP_RATE = 2.5


class Enemies(pygame.sprite.Sprite):

    def __init__(self, game, offset_x=0, offset_y=0):
        super().__init__()
        self.game = game
        self.velocity = 3
        self.attack = 1
        self.health = 2
        self.max_health = 2
        self.tick = pygame.time.get_ticks()
        # Keep track of projectile's sprite
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/minion.png')
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.image = pygame.transform.rotozoom(self.image, 180, 1)
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect(center=self.rect.center)
        self.rect.x = offset_x
        self.rect.y = offset_y
        # TODO : rotate minion
        # Information needed to rotate image
        # self.angle = 0
        # self.origin_image = self.image

    def damage(self, amount):
        # Inflict damage
        self.health -= amount

        # Check health <= 0
        if self.health <= 0:
            self.remove()
            # Spawn bonus
            if random.randrange(1, 10) < DROP_RATE:
                self.spawn_bonus()

    def remove(self):
        # Delete enemy
        self.game.all_enemies.remove(self)

    def spawn_bonus(self):
        name = random.choice(bonus_sprite)
        bonus = Bonus(name, self.game, (self.rect.x, self.rect.y))
        self.game.all_bonus.add(bonus)

    def forward(self):
        # Check collision with player first
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
            # TODO : Implement more complicated movements for enemies
        # TODO : Implement enemies destruction while oob
        # elif self.rect.y >= 0 :
        #     pass

        else:
            # Delete enemy
            self.remove()
            # Inflict dmf to player
            self.game.player.damage(1)

    def shoot(self):

        tick = pygame.time.get_ticks()

        if self.rect.y >= 0 and tick > self.tick + random.randrange(800, 4000, 800):
            # Create projectiles instance
            self.all_projectiles.add(Projectile(self, self.game.player, 'laser_beam_2'))
            self.tick = tick
        else:
            pass