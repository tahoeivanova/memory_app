from bottle import Bottle, route, static_file, template, run, request, redirect
from sqlAlchemy_classes import User, NumberResults, CardsResults, PiResults, Card, PathName, PathItems, session, cards_filter
import random
import itertools
from mnemo_functions import pi_reader
from sqlalchemy import and_

application = Bottle()

# globals for User
user_global = ''

# globals for Number Memory
random_numbers_global = [] # a list for computer's numbers
# input_numbers_global = [] # a list for user's numbers

# globals for Card Memory
cards_init_global = [] # an ordered list for select input form
cards_shuffled_global = [] # shuffled cards

# globals for Pi
pi = ''
pi_length = 0
pi_field_length = 0

# globals for paths
global path_global


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
    user = session.query(User).filter_by(nickname=user_global).first()
    # registered user
    if user:
        results_number = session.query(NumberResults).filter_by(user_id=user.id).order_by(NumberResults.attempt_id.desc()).first()
        results_cards = session.query(CardsResults).filter_by(user_id=user.id).order_by(CardsResults.attempt_id.desc()).first()
        results_pi = session.query(PiResults).filter_by(user_id=user.id).order_by(PiResults.attempt_id.desc()).first()

        return template('profile', user=user_global, results_number=results_number, results_cards=results_cards, results_pi=results_pi)
    else:
        return template('profile', user='you\'re not logged in', results_number='no results', results_cards='no results', results_pi='no results')


# Log Out
@application.route('/logout')
def logout():
    global user_global
    user_global = ''
    return redirect('/')

# I - Number Memory
# 1 - Set Options
@application.route('/number_memory')
def set_options():
    # clear global variables
    global random_numbers_global
    random_numbers_global.clear()
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
    url = '/number_memory' # training one more time
    # get the list of user's answers
    # global input_numbers_global
    user_input_list = []
    for i in range(len(random_numbers_global)): # amount of numbers
        i +=1 # counter (fields starting count from 1)
        i = str(i) #  counter to string
        # the same counter is in a template, so we can define user's answer
        user_input = request.forms.get('number'+ i, type=int) # get the user's input ('i' is a number of field)
        user_input_list.append(user_input) # add user's inputs in a global list

    # status Win or Loose
    results_status = ''
    # make the zip lists of results for template
    result_lists = itertools.zip_longest(user_input_list, random_numbers_global)

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
        if user_input_list == random_numbers_global:
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
        return template('results', zipped_list=result_lists, results_status=results_status, win_results=win_results, loose_results=loose_results, url=url)
    # not registered user

    return template('results', zipped_list=result_lists, results_status='You\'re not logged in', win_results='You\'re not logged in', loose_results='You\'re not logged in', url=url)


# II - Cards Memory
# 1 - Set Options
@application.route('/cards_memory')
def cards_options():
    return template('cards_set_options')

@application.post('/cards_memory')
def show_cards():
    cards_all = request.forms.get('cards_all', type=int)
    cards_time = request.forms.get('cards_time', type=int)

    cards_time *= 1000

    # filter cards from SQL (36, 52, 53)
    cards = cards_filter(cards_all)
    # cards_initial - ordered list for answers
    cards_initial = cards.copy()
    global cards_init_global
    cards_init_global = cards_initial
    random.shuffle(cards)

    global cards_shuffled_global
    cards_shuffled_global = cards
    return template('cards_training', cards_shuffled=cards_shuffled_global, cards_time=cards_time)

@application.post('/cards_input')
def show_cards_post():
    global cards_init_global

    return template('cards_input', card_list=cards_init_global)

