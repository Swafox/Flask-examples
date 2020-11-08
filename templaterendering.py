from flask import render_template

@app.route('/rendered')
def hello(name=None):
    return render_template('template.html', name=name)


'''
HTML example:
<!doctype html>
<title>Hello from Flask</title>
<h1>Hello again, TryHackMe</h1>
'''

