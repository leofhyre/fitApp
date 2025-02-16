import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout


class ChildApp(GridLayout):
    def __init__(self, **kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2

        self.add_widget(Label(text='Student Name'))
        self.s_name = TextInput()
        self.add_widget(self.s_name)

        self.add_widget(Label(text='Student Marks'))
        self.s_marks = TextInput()
        self.add_widget(self.s_marks)

        self.add_widget(Label(text='Student Gender'))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

        self.press = Button(text='Click me')
        self.press.bind(on_press=self.show_popup)
        self.add_widget(self.press)

    def show_popup(self, instance):
        # Message content
        message = (f"Name of Student: {self.s_name.text}\n"
                   f"Marks of Student: {self.s_marks.text}\n"
                   f"Gender of Student: {self.s_gender.text}")

        # Popup layout
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        label = Label(text=message)
        close_button = Button(text='Close', size_hint=(None, None), size=(100, 40))

        # Popup window
        popup = Popup(title='Student Information',
                      content=layout,
                      size_hint=(None, None),
                      size=(300, 200),
                      auto_dismiss=False)

        # Close button action
        close_button.bind(on_press=popup.dismiss)

        # Add widgets to the layout
        layout.add_widget(label)
        layout.add_widget(close_button)

        # Open popup
        popup.open()


class ParentApp(App):
    def build(self):
        return ChildApp()


if __name__ == "__main__":
    ParentApp().run()