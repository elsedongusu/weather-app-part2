from kivy.app import App
from kivy.config import Config
from kivy.core.text import LabelBase
fontfile="byom_icon.ttf"
Config.set("graphics","width","400")
Config.set("graphics","height","700")
class ElseDongusuApp(App):
    pass
if __name__ == '__main__':
    LabelBase.register(name="mFont",fn_regular=fontfile)
    ElseDongusuApp().run()