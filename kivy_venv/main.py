from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from random import random
from kivy.core.window import Window


class PainterWidget(Widget):
    def __init__(self,**kw):
        super(PainterWidget, self).__init__(**kw)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(),random(),random(),1)
            rad=40
            Ellipse(pos=(touch.x-rad/2,touch.y-rad/2),size=(rad,rad))
            touch.ud['c'] = Line(points=(touch.x, touch.y), width=20)

    def on_touch_move(self, touch):
        touch.ud['c'].points+=(touch.x,touch.y)

class PaintApp(App):
    def build(self):
        pa=Widget()
        self.p=PainterWidget()
        pa.add_widget(self.p)
        pa.add_widget(Button(text='Clear', on_press=self.clearp))
        pa.add_widget(Button(text='Save', on_press=self.save,pos=(100,0)))




        return pa

    def clearp(self,instance):
        self.p.canvas.clear()

    def save(self,instance):
        self.p.size=(Window.size[0],Window.size[1])
        self.p.export_to_png('eee.png')

if __name__ == "__main__":
	PaintApp().run()