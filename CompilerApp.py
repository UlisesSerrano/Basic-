

from sys import stdin
from kivy.app import App
from kivy.uix.scrollview import ScrollView
from pygments.lexers.c_cpp import CppLexer
from kivy.uix.spinner import Spinner, SpinnerOption
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.codeinput import CodeInput
from kivy.uix.behaviors import EmacsBehavior
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.core.text import LabelBase
from pygments import lexers
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
import codecs
import os
stdoutin = ['', '', '', '']


# Mobile Code

class Fnt_SpinnerOption(SpinnerOption):
    pass


class P(FloatLayout):
    pass


class LoadDialog(Popup):
    pass

    def load(self, path, selection):
        self.choosen_file = [None, ]
        self.choosen_file = selection
        Window.title = selection[0][selection[0].rfind(os.sep) + 1:]
        print(selection[-1])
        self.code = selection[-1]
        self.current_code = open(selection[-1]).read()
        self.dismiss()

    def cancel(self):
        self.dismiss()


class SaveDialog(Popup):

    def save(self, path, selection):
        _file = codecs.open(selection, 'w', encoding='utf8')
        _file.write(self.text)
        Window.title = selection[selection.rfind(os.sep) + 1:]
        print(selection[selection.rfind(os.sep) + 1:])
        _file.close()
        self.dismiss()

    def cancel(self):
        self.dismiss()


class ScrolllabelLabel(ScrollView):
    text = StringProperty('')


class CodeInputWithBindings(EmacsBehavior, CodeInput):

    '''CodeInput with keybindings.
    To add more bindings, add the behavior before CodeInput in the class
    definition.
    '''
    pass


