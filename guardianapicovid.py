import requests
import json
import calendar
import matplotlib.pyplot as plt
# Set up the API endpoint and base parameters
endpoint = "https://content.guardianapis.com/search"
base_params = {
    "q": "covid",
    "api-key": "KEY_GOES_HERE"
}

# Loop over each month in 2022 and generate the parameters
params_by_month = {}
for month in range(1, 13):
    # Generate the from-date and to-date strings
    year = 2022
    from_date = f"{year}-{month:02d}-01"
    to_date = f"{year}-{month:02d}-{calendar.monthrange(year, month)[1]:02d}"
    
    # Combine the base parameters with the date range
    params = {**base_params, "from-date": from_date, "to-date": to_date}
    
    # Add the parameters to the dictionary
    params_by_month[f"{year}-{month:02d}"] = params

# Loop over the parameters for each month and retrieve the number of articles
total_articles_by_month = []
for month, params in params_by_month.items():
    # Make the API request
    response = requests.get(endpoint, params=params)

    # Convert the response to JSON
    data = json.loads(response.text)

    # Get the total number of articles
    total_articles = data["response"]["total"]

    total_articles_by_month.append(total_articles)
    # Print the result
    print(f"Total number of COVID-related articles in {month}: {total_articles}")

    plt.plot(total_articles_by_month)
    plt.title("Number of COVID-Related Articles in The Guardian, 2022")
    plt.xlabel("Month")
    plt.ylabel("Number of Articles")
    plt.xticks(range(12), params_by_month.keys(), rotation=45)
    plt.show()
