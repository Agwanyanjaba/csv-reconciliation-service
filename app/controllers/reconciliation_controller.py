from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.services.reconciliation_service import ReconciliationService

reconciliation_blueprint = Blueprint('reconciliation', __name__)

@reconciliation_blueprint.route('/v1/data-tool/reconciliation', methods=['POST'])
def reconcile_files():
    try:
        source_file = request.files['sourceFile']
        target_file = request.files['targetFile']
        if source_file and target_file:
            source_filename = secure_filename(source_file.filename)
            target_filename = secure_filename(target_file.filename)
            source_file.save(source_filename)
            target_file.save(target_filename)

            reconciliation_service = ReconciliationService()
            reconciliation_report = reconciliation_service.generate_reconciliation_report(source_filename, target_filename)

            return jsonify(reconciliation_report), 200
        else:
            return jsonify({"message": "Files not provided"}), 400
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 500