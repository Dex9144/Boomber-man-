import arcade

SCREEN_WIDTH = 660
SCREEN_HEIGHT = 660
SCREEN_TITLE = "Bomberman"


"""Bg settings"""
CELL_WIDTH = 60
CELL_HEIGHT = 60

ROW_COUNT = 11
COL_COUNT = 11


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

        self.bg = arcade.load_texture("Blocks/BackgroundTile.png")

    def setup(self):
        pass

    def on_draw(self):
        self.clear()
        self.draw_background()


    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass

    def draw_background(self):
        for y in range(ROW_COUNT):
            for x in range(COL_COUNT):
                arcade.draw_texture_rectangle()

window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()
