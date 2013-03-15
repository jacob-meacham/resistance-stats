from app import app, db
from flask import render_template, flash, redirect, session, url_for, request

@app.route('/')
def index():
	return render_template('index.html')