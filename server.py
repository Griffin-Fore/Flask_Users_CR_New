from flask import Flask, render_template, request, redirect
# import the class from friend.py
from models.user import User
app = Flask(__name__)

# READ
@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("index.html", all_users = users)

@app.route('/users/new')
def user():
    return render_template('create_user_form.html')

# CREATE
@app.route('/create_user', methods=["POST"])
def create_user():
    User.save(request.form)
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

