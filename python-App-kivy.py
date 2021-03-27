import kivy
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class SpartanGrid(GridLayout):
    def __init__(self,**kwargs):
        super(SpartanGrid, self).__init__()
        self.cols =  2
        self.add_widget(Label(text="Student Name: "))
        self.s_name = TextInput(multiline=True)
        self.add_widget(self.s_name)

        self.add_widget(Label(text="Student Marks"))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text="Submit")
        self.press.bind(on_press=self.sub_btn)
        self.add_widget(self.press)

    def sub_btn(self,instance):
        print("Name of Student: "+self.s_name.text)
        print("Marks of Student: "+self.s_marks.text)
        print("Gender of Student: "+self.s_gender.text)


class SpartanApp(App):
    def build(self):
        return SpartanGrid()


if __name__ == "__main__":
    SpartanApp().run()


