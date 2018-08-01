from flask import Flask
app = Flask(__name__)

from flask import render_template
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import json

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/commits/')
@app.route('/commits/<commit_id>')
def commits(commit_id=None):
    if commit_id:
        response = urllib2.urlopen('https://api.github.com/repos/torvalds/linux/commits/'+commit_id)
        commit_details = json.loads(response.read().decode('utf-8'))
        return render_template('commit_details.html', commit_details=commit_details)
    else:
        response = urllib2.urlopen('https://api.github.com/repos/torvalds/linux/commits')
        commits = json.loads(response.read().decode('utf-8'))
        return render_template('commits.html', commits=commits)