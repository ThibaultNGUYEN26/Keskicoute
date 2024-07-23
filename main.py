from tkinter import Tk, Frame, Button, Label, CENTER, Entry, StringVar
import random

CHAR_LIMIT = 15

def random_price():
	return round(random.uniform(5, 1000000), 2)

class Keskicoute:

	def display_player2_input(self):
		self.player1_button.place_forget()
		self.player1_input.place_forget()
		self.player1_label.place_forget()
		self.player2_label.place(relx=0.5, rely=0.4, anchor=CENTER)
		self.player2_input.place(relx=0.5, rely=0.5, anchor=CENTER)
		self.player2_input.focus()
		self.toggle_player2_button()

	def calculate_player1(self):
		entries = [self.player1_input1.get(), self.player1_input2.get(), self.player1_input3.get(), self.player1_input4.get()]
		try:
			values = [float(entry) if entry else 0 for entry in entries]
			total = sum(values)
			print(f"Player 1 total: {total}")
			self.player1_calculated = True
			self.check_calculations()
		except ValueError:
			print("Please enter valid float values for Player 1")

	def calculate_player2(self):
		entries = [self.player2_input1.get(), self.player2_input2.get(), self.player2_input3.get(), self.player2_input4.get()]
		try:
			values = [float(entry) if entry else 0 for entry in entries]
			total = sum(values)
			print(f"Player 2 total: {total}")
			self.player2_calculated = True
			self.check_calculations()
		except ValueError:
			print("Please enter valid float values for Player 2")

	def check_calculations(self):
		if self.player1_calculated and self.player2_calculated:
			print("Both players have calculated their totals")

	def display_game_frame(self):
		self.main_frame.place_forget()
		self.game_frame.place(x=0, y=0)

		player1_name = self.str1.get()
		player2_name = self.str2.get()

		self.player1_display = Label(self.game_frame, text=f"{player1_name}", fg="white", bg="black", font=("Futura", 17))
		self.player1_display.place(relx=0.2, rely=0.3, anchor=CENTER)
		
		self.player2_display = Label(self.game_frame, text=f"{player2_name}", fg="white", bg="black", font=("Futura", 17))
		self.player2_display.place(relx=0.8, rely=0.3, anchor=CENTER)

		validate_float_cmd = self.root.register(self.validate_float)

		self.player1_input1 = Entry(self.game_frame, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_float_cmd, '%P'))
		self.player1_input1.place(relx=0.2, rely=0.4, anchor=CENTER)
		
		self.player1_input2 = Entry(self.game_frame, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_float_cmd, '%P'))
		self.player1_input2.place(relx=0.2, rely=0.5, anchor=CENTER)
		
		self.player1_input3 = Entry(self.game_frame, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_float_cmd, '%P'))
		self.player1_input3.place(relx=0.2, rely=0.6, anchor=CENTER)
		
		self.player1_input4 = Entry(self.game_frame, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_float_cmd, '%P'))
		self.player1_input4.place(relx=0.2, rely=0.7, anchor=CENTER)

		self.player2_input1 = Entry(self.game_frame, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_float_cmd, '%P'))
		self.player2_input1.place(relx=0.8, rely=0.4, anchor=CENTER)
		
		self.player2_input2 = Entry(self.game_frame, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_float_cmd, '%P'))
		self.player2_input2.place(relx=0.8, rely=0.5, anchor=CENTER)
		
		self.player2_input3 = Entry(self.game_frame, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_float_cmd, '%P'))
		self.player2_input3.place(relx=0.8, rely=0.6, anchor=CENTER)
		
		self.player2_input4 = Entry(self.game_frame, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_float_cmd, '%P'))
		self.player2_input4.place(relx=0.8, rely=0.7, anchor=CENTER)

		self.calculate_button1 = Button(self.game_frame, text="Calculate", command=self.calculate_player1, font=("Futura 15"))
		self.calculate_button1.place(relx=0.2, rely=0.8, anchor=CENTER)

		self.calculate_button2 = Button(self.game_frame, text="Calculate", command=self.calculate_player2, font=("Futura 15"))
		self.calculate_button2.place(relx=0.8, rely=0.8, anchor=CENTER)

	def validate_length(self, new_value):
		return len(new_value) <= CHAR_LIMIT

	def validate_float(self, new_value):
		if new_value == "" or new_value == ".":
			return True
		try:
			float(new_value)
			if '.' in new_value:
				decimal_part = new_value.split('.')[1]
				if len(decimal_part) > 2:
					return False
			return True
		except ValueError:
			return False

	def toggle_player1_button(self, *args):
		if self.str1.get():
			self.player1_button.place(relx=0.5, rely=0.6, anchor=CENTER)
		else:
			self.player1_button.place_forget()

	def toggle_player2_button(self, *args):
		if self.str2.get():
			self.player2_button.place(relx=0.5, rely=0.6, anchor=CENTER)
		else:
			self.player2_button.place_forget()
	
	def handle_enter_key(self, event):
		if self.player1_input.winfo_ismapped() and self.str1.get():
			self.display_player2_input()
		elif self.player2_input.winfo_ismapped() and self.str2.get():
			self.display_game_frame()

	def exit_win(self, event=None):
		self.root.destroy()

	def __init__(self, root):
		""" ---------- [ ROOT SETUP ] ---------- """
		self.width = 800
		self.height = 600
		self.root = root
		self.root.title("Keskicoute")
		self.root.geometry(f"{self.width}x{self.height}")
		self.root.configure(bg="black")
		self.player1_calculated = False
		self.player2_calculated = False

		""" ---------- [ MAIN FRAME ] ---------- """
		self.main_frame = Frame(self.root, bg="black", width=self.width, height=self.height)
		self.main_frame.place(x=0, y=0)

		self.player1_label = Label(self.main_frame, text="Player 1", bg="black", fg="white", font=("Futura 20 bold"))
		self.player1_label.place(relx=0.5, rely=0.4, anchor=CENTER)

		self.str1 = StringVar()
		validate_cmd = self.root.register(self.validate_length)
		self.player1_input = Entry(self.main_frame, textvariable=self.str1, width=int(self.width / 40), font=("Futura 15 bold"), justify="center", validate="key", validatecommand=(validate_cmd, '%P'))
		self.player1_input.place(relx=0.5, rely=0.5, anchor=CENTER)
		self.player1_input.focus()

		def on_player1_entry_change(*args):
			self.str1.set(self.str1.get().upper())
			self.toggle_player1_button()

		self.str1.trace('w', on_player1_entry_change)

		self.player1_button = Button(self.main_frame, command=self.display_player2_input, bg="black", fg="white", text="Enter", font=("Futura", 15))

		self.player2_label = Label(self.main_frame, text="Player 2", bg="black", fg="white", font=("Futura 20 bold"))

		self.str2 = StringVar()
		validate_cmd = self.root.register(self.validate_length)
		self.player2_input = Entry(self.main_frame, textvariable=self.str2, width=int(self.width / 40), font=("Futura 15 bold"), justify="center", validate="key", validatecommand=(validate_cmd, '%P'))

		def on_player2_entry_change(*args):
			self.str2.set(self.str2.get().upper())
			self.toggle_player2_button()

		self.str2.trace('w', on_player2_entry_change)

		self.player2_button = Button(self.main_frame, command=self.display_game_frame, bg="black", fg="white", text="Play", font=("Futura", 15))

		""" ---------- [ GAME FRAME ] ---------- """
		self.game_frame = Frame(self.root, bg="black", width=self.width, height=self.height)

		self.to_find = Label(self.game_frame, text="Total to find:", fg="white", bg="black", font=("Futura", 20, 'bold'))
		self.to_find.place(relx=0.5, rely=0.1, anchor=CENTER)

		self.price = random_price()
		self.price_to_find = Label(self.game_frame, text=f"{self.price}€", fg="white", bg="black", font=("Futura", 17, 'bold'))
		self.price_to_find.place(relx=0.5, rely=0.18, anchor=CENTER)

		""" ---------- [ KEY BIND ] ---------- """
		self.root.bind('<Escape>', self.exit_win)
		self.root.bind('<Return>', self.handle_enter_key)

if __name__ == "__main__":
	root = Tk()
	app = Keskicoute(root)
	root.mainloop()
