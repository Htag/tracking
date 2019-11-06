from flask import (
    Flask,
    render_template
)
import sqlite3 as sq
from flask import jsonify


# Create the application instance
app = Flask(__name__, template_folder="templates")


# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/

    :return:        the rendered template 'home.html'
    """
    return render_template('home.html')

@app.route('/api/users')
def users_list():
    cur = sq.connect('database.db').cursor()
    cur.execute('SELECT * FROM users ORDER BY lname')
    users = cur.fetchall()
    return jsonify(users)

@app.route('/api/positions')
def position_list():
    cur = sq.connect('database.db').cursor()
    cur.execute('SELECT * FROM positions ORDER BY timestamp')
    users = cur.fetchall()
    return jsonify(users)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)