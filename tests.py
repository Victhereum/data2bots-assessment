"""Tests"""
import unittest
from unittest.mock import mock_open, patch

from main import generate_schema_from_file, get_schema


class TestSchemaGeneration(unittest.TestCase):
    """Tests"""

    def test_get_schema_for_string(self):
        """
        Test the `get_schema` function for a string input.

        This test case checks if the `get_schema` function correctly generates a schema
        for a given dictionary containing a string value.

        Parameters:
        - self: The test case instance.

        Returns:
        - None
        """
        data = {"name": "Alice"}
        schema = get_schema(data)
        expected_schema = {
            "name": {"type": "string", "tag": "", "description": "", "required": False}
        }
        self.assertEqual(schema, expected_schema)

    def test_get_schema_for_integer(self):
        """
        Test the `get_schema` function for a dictionary with an integer value.

        This test creates a dictionary `data` with a key "age" and a value of 25.
        It then calls the `get_schema` function with `data` as the argument.
        The returned schema is stored in the `schema` variable.

        The expected schema is defined as a dictionary `expected_schema` with a key "age".
        The value of "age" is another dictionary with keys "type", "tag", "description",
        and "required".
        The "type" key is set to "integer", the "tag" key is set to an empty string,
        the "description" key is set to an empty string, and the "required" key is set to False.

        The `self.assertEqual` method is then called to compare the `schema` variable with the
        `expected_schema` variable.

        If the two dictionaries are equal, the test passes.

        This test ensures that the `get_schema` function correctly handles
        dictionaries with an integer value.
        """
        data = {"age": 25}
        schema = get_schema(data)
        expected_schema = {
            "age": {"type": "integer", "tag": "", "description": "", "required": False}
        }
        self.assertEqual(schema, expected_schema)

    def test_get_schema_for_enum(self):
        """
        Test the function get_schema_for_enum.

        This tests the behavior of the get_schema_for_enum function.
        It creates a test data dictionary with a key "colors" and a list of colors as its value.
        Then, it calls the get_schema function with the test data and stores the returned
        schema in a variable.

        Finally, it compares the obtained schema with the expected schema using the
        assertEqual method.

        Parameters:
            self: The instance of the test class.

        Returns:
            None
        """
        data = {"colors": ["red", "blue"]}
        schema = get_schema(data)
        expected_schema = {
            "colors": {"type": "enum", "tag": "", "description": "", "required": False}
        }
        self.assertEqual(schema, expected_schema)

    def test_get_schema_for_array(self):
        """
        Test the function get_schema_for_array.

        This function tests the behavior of the get_schema_for_array function.
        It creates a test data dictionary with a list of user dictionaries.
        It then calls the get_schema function with the test data and assigns
        the result to the schema variable.
        The expected schema is defined as a dictionary with the same structure
        as the schema variable.
        Finally, the function asserts that the schema variable is equal to the
        expected schema.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        data = {"users": [{"name": "Alice"}, {"name": "Bob"}]}
        schema = get_schema(data)
        expected_schema = {
            "users": {
                "type": "array",
                "tag": "",
                "description": "",
                "items": {
                    "name": {
                        "type": "string",
                        "tag": "",
                        "description": "",
                        "required": False,
                    }
                },
                "required": False,
            }
        }
        self.assertEqual(schema, expected_schema)

    def test_get_schema_for_object(self):
        """
        Test the function get_schema_for_object.

        This function tests the functionality of the get_schema_for_object function.
        It creates a test data dictionary with a nested user object containing name and age.
        It then calls the get_schema function with the test data and stores the returned schema.
        The expected schema is defined as a dictionary with the same structure as the test data.
        Finally, it asserts that the generated schema is equal to the expected schema.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        data = {"user": {"name": "Alice", "age": 25}}
        schema = get_schema(data)
        expected_schema = {
            "user": {
                "type": "object",
                "tag": "",
                "description": "",
                "properties": {
                    "name": {
                        "type": "string",
                        "tag": "",
                        "description": "",
                        "required": False,
                    },
                    "age": {
                        "type": "integer",
                        "tag": "",
                        "description": "",
                        "required": False,
                    },
                },
                "required": False,
            }
        }
        self.assertEqual(schema, expected_schema)

    @patch(
        "builtins.open",
        new_callable=mock_open,
        read_data='{"message": {"name": "Alice"}}',
    )
    def test_generate_schema_from_file(self, mock_file):
        """
        Test the generate_schema_from_file function.

        This function tests the generate_schema_from_file function by mocking the builtin
        open function and passing a test file with JSON data. It asserts that the generated
        schema matches the expected schema.

        Parameters:
        - mock_file: A mock object representing the file to be opened.

        Returns:
        None
        """
        filename = "test_file.json"
        schema = generate_schema_from_file(filename)
        expected_schema = {
            "name": {"type": "string", "tag": "", "description": "", "required": False}
        }
        self.assertEqual(schema, expected_schema)

    @patch(
        "builtins.open", new_callable=mock_open, read_data='{"data": {"name": "Alice"}}'
    )
    def test_generate_schema_from_file_without_message_key(self, mock_file):
        """
        Test the function generate_schema_from_file when the file does not
        contain the 'message' key.

        Parameters:
            mock_file (MagicMock): A MagicMock object representing the mocked open function.

        Returns:
            None
        """
        filename = "test_file.json"
        with self.assertRaises(ValueError) as context:
            generate_schema_from_file(filename)
        self.assertEqual(
            str(context.exception), "'message' key not found in the JSON data"
        )


if __name__ == "__main__":
    unittest.main()
