import requests
from collections import defaultdict


def get_breweries_by_state(state):
    url = f"https://api.openbrewerydb.org/v1/breweries?by_state={state}"
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    return response.json()


def list_breweries(states):
    all_breweries = {}
    for state in states:
        breweries = get_breweries_by_state(state)
        all_breweries[state] = breweries
        print(f"\nBreweries in {state.capitalize()}:")
        for brewery in breweries:
            print(f" - {brewery['name']} ({brewery['city']}, {brewery['state_province']})")
    return all_breweries


def count_breweries_by_state(all_breweries):
    counts = {state: len(breweries) for state, breweries in all_breweries.items()}
    print("\nNumber of breweries by state:")
    for state, count in counts.items():
        print(f" - {state.capitalize()}: {count}")
    return counts


def count_breweries_by_city(all_breweries):
    city_type_count = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    for state, breweries in all_breweries.items():
        for brewery in breweries:
            city = brewery.get('city')
            brewery_type = brewery.get('brewery_type')
            city_type_count[state][city][brewery_type] += 1

    print("\nNumber of types of breweries by city:")
    for state, cities in city_type_count.items():
        print(f" - {state.capitalize()}:")
        for city, types in cities.items():
            print(f"   {city}:")
            for brewery_type, count in types.items():
                print(f"    {brewery_type}: {count}")
    return city_type_count


def count_and_list_breweries_with_websites(all_breweries):
    website_counts = defaultdict(int)
    website_breweries = defaultdict(list)
    for state, breweries in all_breweries.items():
        for brewery in breweries:
            if brewery.get('website_url'):
                website_counts[state] += 1
                website_breweries[state].append(brewery['name'])

    print("\nNumber of breweries with websites by state:")
    for state, count in website_counts.items():
        print(f" - {state.capitalize()}: {count}")
        if count > 0:
            print("   Breweries with websites:")
            for name in website_breweries[state]:
                print(f"    - {name}")


def main():
    states = ['alaska', 'maine', 'new_york']

    all_breweries = list_breweries(states)
    count_breweries_by_state(all_breweries)
    count_breweries_by_city(all_breweries)
    count_and_list_breweries_with_websites(all_breweries)


if __name__ == "__main__":
    main()
