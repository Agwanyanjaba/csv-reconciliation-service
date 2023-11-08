import csv

class ReconciliationService:
    HEADER_TYPE = "Type"
    HEADER_ID = "ID"
    HEADER_FIELD = "Field"
    HEADER_SOURCE = "Source"
    HEADER_TARGET = "Target"
    SOURCE_OUTPUT_MSG = "Source Missing"
    TARGET_OUTPUT_MSG = "Target Missing"

    def generate_reconciliation_report(self, source_file, target_file):
        ERROR_LOG = "Error Occurred :: "
        output_file_path = "./reconciliation_report.csv"
        response_list = []
        
        try:
            source_data = self.read_csv_data(source_file)
            target_data = self.read_csv_data(target_file)

            source_headers = source_data[0]
            target_headers = target_data[0]

            with open(output_file_path, 'w', newline='') as output_file:
                writer = csv.writer(output_file)
                custom_writer = csv.writer(output_file)

                # Write headers
                custom_writer.writerow([self.HEADER_TYPE, self.HEADER_ID, self.HEADER_FIELD, self.HEADER_SOURCE, self.HEADER_TARGET])

                missing_in_target = 0
                missing_in_source = 0
                field_discrepancies = 0

                for source_values in source_data[1:]:
                    if len(source_values) >= len(target_headers):
                        found_in_target = False
                        for target_values in target_data[1:]:
                            if len(target_values) >= len(source_headers):
                                if source_values[0] == target_values[0]:
                                    found_in_target = True
                                    break
                        if not found_in_target:
                            custom_writer.writerow([self.TARGET_OUTPUT_MSG, None, source_values[0], None, None])
                            missing_in_target += 1

                for target_values in target_data[1:]:
                    if len(target_values) >= len(source_headers):
                        found_in_source = False
                        for source_values in source_data[1:]:
                            if len(source_values) >= len(target_headers):
                                if target_values[0] == source_values[0]:
                                    found_in_source = True
                                    break
                        if not found_in_source:
                            custom_writer.writerow([self.SOURCE_OUTPUT_MSG, None, target_values[0], None, None])
                            missing_in_source += 1

                for source_values in source_data[1:]:
                    if len(source_values) >= len(target_headers):
                        for target_values in target_data[1:]:
                            if len(target_values) >= len(source_headers):
                                if source_values[0] == target_values[0]:
                                    for i in range(1, len(source_values)):
                                        if source_values[i] != target_values[i]:
                                            custom_writer.writerow(["Field Discrepancy", source_values[0], source_headers[i], source_values[i], target_values[i]])
                                            field_discrepancies += 1

                response_list.append("Reconciliation completed:")
                response_list.append("- Records missing in target: " + str(missing_in_target))
                response_list.append("- Records missing in source: " + str(missing_in_source))
                response_list.append("- Records with field discrepancies: " + str(field_discrepancies))
                response_list.append("Report saved to: " + output_file_path)

        except Exception as e:
            # Logger
            error_message = ERROR_LOG + str(e)
            print(error_message)
            response_list.append(error_message)

        return response_list


    def read_csv_data(self, file_path):
        data = []
        with open(file_path, 'r', newline='') as file:
            decoded_file = file.read().splitlines()
            reader = csv.reader(decoded_file)
            for row in reader:
                data.append(row)
        return data
