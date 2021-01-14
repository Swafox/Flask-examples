from flask import request

def do_the_login():
	return 'This was a POST request'

def show_the_login_form():
	return 'Not POST. Are you GETting me? :)'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


        
