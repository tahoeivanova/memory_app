from bottle import Bottle, route, static_file, template, run, request, redirect
from auth import User, NumberResults, session
import random
import itertools

application = Bottle()

# globals for User
user_global = ''

# globals for Number Memory
random_numbers_global = [] # a list for computer's numbers
input_numbers_global = [] # a list for user's numbers

# Index page
@application.route('/')
@application.route('/main')
@application.route('/index')
def index():
    return template('index')

# Sign up
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

# Log in
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

# Profile
@application.route('/profile')
def profile():
    global user_global
    return template('profile', user = user_global)

# Log Out
@application.route('/logout')
def logout():
    global user_global
    user_global = ''
    return redirect('/')

# Number Memory
# 1 - Set Options
@application.route('/number_memory')
def set_options():
    # clear global variables
    global random_numbers_global
    global input_numbers_global
    random_numbers_global.clear()
    input_numbers_global.clear()
    return template('number_options')

# 2 - Number Training
@application.post('/number_memory')
def set_options():
    # set number of numbers
    numbers_all = request.forms.get('numbers_all', type=int)
    # set number of digits in a number
    digits_in_number = request.forms.get('digits_in_number', type=int)
    # time for one number
    number_time = request.forms.get('number_time', type=int)
    # time for js code
    number_time *= 1000

    #_________training generator____________
    # list of random numbers
    global random_numbers_global
    # generate random numbers (1 - (0, 9), else - (10, 99))
    random_numbers_global = [random.randint(1, 9) for x in range(numbers_all)] if digits_in_number == 1 else [random.randint(10, 99) for x in range(numbers_all)]
    # return template with Number Memory Training
    return template('number_training', numbers_all = numbers_all, random_numbers_global=random_numbers_global, number_time=number_time)

# 3 - Number Input

@application.post('/number_input')
def digits_answer_input():
    # create a necessary amount of input fields
    global random_numbers_global
    return template('number_input', fields_amount=len(random_numbers_global))

# 4 - Number Results

@application.post('/number_results')
def number_results():
    # get the list of user's answers
    global input_numbers_global
    for i in range(len(random_numbers_global)): # amount of numbers
        i +=1 # counter (fields starting count from 1)
        i = str(i) #  counter to string
        # the same counter is in a template, so we can define user's answer
        user_input = request.forms.get('number'+ i, type=int) # get the user's input ('i' is a number of field)
        input_numbers_global.append(user_input) # add user's inputs in a global list

    # status Win or Loose
    results_status = ''
    # make the zip lists of results for template
    result_lists = itertools.zip_longest(input_numbers_global, random_numbers_global)

    # find a User in SQL
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    # registered user
    if user:
        # find User's Results Table
        # find user's table of results (last result)
        results_table = session.query(NumberResults).filter_by(user_id=user.id).order_by(NumberResults.attempt_id.desc()).first()

        # Comparing two lists (computer list and user list)

        # TRUE
        # add +1 to the win_amount in SQL
        if input_numbers_global == random_numbers_global:
            results_status = 'WIN'
            # if it is a first time, create a table, else - find win_amount and add 1
            win_amount_new = 1 if (results_table == None) else results_table.win_amount + 1
            loose_results = 0 if (results_table == None) else results_table.loose_amount

            results = NumberResults(user_id=user.id, win_amount=win_amount_new, loose_amount=loose_results)
            session.add(results)
            session.commit()
            win_results = results.win_amount

        # FALSE
        # add +1 to the loose_amount in SQL
        else:
            results_status = 'LOOSE'
            # if it is a first time, create a table, else - find loose_amount and add 1
            loose_amount_new = 1 if (results_table == None) else results_table.loose_amount + 1
            win_results = 0 if (results_table == None) else results_table.win_amount


            results = NumberResults(user_id=user.id, win_amount=win_results, loose_amount=loose_amount_new)
            session.add(results)
            session.commit()
            loose_results = results.loose_amount
        return template('number_results', zipped_list=result_lists, results_status=results_status, win_results=win_results, loose_results=loose_results)
    # not registered user

    return template('number_results', zipped_list=result_lists, results_status=results_status, win_results='You\'re not logged in', loose_results='You\'re not logged in')





# static files
@application.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./static/')




if __name__ == '__main__':
    application.run(debug=True, reloader=True)

