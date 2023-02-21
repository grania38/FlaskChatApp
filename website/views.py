from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Rooms
from flask_login import login_user, current_user, logout_user, login_required
from flask_socketio import SocketIO, send, join_room, leave_room, emit
import json
from time import localtime, strftime
views = Blueprint('views', __name__)
ROOMS = ['potterheads', 'f1', 'mcu stans', 'anything football', 'cs', 'memegrounds']
@views.route('/chat')
@login_required
def chat():
	return render_template('chat.html', user=current_user) #, roomList = ROOMS, room = 'global chat'

@views.route('/')
def home():
    return render_template("home.html", user=current_user)



