from kivy.app import App
from kivy.lang import Builder

from functionality.Setting import Setting

class ReinAndroidApp(App):
    def build(self):
    	if not Setting.read('delprivkey'):
        	view = Builder.load_file('views\sign-in.kv')

        else:
        	view = Builder.load_file('views\main.kv')

        return view

    def on_pause(self):
        pass
    
    def on_resume(self):
        pass

if __name__ == '__main__':
    ReinAndroidApp().run()
