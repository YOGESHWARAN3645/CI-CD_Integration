import json

# Sample output data
output_data = {
    "output": "This is the output of my CI/CD pipeline!"
}

# Save the output to a JSON file
with open("output.json", "w") as f:
    json.dump(output_data, f)

print("Output has been saved to output.json")
