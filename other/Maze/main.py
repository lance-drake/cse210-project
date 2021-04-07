import arcade
import WorldGeneration
import random
class MyGame(arcade.Window):
    def __init__(self, width, height, title, bg_color):
        super().__init__(width, height, title)
        arcade.set_background_color(bg_color)
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 900
        self.SCREEN_TITLE = "GAME"
        self.MAZE_LENGTH = 15
        self.worldGen = WorldGeneration.World(self.MAZE_LENGTH, random.randint(0,10000))

    def newScreen(self):
        self.worldGen = WorldGeneration.World(self.MAZE_LENGTH, random.randint(0,10000))
        self.worldGen.generateTiles()
        running = True
        while(running):
            running = not self.worldGen.walkThroughWorld()

    def on_key_press(self, key, modifiers):
        print("Key pressed!")
        if key == arcade.key.R:
            self.newScreen()

    def on_draw(self):

        arcade.start_render()

        tiles = self.worldGen.getTiles()
        for y in range(len(tiles)):
            for x in range(len(tiles[y])):
                tile = tiles[y][x]
                tileX = tile.position.getX()
                tileY = tile.position.getY()
                tile_width = self.SCREEN_WIDTH/self.MAZE_LENGTH
                tile_height = self.SCREEN_HEIGHT/self.MAZE_LENGTH

                if(tile.walls[0]):
                    arcade.draw_line(tileX*tile_width, tileY*tile_height, tileX*tile_width, (tileY*tile_height) + tile_height, arcade.color.BLACK)
                    #arcade.draw_text("Wall",((tileX*tile_width)+(tileX*tile_width))/2 + 40, (( tileY*tile_height)+((tileY*tile_height) + tile_height))/2, arcade.color.GREEN)

                if(tile.walls[1]):
                    arcade.draw_line(tileX*tile_width, tileY*tile_height + tile_height, (tileX*tile_width) +  tile_width, tileY*tile_height + tile_height, arcade.color.BLACK)
                    #arcade.draw_text("Wall",((tileX*tile_width)+((tileX*tile_width) +  tile_width))/2, ((tileY*tile_height + tile_height)+(tileY*tile_height + tile_height))/2 -40, arcade.color.GREEN)

                if(tile.walls[2]):
                    arcade.draw_line(tileX*tile_width + tile_width, tileY*tile_height, tileX*tile_width + tile_width, (tileY*tile_height) + tile_height, arcade.color.BLACK)
                    #arcade.draw_text("Wall",((tileX*tile_width + tile_width)+(tileX*tile_width + tile_width))/2 - 40, ((tileY*tile_height)+((tileY*tile_height) + tile_height))/2, arcade.color.GREEN)

                if(tile.walls[3]):
                    arcade.draw_line(tileX*tile_width, tileY*tile_height, (tileX*tile_width) + tile_width, tileY*tile_height, arcade.color.BLACK)
                    #arcade.draw_text("Wall",((tileX*tile_width)+((tileX*tile_width) + tile_width))/2, ((tileY*tile_height)+(tileY*tile_height))/2 + 40, arcade.color.GREEN)

def main():
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 900
    SCREEN_TITLE = "GAME"

    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, arcade.color.WHITE)
    game.newScreen()
    arcade.run()

if __name__ == "__main__":
    main()