import pandas as pd

def get_file_status(csv_file, patient_id):
    patient_id = f'P_{patient_id:05d}'
    df = pd.read_csv(csv_file)
    # Filter the DataFrame to find the specific file ID
    file_status = df.loc[df['patient_id'] == patient_id, 'pathology']
    
    if not file_status.empty:
        return file_status.values[0]
    else:
        return None

# Example usage
if __name__ == "__main__":
    csv_file = '/Volumes/BOOTCAMP/Users/Tejas Annapareddy/Downloads/archive/csv/mass_case_description_train_set.csv'
    output_file = 'patient_statuses.txt'
    
    df = pd.read_csv(csv_file)
    
    with open(output_file, 'w') as f:
        for patient_id in df['patient_id']:
            # Extract the numeric part of the patient_id
            numeric_patient_id = int(patient_id.split('_')[1])
            status = get_file_status(csv_file, numeric_patient_id)
            
            if status:
                output = f"The status of patient ID {patient_id} is: {status}\n"
            else:
                output = f"Patient ID {patient_id} not found.\n"
            
            print(output.strip())
            f.write(output)