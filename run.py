from flask import Flask
from app.controllers.reconciliation_controller import reconciliation_blueprint  # Assuming the controller is in a directory named "controllers"

app = Flask(__name__)

# Register blueprints
app.register_blueprint(reconciliation_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8089) 