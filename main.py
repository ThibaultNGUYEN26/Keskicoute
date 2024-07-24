from tkinter import Tk, Frame, Button, Label, Entry, StringVar
import random

CHAR_LIMIT = 10
USERNAME_CHAR_LIMIT = 15

def random_price():
	return round(random.uniform(5, 1000000), 2)

class Keskicoute:
	def __init__(self, root):
		""" ---------- [ ROOT SETUP ] ---------- """
		self.root = root
		self.width = 800
		self.height = 600
		self.root.title("Keskicoute")
		self.root.geometry(f"{self.width}x{self.height}")
		self.root.configure(bg="black")
		self.init_game_variables()

		""" ---------- [ MAIN FRAME SETUP ] ---------- """
		self.setup_main_frame()
		
		""" ---------- [ GAME FRAME SETUP ] ---------- """
		self.setup_game_frame()

		""" ---------- [ KEY BINDINGS ] ---------- """
		self.root.bind('<Escape>', self.exit_win)
		self.root.bind('<Return>', self.handle_enter_key)

	def init_game_variables(self):
		self.player1_calculated = False
		self.player2_calculated = False
		self.player1_score = 0
		self.player2_score = 0
		self.price = random_price()

	def setup_main_frame(self):
		self.main_frame = Frame(self.root, bg="black", width=self.width, height=self.height)
		self.main_frame.place(x=0, y=0)

		self.str1 = StringVar()
		self.player1_label = Label(self.main_frame, text="Player 1", bg="black", fg="white", font=("Futura 20 bold"))
		self.player1_label.place(relx=0.5, rely=0.4, anchor="center")

		self.player1_input = Entry(self.main_frame, textvariable=self.str1, width=int(self.width / 40), font=("Futura 15 bold"), justify="center", validate="key", validatecommand=(self.root.register(self.validate_length), '%P'))
		self.player1_input.place(relx=0.5, rely=0.5, anchor="center")
		self.player1_input.focus()
		self.str1.trace('w', self.on_player1_entry_change)

		self.player1_button = Button(self.main_frame, command=self.display_player2_input, bg="black", fg="white", text="Enter", font=("Futura", 15))

		self.str2 = StringVar()
		self.player2_label = Label(self.main_frame, text="Player 2", bg="black", fg="white", font=("Futura 20 bold"))

		self.player2_input = Entry(self.main_frame, textvariable=self.str2, width=int(self.width / 40), font=("Futura 15 bold"), justify="center", validate="key", validatecommand=(self.root.register(self.validate_length), '%P'))
		self.str2.trace('w', self.on_player2_entry_change)

		self.player2_button = Button(self.main_frame, command=self.display_game_frame, bg="black", fg="white", text="Play", font=("Futura", 15))

	def setup_game_frame(self):
		self.game_frame = Frame(self.root, bg="black", width=self.width, height=self.height)

		self.to_find = Label(self.game_frame, text="Total to find:", fg="white", bg="black", font=("Futura", 20, 'bold'))
		self.to_find.place(relx=0.5, rely=0.1, anchor="center")

		self.price_to_find = Label(self.game_frame, text=f"{self.price}€", fg="white", bg="black", font=("Futura", 17, 'bold'))
		self.price_to_find.place(relx=0.5, rely=0.18, anchor="center")

	def on_player1_entry_change(self, *args):
		self.str1.set(self.str1.get().upper())
		self.toggle_player1_button()

	def on_player2_entry_change(self, *args):
		self.str2.set(self.str2.get().upper())
		self.toggle_player2_button()

	def display_player2_input(self):
		self.player1_label.place_forget()
		self.player1_input.place_forget()
		self.player1_button.place_forget()

		self.player2_label.place(relx=0.5, rely=0.4, anchor="center")
		self.player2_input.place(relx=0.5, rely=0.5, anchor="center")
		self.player2_input.focus()

	def display_game_frame(self):
		self.main_frame.place_forget()
		self.game_frame.place(x=0, y=0)

		self.player1_name = self.str1.get()
		self.player2_name = self.str2.get()

		self.player1_display = Label(self.game_frame, text=f"{self.player1_name}", fg="white", bg="black", font=("Futura", 17))
		self.player1_display.place(relx=0.2, rely=0.3, anchor="center")

		self.player2_display = Label(self.game_frame, text=f"{self.player2_name}", fg="white", bg="black", font=("Futura", 17))
		self.player2_display.place(relx=0.8, rely=0.3, anchor="center")

		self.setup_player_inputs()

	def setup_player_inputs(self):
		validate_float_cmd = self.root.register(self.validate_float)

		self.player1_input1 = self.create_input(self.game_frame, 0.2, 0.4, validate_float_cmd)
		self.player1_input2 = self.create_input(self.game_frame, 0.2, 0.5, validate_float_cmd)
		self.player1_input3 = self.create_input(self.game_frame, 0.2, 0.6, validate_float_cmd)
		self.player1_input4 = self.create_input(self.game_frame, 0.2, 0.7, validate_float_cmd)

		self.player2_input1 = self.create_input(self.game_frame, 0.8, 0.4, validate_float_cmd)
		self.player2_input2 = self.create_input(self.game_frame, 0.8, 0.5, validate_float_cmd)
		self.player2_input3 = self.create_input(self.game_frame, 0.8, 0.6, validate_float_cmd)
		self.player2_input4 = self.create_input(self.game_frame, 0.8, 0.7, validate_float_cmd)

		self.calculate_button1 = Button(self.game_frame, text="Calculate", command=self.calculate_player1, font=("Futura 15"))
		self.calculate_button2 = Button(self.game_frame, text="Calculate", command=self.calculate_player2, font=("Futura 15"))

	def create_input(self, parent, relx, rely, validate_cmd):
		input_field = Entry(parent, bg="black", fg="white", justify="center", validate="key", validatecommand=(validate_cmd, '%P'))
		input_field.place(relx=relx, rely=rely, anchor="center")
		input_field.bind('<KeyRelease>', self.check_entries)
		return input_field

	def check_entries(self, event):
		self.toggle_calculate_button(self.player1_input1, self.player1_input2, self.player1_input3, self.player1_input4, self.calculate_button1, 0.2)
		self.toggle_calculate_button(self.player2_input1, self.player2_input2, self.player2_input3, self.player2_input4, self.calculate_button2, 0.8)

	def toggle_calculate_button(self, *args):
		inputs = args[:4]
		button = args[4]
		relx = args[5]
		if any(input_field.get() for input_field in inputs):
			button.place(relx=relx, rely=0.8, anchor="center")
		else:
			button.place_forget()

	def calculate_player1(self):
		self.calculate_score([self.player1_input1, self.player1_input2, self.player1_input3, self.player1_input4], "Player 1")

	def calculate_player2(self):
		self.calculate_score([self.player2_input1, self.player2_input2, self.player2_input3, self.player2_input4], "Player 2")

	def calculate_score(self, entries, player):
		try:
			values = [float(entry.get()) if entry.get() else 0 for entry in entries]
			score = sum(values)
			if player == "Player 1":
				self.player1_score = score
				self.player1_calculated = True
				self.calculate_button1.configure(text="Calculated")
			else:
				self.player2_score = score
				self.player2_calculated = True
				self.calculate_button2.configure(text="Calculated")
			self.check_calculations()
		except ValueError:
			print(f"Please enter valid float values for {player}")

	def check_calculations(self):
		if self.player1_calculated and self.player2_calculated:
			self.display_results()

	def display_results(self):
		diff_player1 = abs(self.player1_score - self.price)
		diff_player2 = abs(self.player2_score - self.price)

		if diff_player1 < diff_player2:
			winner = self.player1_name
		elif diff_player2 < diff_player1:
			winner = self.player2_name
		else:
			winner = "Draw"

		self.total_player1 = Label(self.game_frame, text=f"total: {self.player1_score}€", fg="white", bg="black", font=("Futura 18 bold"))
		self.total_player1.place(relx=0.2, rely=0.8, anchor="center")

		self.total_player2 = Label(self.game_frame, text=f"total: {self.player2_score}€", fg="white", bg="black", font=("Futura 18 bold"))
		self.total_player2.place(relx=0.8, rely=0.8, anchor="center")

		self.winner_label = Label(self.game_frame, text=winner, fg="white", bg="black", font=("Futura 20 bold"))
		self.winner_label.place(relx=0.5, rely=0.5, anchor="center")

		self.won_label = Label(self.game_frame, text="Win", fg="white", bg="black", font=("Futura 20 bold"))
		self.won_label.place(relx=0.5, rely=0.57, anchor="center")

		self.replay_button = Button(self.game_frame, text="Replay", command=self.replay_game, font=("Futura 20 bold"))
		self.replay_button.place(relx=0.5, rely=0.8, anchor="center")

		self.calculate_button1.place_forget()
		self.calculate_button2.place_forget()

	def replay_game(self):
		self.init_game_variables()
		self.total_player1.place_forget()
		self.total_player2.place_forget()
		self.winner_label.place_forget()
		self.won_label.place_forget()
		self.replay_button.place_forget()
		self.price_to_find.configure(text=f"{self.price}€")
		self.clear_inputs([self.player1_input1, self.player1_input2, self.player1_input3, self.player1_input4])
		self.clear_inputs([self.player2_input1, self.player2_input2, self.player2_input3, self.player2_input4])
		self.calculate_button1.configure(text="Calculate")
		self.calculate_button2.configure(text="Calculate")

	def clear_inputs(self, inputs):
		for input_field in inputs:
			input_field.delete(0, 'end')

	def validate_length(self, new_value):
		return len(new_value) <= USERNAME_CHAR_LIMIT

	def validate_float(self, new_value):
		if len(new_value) > CHAR_LIMIT:
			return False
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
			self.player1_button.place(relx=0.5, rely=0.6, anchor="center")
		else:
			self.player1_button.place_forget()

	def toggle_player2_button(self, *args):
		if self.str2.get():
			self.player2_button.place(relx=0.5, rely=0.6, anchor="center")
		else:
			self.player2_button.place_forget()

	def handle_enter_key(self, event):
		if self.player1_input.winfo_ismapped() and self.str1.get():
			self.display_player2_input()
		elif self.player2_input.winfo_ismapped() and self.str2.get():
			self.display_game_frame()

	def exit_win(self, event=None):
		self.root.destroy()

if __name__ == "__main__":
	root = Tk()
	app = Keskicoute(root)
	root.mainloop()
