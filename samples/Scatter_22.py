# Модуль Scatter_22.py
from kivy.app import App
from kivy.lang import Builder
KV = '''
<Picture@Scatter>:
    source: None
    size: image.size
    size_hint: None, None
    Image:
        id: image
        source: root.source
    FloatLayout:
        Picture:
            source: './Images/Dog.jpg'
        Picture:
            source: './Images/forest.jpg'
        Picture:
            source: './Images/Elena.jpg'
'''
class MyApp(App):
    def build(self):
        return Builder.load_string(KV)
MyApp().run()
# ВНИМАНИЕ! Код не работает (он неправильный). Искать ошибку в чужом коде лишь на этапе изучения фреймворка я не буду.