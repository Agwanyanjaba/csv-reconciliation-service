from flask_restful import Resource, reqparse
#from app.services.reconciliation_service import ReconciliationService

class ReconciliationResource(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('sourceFile', type=str, location='files')
        parser.add_argument('targetFile', type=str, location='files')
        args = parser.parse_args()

        source_file = args['sourceFile']
        target_file = args['targetFile']

        #reconciliation_service = ReconciliationService()
        #reconciliation_report = reconciliation_service.generate_reconciliation_report(source_file, target_file)

        reconciliation_report = True
        if reconciliation_report:
            return {'reconciliation_report': "reconciliation_report"}, 200
        else:
            return {'error': 'An error occurred'}, 500
