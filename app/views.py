from app import app, db
from flask import render_template, flash, redirect, session, url_for, request
from datetime import datetime
import stats
from stats import Player, Game, overall_stats

@app.route('/games/')
def games():
	pass

@app.route('/leaderboards/')
def leaderboards():
	pass

@app.route('/search/')
def search():
	pass

@app.route('/')
def index():
	games = Game.query.order_by(Game.date).all()
	players = Player.query.all()

	overall_stats = stats.overall_stats(games)

	return render_template('index.html',
		overall_stats=overall_stats,
		games=games,
		players=players)