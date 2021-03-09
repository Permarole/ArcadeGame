import pygame


class Projectile(pygame.sprite.Sprite):

    def __init__(self, shooter, player, sprite, offset=0):
        super().__init__()
        self.velocity = 7
        self.player = player
        self.shooter = shooter
        self.image = sprite
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.rect = self.image.get_rect()
        self.rect.x = shooter.rect.x-7 + (shooter.image.get_width()/2) + offset
        self.rect.y = shooter.rect.y

    def move(self, is_player=True):


        # If the shot come from the player
        if is_player:
            self.rect.y -= self.velocity

            # Check collision with enemies
            for enemy in self.shooter.game.check_collision(self, self.shooter.game.all_enemies):
                # Delete projectile
                self.remove()
                # Inflict dmg to enemy
                enemy.damage(self.shooter.attack)
        # Else, the shot come from an enemy
        else:
            self.rect.y += self.velocity

            # Check collision with player
            for player in self.shooter.game.check_collision(self, self.shooter.game.all_players):
                # Delete projectile
                self.remove()
                # Inflict dmg to player
                player.damage(self.shooter.attack)

        # Check if the projectile is out of bounds
        if self.rect.y < 0 or self.rect.y - 60 >= self.shooter.game.screen_height:
            # Delete projectile
            self.remove()

    def remove(self):
        # Delete projectile to free memory
        self.shooter.all_projectiles.remove(self)
