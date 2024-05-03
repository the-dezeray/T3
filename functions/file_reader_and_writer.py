import csv


def update_csv(data):
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_dir, "name.csv")  # Subdirectory "data"



    file_name =file_name.replace("\\","\\\\")
    fieldnames = ["timestamp", "type", "value","time"]
    # Open the CSV file in append mode
    with open(file_name, mode="a", newline="") as csvfile:
        # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # If the file is empty, write the header
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write the data to the CSV file
        writer.writerow(data)


def new_csv(data):
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_dir, "name.csv")  # Subdirectory "data"



    file_name =file_name.replace("\\","\\\\")
    fieldnames = ["timestamp", "type", "value","time"]
    # Open the CSV file in append mode
    with open(file_name, mode="w", newline="") as csvfile:
        # Create a DictWriter object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # If the file is empty, write the header
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write the data to the CSV file
        for row in data:
            writer.writerow(row)


def read_csv():
    import os

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(script_dir, "name.csv")  # Subdirectory "data"



    file_name =file_name.replace("\\","\\\\")
    data = []
    with open(file_name, mode="r", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data


# Example usage
