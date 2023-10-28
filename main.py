"""
Write a genertic program that:
- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file
- Dumps the output in (./schema/)
"""
import json
import os


def get_schema(data):
    """Construct the schema for a given data"""
    schema = {}
    for key, value in data.items():
        if isinstance(value, str):
            schema[key] = {
                "type": "string",
                "tag": "",
                "description": "",
                "required": False,
            }
        elif isinstance(value, int):
            schema[key] = {
                "type": "integer",
                "tag": "",
                "description": "",
                "required": False,
            }
        elif isinstance(value, list):
            if value and isinstance(value[0], str):
                schema[key] = {
                    "type": "enum",
                    "tag": "",
                    "description": "",
                    "required": False,
                }
            elif value and isinstance(value[0], dict):
                schema[key] = {
                    "type": "array",
                    "tag": "",
                    "description": "",
                    "items": get_schema(value[0]),
                    "required": False,
                }
        elif isinstance(value, dict):
            schema[key] = {
                "type": "object",
                "tag": "",
                "description": "",
                "properties": get_schema(value),
                "required": False,
            }
    return schema


def generate_schema_from_file(filename):
    """Read JSON from a file and generate its schema"""
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        if "message" in data:
            schema = get_schema(data["message"])
            return schema
        raise ValueError("'message' key not found in the JSON data")


def main():
    """
    Main function that generates a schema from each JSON file in the
    input directory and saves it to the output directory.

    Parameters:
        None

    Returns:
        None
    """
    input_dir = "./data/"
    output_dir = "./schema/"
    # Create the directory and ensure directory exists
    os.makedirs(output_dir, exist_ok=True)
    # Counter for given unique numbers to output files
    counter = 1
    # Iterate through each JSON file in the directory
    for file in os.listdir(input_dir):
        if file.endswith(".json"):
            output_filename = f"schema_{counter}.json"
            input_filepath = os.path.join(input_dir, file)
            output_filepath = os.path.join(output_dir, output_filename)

            # Generate schema
            schema = generate_schema_from_file(input_filepath)

            # Save the schema to the output directory
            with open(output_filepath, "w", encoding="utf-8") as f:
                json.dump(schema, f, indent=4)

            # Increment the counter for the next file
            counter += 1


if __name__ == "__main__":
    main()
