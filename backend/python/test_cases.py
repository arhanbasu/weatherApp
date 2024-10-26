# test_cases.py
from data_processing import kelvin_to_celsius

def test_temperature_conversion():
    kelvin = 300
    expected_celsius = 26.85
    assert round(kelvin_to_celsius(kelvin), 2) == expected_celsius, "Kelvin to Celsius conversion failed."

if __name__ == "__main__":
    test_temperature_conversion()
    print("All tests passed!")

