from flask import Flask, render_template
import requests
import post


posts = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
all_posts = []
for blog in posts:
    post_obj = post.Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    all_posts.append(post_obj)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
