import pygame
import random


class Bonus(pygame.sprite.Sprite):

    # pos: position of enemy when dying
    def __init__(self, sprite_name, game, enemy_pos=(0, 0), size=(40, 40)):
        super().__init__()
        self.name = sprite_name
        self.game = game
        self.speed = 1
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.x = enemy_pos[0]
        self.rect.y = enemy_pos[1]

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.speed
            # TODO : Implement bonus destruction while OOB
        elif self.rect.y >= self.game.screen_height :
                self.remove()
        else:
            self.improve(self.name)
            self.remove()


    def remove(self):
        self.game.all_bonus.remove(self)

    def improve(self, sprite_name):
        if sprite_name == 'health':
            self.game.player.life_up()
        elif sprite_name == 'double_fire':
            self.game.player.double_fire()





bonus_sprite = [
    'health',
    'double_fire'
]




