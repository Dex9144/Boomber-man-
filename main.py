import arcade

SCREEN_WIDTH = 660
SCREEN_HEIGHT = 660
SCREEN_TITLE = "Bomberman"


class Game(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.setup()

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

arcade.run()
