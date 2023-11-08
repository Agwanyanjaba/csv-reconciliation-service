from flask import Flask
from app.controllers.reconciliation_controller import reconciliation_blueprint

app = Flask(__name__)

app.register_blueprint(reconciliation_blueprint)

if __name__ == '__main__':
    app.run(debug=True)