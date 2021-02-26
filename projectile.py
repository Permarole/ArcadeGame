import pygame


class Projectile(pygame.sprite.Sprite,):

    def __init__(self, player,  offset=0):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.image = pygame.image.load('assets/laser_beam.png')
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x-7 + (player.image.get_width()/2) + offset
        self.rect.y = player.rect.y

    def move(self, is_player=True):

        # If the shot come from the player
        if is_player:
            self.rect.y -= self.velocity

            # Check collision with enemies
            for enemy in self.player.game.check_collision(self, self.player.game.all_enemies):
                # Delete projectile
                self.remove()
                # Inflict dmg to enemy
                enemy.damage(self.player.attack)
        # Else, the shot come from an enemy
        else:
            self.rect.y += self.velocity

            # Check collision with player
            for player in self.player.game.check_collision(self, self.player):
                # Delete projectile
                self.remove()
                # Inflict dmg to player
                player.damage(1)

        # Check if the projectile is out of bounds
        if self.rect.y < 0:
            # Delete projectile
            self.remove()

    def remove(self):
        # Delete projectile to free memory
        self.player.all_projectiles.remove(self)
