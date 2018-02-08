#coding=utf-8 
from kivy.app import App
from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.dropdown import DropDown
from kivy.properties import NumericProperty,StringProperty

class Quant_Select_Dropdown(DropDown):
    quant = NumericProperty(0)


class GreyHatsApp(App):
    def __init__(self):
        super(GreyHatsApp,self).__init__()
# use floatlayout for a prettier display 
    def build(self):
        layout = GridLayout(cols=1,row_force_default=True, row_default_height=30)
        label = Label(text='How many objects do you want in the scene?')
        layout.add_widget(label)
        mainbutton = Button(text='Please choose', size_hint_x=None, width=300)
        Quant_Select = Quant_Select_Dropdown()
        print Quant_Select.quant
        mainbutton.bind(on_release=Quant_Select.open)

        Quant_Select.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        layout.add_widget(mainbutton)
        return layout

if __name__ == '__main__':
    GreyHatsApp().run()

#获取另一个widget值,用kivy language  (root.label_text)
# https://stackoverflow.com/questions/30202801/how-to-access-id-widget-of-different-class-from-a-kivy-file-kv
# https://groups.google.com/forum/#!topic/kivy-users/dTuNe7Y_OpM
#显示隐藏widget内容，当判断条件为真时，再add_widget,在greyhats这个class里面新建函数，调用
