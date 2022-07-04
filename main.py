from flask import Flask, render_template, request, redirect, url_for, session,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

app.secret_key = '1a2b3c4d5e'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = '*****'
app.config['MYSQL_PASSWORD'] = '*****'
app.config['MYSQL_DB'] = '****'

mysql = MySQL(app)

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:

        username = request.form['username']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password))

        account = cursor.fetchone()

        if account:

            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']

            return redirect(url_for('home'))
        else:

            flash("Incorrect username/password!", "danger")
    return render_template('auth/login.html',title="Login")

@app.route('/pythonlogin/register', methods=['GET', 'POST'])
def register():
	
	
	
	
p= input("Input your password")
x = True
while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        print("Valid Password")
        x=False
        break

if x:
    print("Not a Valid Password")




    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:

        username = request.form['username']
        password = request.form['password']
        email = request.form['email']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute( "SELECT * FROM accounts WHERE username LIKE %s", [username] )
        account = cursor.fetchone()

        if account:
            flash("Account already exists!", "danger")
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash("Invalid email address!", "danger")
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash("Username must contain only characters and numbers!", "danger")
        elif not username or not password or not email:
            flash("Incorrect username/password!", "danger")
        else:

            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username,email, password))
            mysql.connection.commit()
            flash("You have successfully registered!", "success")
            return redirect(url_for('login'))

    elif request.method == 'POST':

        flash("Please fill out the form!", "danger")

    return render_template('auth/register.html',title="Register")

@app.route('/pythonlogin/home')
def home():

    if 'loggedin' in session:

        return render_template('home/home.html', username=session['username'],title="Home")

    return redirect(url_for('login'))    


@app.route('/pythonlogin/profile')
def profile():
    if 'loggedin' in session:
        return render_template('auth/profile.html', username=session['username'],title="Profile")
    return redirect(url_for('login'))  

if __name__ =='__main__':
	app.run(Debug=True)
