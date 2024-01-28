import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player

# Klasse an die Level übergeben wird (z.B. level1)
class Level:
    def __init__(self,level_data,surface):
        self.display_suface = surface
        self.initalise_level(level_data)
        self.world_shift = 0

# Funktion die durch level list iteriert und tiles plaziert
    def initalise_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

# zählt durch reihen und gibt position(index) der reihen aus
        for row_index,row in enumerate(layout):
            for column_index,cell in enumerate(row):
            # Multiplizieren da y sonst zu klein und tiles überlagern
                x = column_index * tile_size
                y = row_index * tile_size
                if cell == 1:
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                if cell == 2:
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

# Bewegung der Kamera in ABhängigkeit vom Spieler
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0

        else:
            self.world_shift = 0
            player.speed = 8


# Kollisionserkenneung aller Tiles beim vertikal laufen
    def horizontal_movement_collission(self):
        player = self.player.sprite

        player.rect.x += player.direction.x * player.speed

        for sprite in self.tile.sprites():
            if sprite.rect.colliderect(player.rect):
                # läuft links
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                # läuft rechts
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left


            
def vertical_movement_collision(self):
    player =   self.player.sprite
    player.apply_gravity() 

    for sprite in self.tile.sprites():
        if sprite.rect.colliderect(player.rect):
            # steht auf tile
            if player.direction.y < 0:
                player.rect.bottom = sprite.rect.top
            # y = 0 damit gravitation beim stehen nicht weiterwächst
                player.direction.y = 0
            # unter tile
            elif player.direction.y > 0:
                player.rect.top = sprite.rect.bottom
            # aufhebung -y movement
                player.direction.y = 0
                
                




# Darstellen der verschiedenen Komponenten
    def run(self):

    # tiles
        self.tiles.update(0)
        self.tiles.draw(self.display_suface)

    # player
        self.player.update()
        self.player.draw(self.display_suface)
        self.scroll_x()
        self.horizontal_movement_collission()
        self.vertical_movement_collision()