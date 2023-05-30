import json

# Read the location data from the JSON file
with open("location.json", "r") as json_file:
    data = json.load(json_file)

# Create an empty matrix
matrix = [[{"name": "", "objects": []} for _ in range(5)] for _ in range(2)]  # Adjust the dimensions as per your requirement

# Fill the matrix with location names
for i, location in enumerate(data["locations"]):
    name = location["name"]
    objects = location["objects"]
    matrix[i // 5][i % 5] = {"name": name, "objects": objects}

# Print the matrix
for row in matrix:
    print(row)
