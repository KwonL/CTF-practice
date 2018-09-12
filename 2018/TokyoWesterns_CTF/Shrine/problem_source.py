import flask
import os
from search import search


app = flask.Flask(__name__)
# app.config['FLAG'] = os.environ.pop('FLAG')
app.config['FLAG'] = 'test_flag'

@app.route('/')
def index():
    return open(__file__).read()

@app.route('/shrine/<path:shrine>')
def shrine(shrine):
    def safe_jinja(s):
        for path, obj in search(flask.request, 10) :
            print(obj, path)
        s = s.replace('(', '').replace(')', '')
        blacklist = ['config', 'self']
        return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist])+s
    return flask.render_template_string(safe_jinja(shrine))

if __name__ == '__main__':
    app.run(debug=True)
