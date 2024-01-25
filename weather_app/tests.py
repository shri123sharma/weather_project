from django.test import TestCase, Client
from weather_app.utils import extract_data_from_response

class WeatherTestCase(TestCase):

    def test_index_view_with_valid_data(self):
        # Simulate a POST request to the index view with a valid query
        response = self.client.post('', {'query': 'Indore'})
        # Check if the response is successful (HTTP status code 200)
        self.assertEqual(response.status_code, 200)


    def test_index_view_with_invalid_data(self):
        # Simulate a POST request to the index view with an invalid query
        response = self.client.post('', {'query': 'ueryuerte'})
        # Check if the response is not successful (HTTP status code 200)
        self.assertEqual(response.status_code, 400)


    def test_extract_data_from_response(self):
        # Provide a sample response to test the extract_data_from_response function
        sample_response = {"location": {"name": "TestCity"}, "current": {"temp_c": 20.0, "condition": {"text": "Clear", "icon": "https://example.com/icon.png"}}, "forecast": {"forecastday": []}}

        # Call the extract_data_from_response function with the sample response
        result = extract_data_from_response(sample_response)

        # Check if the result is a dictionary
        self.assertIsInstance(result, dict)

        # Check if the relevant data is present in the result
        self.assertIn("location", result)
        self.assertIn("current", result)
        self.assertIn("forecast", result)



