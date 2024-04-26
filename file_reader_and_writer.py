import csv

def update_csv( data):
	filename ="name.csv"
	fieldnames = ['timestamp', 'type','value']
    # Open the CSV file in append mode
	with open(filename, mode='a', newline='') as csvfile:
        # Create a DictWriter object
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		# If the file is empty, write the header
		if csvfile.tell() == 0:
		    writer.writeheader()

		# Write the data to the CSV file
		writer.writerow(data)




def read_csv():
	filename = "name.csv"
	data = []
	with open(filename, mode='r', newline='') as csvfile:
	    reader = csv.DictReader(csvfile)
	    for row in reader:
	        data.append(row)
	return data

# Example usage