@application.post('/cards_results')
def cards_input():
    url = '/cards_memory'
    user_input_list = []
    global cards_shuffled_global
    for i in range(1, len(cards_shuffled_global)+1):
        i = str(i)
        user_answer_cards = request.forms.getunicode('card'+ i)
        user_answer_cards=str(user_answer_cards)
        user_input_list.append(user_answer_cards)

    # status Win or Loose
    results_status = ''
    # make the zip lists of results for template
    result_lists = itertools.zip_longest(user_input_list, cards_shuffled_global)


    # find a User in SQL
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    # registered user
    if user:
        # find User's Results Table
        # find user's table of results (last result)
        results_table = session.query(CardsResults).filter_by(user_id=user.id).order_by(
            CardsResults.attempt_id.desc()).first()

        # Comparing two lists (computer list and user list)

        # TRUE
        # add +1 to the win_amount in SQL
        if user_input_list == cards_shuffled_global:
            results_status = 'WIN'
            # if it is a first time, create a table, else - find win_amount and add 1
            win_amount_new = 1 if (results_table == None) else results_table.win_amount + 1
            loose_results = 0 if (results_table == None) else results_table.loose_amount

            results = CardsResults(user_id=user.id, win_amount=win_amount_new, loose_amount=loose_results)
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

            results = CardsResults(user_id=user.id, win_amount=win_results, loose_amount=loose_amount_new)
            session.add(results)
            session.commit()
            loose_results = results.loose_amount
        return template('results', zipped_list=result_lists, results_status=results_status,
                        win_results=win_results, loose_results=loose_results, url=url)
    # not registered user

    return template('results', zipped_list=result_lists, results_status='You\'re not logged in',
                    win_results='You\'re not logged in', loose_results='You\'re not logged in', url=url)


# III - Pi
# get pi number
@application.route('/pi/<n:int>')
def pi(n):
    pi = pi_reader(n)
    return f'<h1>3.{pi}</h1>'

# Pi Index
@application.route('/pi')
def pi_page():
    return template('pi_main')

# Options
@application.post('/pi')
def pi_page():
    global pi_length
    global pi_field_length
    pi_length = request.forms.get('pi_length', type=int) # digits after comma
    pi_field_length = request.forms.get('pi_field_length', type=int) # amount of digits in one field

    return template('pi_input', pi_length=pi_length, pi_field_length=pi_field_length)

@application.post('/pi_results')
def results_pi():
    url = '/pi'
    global pi_length
    global pi_field_length
    if pi_length%pi_field_length==0:
        count = pi_length//pi_field_length
    else:
        count = pi_length // pi_field_length + 1
    input_pi = ''
    for i in range(1, count+1):
        i = str(i)
        pi_answer = request.forms.get('pi_answer'+i)  # сколько цифр после запятой
        input_pi+=pi_answer
    print(input_pi)

    # Define Pi global
    global pi

    pi = pi_reader(pi_length)
    # pi = pi[2:] # pi without '3.'


    input_pi = list(input_pi)
    pi = list(pi)
    result_lists = itertools.zip_longest(input_pi,pi)
    results_status = ''

    # find a User in SQL
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    # registered user
    if user:
        # find User's Results Table
        # find user's table of results (last result)
        results_table = session.query(PiResults).filter_by(user_id=user.id).order_by(
            PiResults.attempt_id.desc()).first()

        # Comparing two lists (computer list and user list)

    # RESULTS
    if input_pi == pi:
        results_status = "WIN"

        # if it is a first time, create a table, else - find win_amount and add 1
        pi_signs_amount = len(pi)

        results = PiResults(user_id=user.id, pi_signs_amount=pi_signs_amount)
        session.add(results)
        session.commit()
        results = results.pi_signs_amount

    else:
        results_status = "LOOSE"
        pi_signs_amount = 'Mistakes'
    return template('results', zipped_list=result_lists, results_status=results_status, win_results=f'Вы знаете {pi_signs_amount} знаков Пи после запятой', loose_results='Not counted', url=url)





#_______

# IV - 1 - Path
# list of paths
@application.route('/path')
def path_names():
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    if user:
        path_names_all = session.query(PathName).filter_by(user_id=user.id).all()
        # path_names = path_names_all.path_name
        return template('path_names', path_names=path_names_all)
    else:
        return redirect('/login')
# add new path_name
@application.post('/path')
def add_path_name():
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    path_name = request.forms.getunicode('path_name')
    path_name_new = PathName(user_id=user.id, name=path_name)
    session.add(path_name_new)
    session.commit()
    return redirect('/path')

