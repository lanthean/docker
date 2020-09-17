from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
	return "<h1>Flask is up!</h1>"

def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT user, host FROM mysql.user''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')