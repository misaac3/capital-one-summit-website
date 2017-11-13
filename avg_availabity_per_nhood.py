# This Python script is used for generating the JSON data for the availability.
# It calculates the average availability for a listing in each neighbourhood.
#
# A BIG assumption for these calculations is that for every day a listing is not
# available, it is booked. I also assumed that it is unreasonable for a listing to be booked
# for 30 straight days so I did not include that in the data.

import csv
import copy
import json

filename = 'listings.csv'
file = open(filename, encoding="utf8")
listings = csv.DictReader(file)

nhood_30_day_availability_dict = {'Bayview': 0.0, 'Bernal Heights': 0.0, 'Castro/Upper Market': 0.0, 'Chinatown': 0.0,
                       'Crocker Amazon': 0.0, 'Diamond Heights': 0.0, 'Downtown/Civic Center': 0.0, 'Excelsior': 0.0,
                       'Financial District': 0.0, 'Glen Park': 0.0, 'Golden Gate Park': 0.0, 'Haight Ashbury': 0.0,
                       'Inner Richmond': 0.0, 'Inner Sunset': 0.0, 'Lakeshore': 0.0, 'Marina': 0.0, 'Mission': 0.0,
                       'Nob Hill': 0.0, 'Noe Valley': 0.0, 'North Beach': 0.0, 'Ocean View': 0.0, 'Outer Mission': 0.0,
                       'Outer Richmond': 0.0, 'Outer Sunset': 0.0, 'Pacific Heights': 0.0, 'Parkside': 0.0,
                       'Potrero Hill': 0.0, 'Presidio': 0.0, 'Presidio Heights': 0.0, 'Russian Hill': 0.0,
                       'Seacliff': 0.0, 'South of Market': 0.0, 'Treasure Island/YBI': 0.0, 'Twin Peaks': 0.0,
                       'Visitacion Valley': 0.0, 'West of Twin Peaks': 0.0, 'Western Addition': 0.0}

nhood_count_dict = copy.deepcopy(nhood_30_day_availability_dict)
nhood_avg_availability_30_day_dict = copy.deepcopy(nhood_30_day_availability_dict)

# [Revenue, price, booked, lisitng_id]

nhood_max_revenue_dict = {'Bayview': [0, 0, 0, 0], 'Bernal Heights': [0, 0, 0, 0],
                        'Castro/Upper Market': [0, 0, 0, 0], 'Chinatown': [0, 0, 0, 0],
                        'Crocker Amazon': [0, 0, 0, 0], 'Diamond Heights': [0, 0, 0, 0],
                        'Downtown/Civic Center': [0, 0, 0, 0], 'Excelsior': [0, 0, 0, 0],
                        'Financial District': [0, 0, 0, 0], 'Glen Park': [0, 0, 0, 0],
                        'Golden Gate Park': [0, 0, 0, 0], 'Haight Ashbury': [0, 0, 0, 0],
                        'Inner Richmond': [0, 0, 0, 0], 'Inner Sunset': [0, 0, 0, 0],
                        'Lakeshore': [0, 0, 0, 0], 'Marina': [0, 0, 0, 0], 'Mission': [0, 0, 0, 0],
                        'Nob Hill': [0, 0, 0, 0], 'Noe Valley': [0, 0, 0, 0], 'North Beach': [0, 0, 0, 0],
                        'Ocean View': [0, 0, 0, 0], 'Outer Mission': [0, 0, 0, 0],
                        'Outer Richmond': [0, 0, 0, 0], 'Outer Sunset': [0, 0, 0, 0],
                        'Pacific Heights': [0, 0, 0, 0], 'Parkside': [0, 0, 0, 0],'Potrero Hill': [0, 0, 0, 0],
                        'Presidio': [0, 0, 0, 0], 'Presidio Heights': [0, 0, 0, 0],
                        'Russian Hill': [0, 0, 0, 0],'Seacliff': [0, 0, 0, 0], 'South of Market': [0, 0, 0, 0],
                        'Treasure Island/YBI': [0, 0, 0, 0], 'Twin Peaks': [0, 0, 0, 0],
                        'Visitacion Valley': [0, 0, 0, 0], 'West of Twin Peaks': [0, 0, 0, 0],
                        'Western Addition': [0, 0, 0, 0]
                                 }

count = 0
non_zero_count = 0
for listing in listings:
    if listing['availability_30'] != '0':
        nhood = listing['neighbourhood_cleansed']

        price = listing['price']
        if "," in price:
            price = price.replace(",", "")
        price = int(price[1:-3])

        count += 1
        if listing['availability_30'] != '0':
            availability = int(listing['availability_30'])
            non_zero_count += 1
            nhood_30_day_availability_dict[nhood] += availability
            nhood_count_dict[nhood] += 1
            revenue = price * (30 - availability)
            if revenue > nhood_max_revenue_dict[nhood][0]:
                nhood_max_revenue_dict[nhood][0] = revenue
                nhood_max_revenue_dict[nhood][1] = price
                nhood_max_revenue_dict[nhood][2] = 30 - availability
                nhood_max_revenue_dict[nhood][3] = listing['id']

print('Total number of listings:', count)
print('Non-Zero listings:', non_zero_count)

print(nhood_30_day_availability_dict)
print(nhood_count_dict)

nhood_list = []
avg_availability_30_day_list = []

for nhood in nhood_30_day_availability_dict:
    nhood_avg_availability_30_day_dict[nhood] = nhood_30_day_availability_dict[nhood] / nhood_count_dict[nhood]
    nhood_list.append(nhood)
    avg_availability_30_day_list.append(nhood_avg_availability_30_day_dict[nhood])

avg_availability_30_day_JSON_dict = {'x': nhood_list, 'y': avg_availability_30_day_list, 'type': 'bar', "text": "yValue"}

avg_nhood_availability_30_day_file_content = json.dumps(avg_availability_30_day_JSON_dict, sort_keys=True, indent=4)

avg_nhood_availability_30_day_file = open('AverageNeighbourhoodAvailability30days.json', 'w')
avg_nhood_availability_30_day_file.write(avg_nhood_availability_30_day_file_content)
avg_nhood_availability_30_day_file.close()
