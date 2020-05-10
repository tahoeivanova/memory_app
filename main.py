from bottle import Bottle, route, static_file, template, run, request, redirect
from auth import User, session

application = Bottle()

# globals for user
user_global = ''

# index page
@application.route('/')
@application.route('/main')
def index():
    return template('layout')

# sign up
@application.route('/signup')
def signup():
    return template('signup')

@application.post('/signup')
def do_signup():
    nickname = request.forms.get('nickname')
    email = request.forms.get('email')
    password = request.forms.get('password')

    new_user = User(nickname=nickname, email=email, password=password)
    session.add(new_user)
    session.commit()
    return redirect('/')
    # return f'<h1> Hello, {nickname}!<br> Your e-mail: {email}<br> Your password: {password} </h1> <br><p>Now you\'re in database!</p>'

# log in
@application.route('/login')
def login():
    return template('login')

@application.post('/login')
def do_login():
    nickname = request.forms.get('nickname')
    password = request.forms.get('password')
    global user_global
    user_global = nickname

    user = session.query(User).filter_by(nickname=nickname).first()
    if user:
        if user.password == password:
            # return '<h1>You are logged in! </h1>'
            return redirect('/profile')
    return '<h1>Invalid user or password!</h1>'

@application.route('/profile')
def profile():
    global user_global
    return template('profile', user = user_global)



# static files
@application.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./static/')




if __name__ == '__main__':
    application.run(debug=True, reloader=True)

