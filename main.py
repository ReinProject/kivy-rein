from kivy.app import App
from kivy.lang import Builder

class ReinAndroidApp(App):
    def build(self):
        view = Builder.load_file('main.kv')
        return view

    def on_pause(self):
        pass
    
    def on_resume(self):
        pass

if __name__ == '__main__':
    ReinAndroidApp().run()
