from flask import Flask
from flask_restful import Api
from app.controllers.reconciliation_controller import ReconciliationResource

app = Flask(__name__)
api = Api(app)

api.add_resource(ReconciliationResource, '/v1/data-tool/reconciliation')

if __name__ == '__main__':
    app.run(debug=True, port=8088)