# delete path_name
@application.route('/path_delete/<path_id:int>')
def delete_path_name(path_id):
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    path = session.query(PathName).filter_by(user_id=user.id, id=path_id).first()

    if request.GET.delete:
        session.delete(path)
        return redirect('/path')
    return template('path_delete', path=path)

# edit path_name
@application.route('/path_name_edit/<path_id:int>', method="GET")
def edit_path_name(path_id):
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    old_path_name = session.query(PathName).filter_by(user_id=user.id, id=path_id).first()
    if request.GET.edit:
        path_name_edited = request.GET.path_name.strip()
        old_path_name.name = path_name_edited
        return redirect('/path')
    else:
        return template('path_name_edit', old_path_name=old_path_name)


# IV - 2 - Path Items

# add, edit, delete path_items
# list of path items
@application.route('/path/<path_id>')
def path_item(path_id):
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    path_items = session.query(PathItems).filter_by(user_id=user.id, path_id=path_id).all()
    if path_items:
        return template('path_items', path=path_items, path_id=path_id)
    else:
        return template('path_no_items', path_id=path_id)

# add path item
@application.post('/path/<path_id>')
def add_path_item(path_id):
    item = request.forms.getunicode('item')
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    # path = session.query(PathItems).filter_by(user_id=user.id, path_id=path_id).first()
    new_item = PathItems(user_id=user.id, path_id=path_id, name=item)
    session.add(new_item)
    session.commit()
    return redirect(f'/path/{path_id}')

# delete path item
@application.route('/path_item_delete/<path_id:int>/<item_id:int>')
def delete_path_item(path_id, item_id):
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    path_item = session.query(PathItems).filter_by(user_id=user.id, path_id=path_id, id=item_id).first()

    if request.GET.delete:
        session.delete(path_item)
        return redirect(f'/path/{path_id}')
    return template('path_item_delete', path_item=path_item, path_id=path_id, item_id=item_id)

# edit path item
@application.route('/path_item_edit/<path_id:int>/<item_id:int>', method="GET")
def edit_path_item(path_id, item_id):
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    old_item_name = session.query(PathItems).filter_by(user_id=user.id, path_id=path_id, id=item_id).first()
    if request.GET.edit:
        item_name_edited = request.GET.item_name.strip()
        old_item_name.name = item_name_edited
        return redirect(f'/path/{path_id}')
    else:
        return template('path_item_edit', old_item_name=old_item_name, path_id=path_id, item_id=item_id)

# IV - 3 - Path Training
@application.route('/path_training/<path_id:int>', method="GET")
def path_training(path_id):
    global user_global
    user = session.query(User).filter_by(nickname=user_global).first()
    path_items = session.query(PathItems).filter_by(user_id=user.id, path_id=path_id).all()
    path_item_list = []
    for item in path_items:
        item = str(item)
        path_item_list.append(item)
    global path_global
    path_global = path_item_list

    return template('path_training', numbers_all = len(path_global), random_numbers_global=path_global, number_time=5000)

@application.post('/path_input')
def path_input():
    global path_global
    return template('number_input', fields_amount=len(path_global))

@application.post('/number_results')
def path_results():
    url = '/path'
    user_input_list = []
    global path_global
    for i in range(1, len(path_global)+1):
        i = str(i)
        user_input = request.forms.getunicode('number' + i)  # get the user's input ('i' is a number of field)
        user_input_list.append(user_input)  # add user's inputs in a global list

    # status Win or Loose
    results_status = ''
    # make the zip lists of results for template
    result_lists = itertools.zip_longest(user_input_list, path_global)


    # registered user

    if user_input_list == path_global:
        results_status = 'WIN'

    # FALSE
    # add +1 to the loose_amount in SQL
    else:
        results_status = 'LOOSE'

    return template('results', zipped_list=result_lists, results_status=results_status, win_results='no result', loose_results='no result', url=url)

# V - Theory
@application.route('/theory')
def theory():
    return template('articles')


# static files
@application.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./static/')




if __name__ == '__main__':
    application.run(debug=True, reloader=True)
# if __name__ == '__main__':
#     application.run(host='0.0.0.0')



