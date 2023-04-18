from flask import *

app = Flask(__name__)

users = {
    'john': 'password123',
    'jane': 'secretword',
    'kerston': 'asdf'
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('loginpage.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/login', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return  render_template('homepage.html', name = username)
    else:
        if True:
            return render_template('loginpage.html', msg = "USER NAME AND PASSWORD DOESN'T MATCH TRY AGAIN")