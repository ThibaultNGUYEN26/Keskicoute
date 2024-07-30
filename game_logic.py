import random

class GameLogic:
	CHAR_LIMIT = 10
	USERNAME_CHAR_LIMIT = 15

	def __init__(self, ui):
		self.ui = ui
		self.init_game_variables()
		self.max_price = 0

	def init_game_variables(self):
		self.player1_calculated = False
		self.player2_calculated = False
		self.player1_score = 0
		self.player2_score = 0
		self.price = 0

	def set_difficulty(self, level):
		if level == 1:
			self.max_price = 100
		elif level == 2:
			self.max_price = 1000
		elif level == 3:
			self.max_price = 100000
		else:
			self.max_price = 1000000
		self.price = self.random_price(self.max_price)

	def random_price(self, max_price):
		return round(random.uniform(5, max_price), 2)

	def calculate_score(self, entries, player):
		try:
			values = [float(entry.get()) if entry.get() else 0 for entry in entries]
			score = sum(values)
			if player == "Player 1":
				self.player1_score = score
				self.player1_calculated = True
				self.ui.calculate_button1.configure(text="Calculated")
			else:
				self.player2_score = score
				self.player2_calculated = True
				self.ui.calculate_button2.configure(text="Calculated")
			self.check_calculations()
		except ValueError:
			print(f"Please enter valid float values for {player}")

	def check_calculations(self):
		if self.player1_calculated and self.player2_calculated:
			self.ui.display_results()

	def get_results(self):
		diff_player1 = abs(self.player1_score - self.price)
		diff_player2 = abs(self.player2_score - self.price)

		if diff_player1 < diff_player2:
			winner = self.ui.player1_name
		elif diff_player2 < diff_player1:
			winner = self.ui.player2_name
		else:
			winner = "Draw"

		return diff_player1, diff_player2, winner
