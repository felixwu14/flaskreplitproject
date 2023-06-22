# ---- YOUR APP STARTS HERE ----

# -- Import section --
from flask import Flask
from flask import render_template
# from flask import request

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --


# INDEX
@app.route('/')
@app.route('/index')
def index():
  props = {
    'title': 'Home',
    'first_name': 'Alejandra',
  }

  return render_template('index.html', props=props)


@app.route('/secret')
def secret():
  return ("Congrats! You found the secret!")


@app.route('/results')
def results():
  props = {
    'name': 'Felix',
    'favorite_animal': 'wolf',
  }
  return (render_template('resultspage.html', props=props))


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
