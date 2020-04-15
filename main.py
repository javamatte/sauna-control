from kivy.app import App
from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

class SaunaDisplay(Widget):
    temp_set = NumericProperty(0)
    temp_current = NumericProperty(0)


class SaunaApp(App):

    def build(self):
        display = SaunaDisplay()
        return display


if __name__ == '__main__':
    SaunaApp().run()