from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/posts')
def posts():
    return render_template("posts.html")

@app.route('/post/id/')
def post():
    return render_template("post.html")

if __name__=="__main__":
    app.run(host="127.0.0.1",port=5000)

#  git checkout --theirs app.py