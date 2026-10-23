from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Line
from kivy.core.window import Window


class CarromBoard(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.draw_board, pos=self.draw_board)

    def draw_board(self, *args):
        self.canvas.clear()

        w, h = self.width, self.height
        if w <= 0 or h <= 0:
            return

        with self.canvas:
            Color(0.88, 0.72, 0.48, 1)
            Line(rectangle=(self.x + 12, self.y + 12,
                            w - 24, h - 24), width=4)

            # Four pockets
            pocket = min(w, h) * 0.045
            Color(0.08, 0.06, 0.04, 1)
            for px, py in [
                (self.x + 25, self.y + 25),
                (self.right - 25, self.y + 25),
                (self.x + 25, self.top - 25),
                (self.right - 25, self.top - 25)
            ]:
                Ellipse(pos=(px - pocket, py - pocket),
                        size=(pocket * 2, pocket * 2))

            # Striker and target
            sx, sy = self.center_x - 55, self.center_y - 65
            tx, ty = self.center_x + 35, self.center_y + 40

            Color(0.1, 0.35, 1, 1)
            Ellipse(pos=(sx - 16, sy - 16), size=(32, 32))

            Color(0.95, 0.12, 0.12, 1)
            Ellipse(pos=(tx - 12, ty - 12), size=(24, 24))

            # Aim line
            Color(0.1, 0.35, 1, 1)
            Line(points=[sx, sy, tx, ty], width=2)

            # Approximate collision direction
            Color(0.1, 0.8, 0.25, 1)
            Line(points=[tx, ty, tx + 85, ty + 85], width=2)

            # Pocket direction
            Color(1, 0.85, 0.05, 1)
            Line(points=[tx, ty, self.right - 25,
                         self.top - 25], width=2)


class CarromAimApp(App):
    def build(self):
        Window.clearcolor = (0.12, 0.12, 0.12, 1)
        root = Widget()
        board = CarromBoard(size_hint=(1, 1))
        root.add_widget(board)

        title = Label(
            text="Carrom Aim Line Demo",
            size_hint=(1, None),
            height=45,
            pos_hint={"top": 1}
        )
        root.add_widget(title)
        return root


if __name__ == "__main__":
    CarromAimApp().run()
