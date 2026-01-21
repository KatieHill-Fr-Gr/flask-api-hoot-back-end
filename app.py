from flask import Flask
from dotenv import load_dotenv
from auth_blueprint import authentication_blueprint

load_dotenv()

app = Flask(__name__)
app.register_blueprint(authentication_blueprint)

# Run our application, by default on port 5000
app.run()