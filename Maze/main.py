import arcade
import WorldGeneration

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
SCREEN_TITLE = "GAME"
worldGen = WorldGeneration.World()

def main():
    

    worldGen.create_building(15)
    # Open up our window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.set_background_color(arcade.color.WHITE)

    # Tell the computer to call the draw command at the specified interval.
    arcade.schedule(on_draw, 1 / 80)

    # Run the program
    arcade.run()


def on_draw(delta_time):
    for i in range(len(worldGen.getBuildings())):
        arcade.draw_rectangle_filled(
            worldGen.getBuildings()[i].getX(), 
            worldGen.getBuildings()[i].getY(), 
            worldGen.getBuildings()[i].getWidth(), 
            worldGen.getBuildings()[i].getHeight(), 
            arcade.color.YELLOW)
if __name__ == "__main__":
    main()