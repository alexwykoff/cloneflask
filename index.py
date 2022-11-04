from flask import Flask
from markupsafe import escape
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/clone/<repo>')
def show_user_profile(repo):
    # show the user profile for that user
    f = open("repo.txt", "a")
    f.write(str((repo)) + "\n")
    f.close()
    return f'Repo {escape(repo)}'


@app.route('/repos')
def show_repos():
    pagecontent = None
    f = open("repo.txt", "r")
    repofile = f.read()
    for repo in repofile:
        print(repo)
    f.close()
    return render_template('repos.html', repofile=repofile)
