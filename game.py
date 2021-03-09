import pygame
from enemies import Enemies
from player import Player
import random


class Game:

    def __init__(self, size):

        self.screen_width = size[0]
        self.screen_height = size[1]
        self.tick = pygame.time.get_ticks()
        self.is_playing = False
        # Create player
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Group of monster
        self.all_enemies = pygame.sprite.Group()
        # Group of bonus
        self.all_bonus = pygame.sprite.Group()
        # Enemies map
        self.enemies_map = []
        # key pressed
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.map()
        self.spawn_enemies()

    def map(self):
        # Create a list that contains every minions positions (x,y)
        spacing = 0

        for i in range(20):
            # A waiting phase occurs every 3 minions
            if i % 3 == 0:
                spacing -= 800
            self.enemies_map.append((random.randrange(10, self.screen_width - 82, 50), spacing - 100*(i % 3)))

    def game_over(self):

        self.all_enemies = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.lives = self.player.default_lives
        self.is_playing = False

    def update(self, screen):

        # Check pressed key
        keys = pygame.key.get_pressed()
        # Need to bond te image so that it can't go out the screen's borders
        if keys[pygame.K_RIGHT] and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        if keys[pygame.K_LEFT] and self.player.rect.x > 0:
            self.player.move_left()
        if keys[pygame.K_UP] and self.player.rect.y > 0:
            self.player.move_up()
        if keys[pygame.K_DOWN] and self.player.rect.y + self.player.rect.height < self.screen_height:
            self.player.move_down()
        if keys[pygame.K_SPACE]:
            tick = pygame.time.get_ticks()
            if tick >= self.tick + 200:
                self.tick = tick
                self.player.shoot()

        # APPLY SPRITES
        # Apply player's sprite
        screen.blit(self.player.image, self.player.rect)

        # Apply every player's projectiles
        self.player.all_projectiles.draw(screen)

        # Apply every enemies projectiles
        for enemy in self.all_enemies:
            enemy.all_projectiles.draw(screen)

        # Apply every enemies
        self.all_enemies.draw(screen)

        # Apply every bonus
        self.all_bonus.draw(screen)

        # UPDATE SPRITE POSITION :
        # Get current enemies
        for enemy in self.all_enemies:
            enemy.forward()
            enemy.shoot()
            enemy.update_health_bar(screen)
            # # Get current enemies projectiles
            for projectile in enemy.all_projectiles:
                projectile.move(False)
        # Get current player's projectiles
        for own_projectile in self.player.all_projectiles:
            own_projectile.move()
        # Get current bonus
        for bonus in self.all_bonus:
            bonus.forward()

        # Refresh remaining  lives
        self.player.update_player_lives(screen)

        # Update health bar
        self.player.update_health_bar(screen)

    def check_collision(self, sprite, group):
        # Return boolean
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_enemies(self):
        for pos in self.enemies_map:
            enemies = Enemies(self, pos[0], pos[1])
            self.all_enemies.add(enemies)
