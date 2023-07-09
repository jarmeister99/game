import arcade

from constants import SCREEN_WIDTH


def get_terrain() -> arcade.SpriteList:
    TILE_WIDTH = 16
    TILE_HEIGHT = 16
    terrain_list = arcade.SpriteList(use_spatial_hash=True)
    for x in range(0, SCREEN_WIDTH, TILE_WIDTH):
        for y in range(0, TILE_HEIGHT * 3, TILE_HEIGHT):
            wall = arcade.Sprite(filename="./resources/terrain/rock/rock1.png", scale=1)
            wall.center_x = x + (wall.width // 2)
            wall.center_y = y + (wall.height // 2)
            terrain_list.append(wall)
    return terrain_list
