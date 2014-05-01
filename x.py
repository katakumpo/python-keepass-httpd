import kivy
kivy.require("1.8.0")

from kivy.app import App
from kivy.uix.button import Button

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
#Builder.load_file("/home/kiwisauce/devel/workspace/bla.git/file.kv")

from kivy.logger import Logger

class Calc(BoxLayout):
    pass

class TestApp(App):
    def build(self):
        return Calc()

    def store_passphrase(self, x):
        self._pass = x

    def get_passphrase(self):
        return self._pass

    def __init__(self, *args, **kwargs):
        super(TestApp, self).__init__(*args, **kwargs)
        self._pass = None


from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '130')


if __name__ == '__main__':
    from kivy.interactive import InteractiveLauncher
    x = InteractiveLauncher(TestApp())
    x.run()
    print "ssss", x.get_passphrase()