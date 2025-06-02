from flask import Flask, render_template
import requests
app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    gender_response = requests.get(f"https://api.genderize.io?name={name}")

    age_data = age_response.json()
    predicted_age = age_data['age']

    gender_data = gender_response.json()
    predicted_gender = gender_data['gender']

    return render_template("guess.html", name=name, predicted_gender=predicted_gender, predicted_age=predicted_age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/38562991ab348a7dbf27"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)