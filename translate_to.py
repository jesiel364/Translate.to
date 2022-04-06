from kivymd.app import MDApp
from kivy.core.window import Window
from translate import Translator
from time import sleep
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.boxlayout import MDBoxLayout

Window.size = 300, 500

class ContentNavigationDrawer(MDBoxLayout):
    pass

class translate_to(MDApp):
	def __init__(self, **kwargs):
		super(translate_to, self).__init__(**kwargs)

		menu_items = [{
		'viewclass': 'OneLineListItem',
		'text': 'Abrir',
		'on_release': lambda: print('Novo')
		},
		{'viewclass': 'OneLineListItem',
		'text': 'Novo',
		'on_release': lambda: print('Abrir')
		},
		{'viewclass': 'OneLineListItem',
		'text': 'Recentes',
		'on_release': lambda: print('Recentes')}]
		self.menu = MDDropdownMenu(
			items= menu_items,
			width_mult = 2.5)

	def callback_menu(self, button):
		self.menu.caller = button
		self.menu.open()

	



	def translate(self):
		
		
		print('Status: Rodando...')
		txt = self.root.ids.txt.text
		lbl = self.root.ids.label
		
		a = self.root.ids.spin.active = True
		
		try:
			def __init__(a):
				return a

				
			s = Translator(from_lang = 'pt-br', to_lang = 'english')
			res = s.translate(txt)
			print(res)
			lbl.text = res
			self.root.ids.spin.active = False
		except Exception as e:
			print(e)
			lbl.text = 'Não foi possivel traduzir o texto'

		

	def save_text(self):
		label = self.root.ids.label.text

		try:
			with open('file.txt', 'a') as f:
				f.write(f'{label}\n')
				f.close()
				print('Arquivo \"file.txt\" salvo!\n')
		except Exception as e:
			print(e)
			print('Ñão foi possivel salvar o arquivo')

	


translate_to().run()