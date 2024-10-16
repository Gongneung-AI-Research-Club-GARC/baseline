import pandas as pd

def preprocess_imu_data(input_file, output_file):
    # Load the dataset with the first row as header
    imu_data = pd.read_csv(input_file, header=1)

    # Select the columns related to Ax, Ay, Az, Gx, Gy, Gz and the label column
    selected_columns = ['Ax', 'Ay', 'Az', 'Gx', 'Gy', 'Gz', 'Unnamed: 69']  # Last column is the label

    # Filter the dataset with selected columns
    imu_data_filtered = imu_data[selected_columns]

    # Define label mapping (e.g., 'walking' -> 0, 'running' -> 1, 'Sitting' -> 2, 'Standing' -> 3, 'Downstairs' -> 4, 'Upstairs' -> 5)
    label_mapping = {'walking': 0, 'running': 1, 'Sitting': 2, 'Standing': 3, 'Downstairs': 4, 'Upstairs': 5 }  # Add more labels as needed
    imu_data_filtered['Unnamed: 69'] = imu_data_filtered['Unnamed: 69'].map(label_mapping)

    # Drop any rows with missing data
    imu_data_filtered = imu_data_filtered.dropna()

    # Save the preprocessed dataset to a new CSV file
    imu_data_filtered.to_csv(output_file, index=False)
    print(f"Preprocessed data saved to {output_file}")

if __name__ == "__main__":
    # Define input and output file paths
    input_file = 'Participant_8.csv'  # Replace with your input file path
    output_file = 'Participant_8_processed.csv'  # Define the output file path

    # Preprocess the dataset
    preprocess_imu_data(input_file, output_file)
