# Модуль Carousel_2.py
from kivy.lang import Builder
from kivy.app import App
KV = '''
Carousel:
    direction: 'right'
    canvas:
        Color:
            rgba: 0, 1, 0, 1
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        Image:
            source: './Images/Fon2.jpg'
    BoxLayout:
        Image:
            source: './Images/Elena.jpg'
    BoxLayout:
        Image:
            source: './Images/Dog.jpg'
    BoxLayout:
        Image:
            source: './Images/Elena.jpg'
'''
class MainApp(App):
    def build(self):
        return Builder.load_string(KV)
MainApp().run()