class CompilerApp(App):

    files = ListProperty([None, ])
    b = BoxLayout(orientation='vertical')

    def __init__(self, run_virtual_machine, clear_virtual_machine, source_code, vm_Data):
        super().__init__()
        self.run_virtual_machine = run_virtual_machine
        self.clear_virtual_machine = clear_virtual_machine
        self.current_code = open(source_code).read()
        self.vm_Data = vm_Data
        self.code = source_code

    def save_state(instruction_pointer, instruction_erorr):
        return instruction_pointer

    def build(self):
        languages = Spinner(
            text='Courier New',
            values=sorted(['CppLexer', ] + list(lexers.LEXERS.keys())))

        languages.bind(text=self.change_lang)

        menu = BoxLayout(
            size_hint_y=None,
            height='15pt')
        fnt_size = Spinner(
            text='20',
            values=list(map(str, list(range(10, 45, 5)))))
        fnt_size.bind(text=self._update_size)

        fonts = [
            file for file in LabelBase._font_dirs_files
            if file.endswith('.ttf')]

        fnt_name = Spinner(
            text='Courier New',
            option_cls=Fnt_SpinnerOption,
            values=fonts)
        fnt_name.bind(text=self._update_font)
        mnu_file = Spinner(
            text='File',
            values=('Open', 'SaveAs', 'Save', 'Close'))
        mnu_file.bind(text=self._file_menu_selected)
        key_bindings = Spinner(
            text='Key bindings',
            values=('Default key bindings', 'Emacs key bindings'))
        key_bindings.bind(text=self._bindings_selected)

        run_button = Button(text='Run')
        run_button.bind(on_press=self.compile)

        menu.add_widget(mnu_file)
        menu.add_widget(fnt_size)
        menu.add_widget(run_button)
        self.b.add_widget(menu)

        self.codeinput = CodeInputWithBindings(
            lexer=CppLexer(),
            font_size=20,
            text=self.current_code,
            key_bindings='default',
        )
        self.output = ScrolllabelLabel(
            text="SECTION: OUTPUT\n",
        )

        self.text_input_box = CodeInputWithBindings(text='', multiline=False, height='0dp')
        self.text_input_box.bind(on_text_validate=self.on_enter)
        self.text_input_box.size_hint_y = None

        self.b.add_widget(self.codeinput)
        self.b.add_widget(self.text_input_box)
        self.b.add_widget(self.output)

        return self.b

    def show_popup(Popup):
        show = P()
        popupWindow = Popup(title="PopUp Window", content=show,
                            size_hint=(None, None), size=(400, 400))

        popupWindow.open()

    def compile(self, instance):
        self.display_and_flush_everything()
        print("Running compiler...")
        print(
            f'{10*"#"} current_code {10*"#"} {self.get_code()}\n{10*"#"} end_current_code {10*"#"}')
        try:
            print ('file_name',self.code)
            _file = codecs.open(self.code, 'w', encoding='utf8')
            _file.write(self.codeinput.text)
            _file.close()
            self.clear_virtual_machine()
            self.vm_Data()

        except KeyboardInterrupt:
            return
        except BaseException as err:
            print(f"Error Caugth: {err}")
            stdoutin[2] += f"{str(err)}\n"
            self.display_and_flush_everything()

    def get_code(self):
        return self.codeinput.text

    def get_stdout(self):
        return stdoutin[1]

    def get_stdoutin(self):
        self.text_input_box.size_hint_y = 1
        value = stdoutin[0]
        stdoutin[0] = ''
        return value

    def get_stderr(self):
        return stdoutin[2]

    def display_and_flush_everything(self):
        self.display_output(self.get_stdout(), display_name='FLUSH')
        self.display_output(self.get_stderr(), display_name='FLUSH')
        stdoutin[1] = stdoutin[2] = ''
        self.output.text = '\nBasic++\n'

    def _update_size(self, instance, size):
        self.codeinput.font_size = float(size)
        self.output.font_size = float(size)
        self.text_input_box.font_size = float(size)

    def _update_font(self, instance, fnt_name):
        instance.font_name = self.codeinput.font_name = self.output_box.font_name = fnt_name

    def on_enter(self, instance):
        # puedo agregar una condicion en la cual me condicione a que haya corrido el compilador para impirmir algo en kivy
        self.stdin = instance.text
        stdoutin[0] = self.stdin
        self.text_input_box.size_hint_y = None
        self.text_input_box.height = '0dp'
        self.text_input_box.text = ''
        self.run_virtual_machine()

    def display_output(self, message, display_name='STDOUT'):
        output = f'{message}'
        self.output.text += output
        if display_name == 'VM':
            self.output.text += '\n'
        print(f'{display_name}: {output}')

    def _file_menu_selected(self, instance, value):
        if value == 'File':
            return
        instance.text = 'File'
        if value == 'Open':
            if not hasattr(self, 'load_dialog'):
                self.load_dialog = LoadDialog()
            self.load_dialog.open()
            self.load_dialog.bind(choosen_file=self.setter('files'))
        elif value == 'SaveAs':
            if not hasattr(self, 'saveas_dialog'):
                self.saveas_dialog = SaveDialog()
            self.saveas_dialog.text = self.codeinput.text
            self.saveas_dialog.open()
        elif value == 'Save':
            if self.files[0]:
                _file = codecs.open(self.files[0], 'w', encoding='utf8')
                print(self.files[0])
                _file.write(self.codeinput.text)
                _file.close()
        elif value == 'Close':
            if self.files[0]:
                self.codeinput.text = ''
                Window.title = 'untitled'

    def _bindings_selected(self, instance, value):
        value = value.split(' ')[0]
        self.codeinput.key_bindings = value.lower()

    def on_files(self, instance, values):
        if not values[0]:
            return
        _file = codecs.open(values[0], 'r', encoding='utf8')
        self.codeinput.text = _file.read()
        _file.close()

    def change_lang(self, instance, z):
        if z == 'CppLexer':
            lx = CppLexer()
        else:
            lx = lexers.get_lexer_by_name(lexers.LEXERS[z][2][0])
        self.codeinput.lexer = lx


if __name__ == '__main__':
    CompilerApp().run()
