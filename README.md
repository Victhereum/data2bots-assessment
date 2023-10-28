# Objective
Write a genertic program that:
- Reads a JSON file similar to what's present in this location (./data/)
- Sniffs the schema of the JSON file
- Dumps the output in (./schema/)

# Additional informations for test cases
- - Padding: All attributes in the JSON schema should be padded with "tag" and "description" keys
- The schema output must capture ONLY the attributes within the "message" key of the input JSON source data (see line 8 in the input JSON files). All attributes withn the key "attributes" should be excluded
- The JSON schema should set all properties "required": false
- For data types of the JSON schema:
STRING: program should identify what is a string and map accordingly in JSON schema output
INTEGER: program should identify what is an integer and map accordingly in JSON schema output
ENUM: When the value in an array is a string, the program should map the data type as an ENUM
ARRAY: When the value in an array is another JSON object, the program should map the data type as an ARRAY


## To run the schema generator using Virtualenv follow the steps below:
NOTE: Make sure you have Python3 installed
1. Install virtualenv via pip if not installed already
```$
pip install virtualenv
```
2. Create and activate the environment
```$
virtualenv venv
```
Windows
```$
./venv/Scripts/activate
```
Linux
```$
source venv/bin/activate
```

3. Run main.py
```$
python main.py
```

4. To run the unittest
```$
python tests.py
```
