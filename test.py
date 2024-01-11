import requests

def get_holidays(country, year):
    url = f'https://date.nager.at/api/v3/PublicHolidays/{year}/{country}'
    response = requests.get(url)

    if response.status_code == 200:
        holidays_data = response.json()
        return {"holidays": holidays_data}
    else:
        return {"error": f"Failed to fetch holidays. Status code: {response.status_code}"}

# Example usage
if __name__ == "__main__":
    country_input = input("Enter the country code (e.g., US, CA, GB): ")
    year_input = int(input("Enter the year: "))

    result = get_holidays(country_input, year_input)
    print(result)