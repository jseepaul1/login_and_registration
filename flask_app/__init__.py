from flask import Flask
app = Flask(__name__)

app.secret_key = "logins_should_be_secured"