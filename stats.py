from app import app, db
import datetime

player_game_table = db.Table('player_game',
	db.Column('player_id', db.Integer, db.ForeignKey('player.id')),
	db.Column('game_id', db.Integer, db.ForeignKey('game.id')))

class Player(db.Model):
	__tablename__ = 'player'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	spy_wins = db.Column(db.Integer)
	spy_losses = db.Column(db.Integer)
	resistance_wins = db.Column(db.Integer)
	resistance_losses = db.Column(db.Integer)

	def __init__(self, name):
		self.name = name
		spy_wins = 0
		spy_losses = 0
		resistance_wins = 0
		resistance_losses = 0

	games = db.relationship("Game",
		secondary=player_game_table,
		backref="players")

class Game(db.Model):
	__tablename__ = 'game'

	id = db.Column(db.Integer, primary_key=True)
	num_players = db.Column(db.Integer)
	date = db.Column(db.Date)
	resistance_rounds = db.Column(db.Integer)
	spy_rounds = db.Column(db.Integer)