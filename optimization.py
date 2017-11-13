# This Python script is used for generating the JSON data for the optimization problem.
# It calculated the top 5 revenue generating listings from each neighbourhood and then
# calculates the adjusted optimal price by weighting the lisitngs that generated the most
# revenue.
#
#  A BIG assumption for these calculations is that for every day a listing is not
# available, it is booked. I also assumed that it is unreasonable for a listing to be booked
# for 30 straight days so I did not include that in the data.

import csv
import copy
import json


filename = 'listings.csv'
file = open(filename, encoding="utf8")
listings = csv.DictReader(file)

filename = 'calendar_available_only.csv'
file = open(filename, encoding="utf8")
calender = csv.DictReader(file)


nhood_top_five_revenue_dict = {'Bayview': [0, 0, 0, 0, 0], 'Bernal Heights': [0, 0, 0, 0, 0],
                               'Castro/Upper Market': [0, 0, 0, 0, 0], 'Chinatown': [0, 0, 0, 0, 0],
                               'Crocker Amazon': [0, 0, 0, 0, 0], 'Diamond Heights': [0, 0, 0, 0, 0],
                               'Downtown/Civic Center': [0, 0, 0, 0, 0], 'Excelsior': [0, 0, 0, 0, 0],
                               'Financial District': [0, 0, 0, 0, 0], 'Glen Park': [0, 0, 0, 0, 0],
                               'Golden Gate Park': [0, 0, 0, 0, 0], 'Haight Ashbury': [0, 0, 0, 0, 0],
                               'Inner Richmond': [0, 0, 0, 0, 0], 'Inner Sunset': [0, 0, 0, 0, 0],
                               'Lakeshore': [0, 0, 0, 0, 0], 'Marina': [0, 0, 0, 0, 0],
                               'Mission': [0, 0, 0, 0, 0], 'Nob Hill': [0, 0, 0, 0, 0],
                               'Noe Valley': [0, 0, 0, 0, 0], 'North Beach': [0, 0, 0, 0, 0],
                               'Ocean View': [0, 0, 0, 0, 0], 'Outer Mission': [0, 0, 0, 0, 0],
                               'Outer Richmond': [0, 0, 0, 0, 0], 'Outer Sunset': [0, 0, 0, 0, 0],
                               'Pacific Heights': [0, 0, 0, 0, 0], 'Parkside': [0, 0, 0, 0, 0],
                               'Potrero Hill': [0, 0, 0, 0, 0], 'Presidio': [0, 0, 0, 0, 0],
                               'Presidio Heights': [0, 0, 0, 0, 0], 'Russian Hill': [0, 0, 0, 0, 0],
                               'Seacliff': [0, 0, 0, 0, 0], 'South of Market': [0, 0, 0, 0, 0],
                               'Treasure Island/YBI': [0, 0, 0, 0, 0], 'Twin Peaks': [0, 0, 0, 0, 0],
                               'Visitacion Valley': [0, 0, 0, 0, 0], 'West of Twin Peaks': [0, 0, 0, 0, 0],
                               'Western Addition': [0, 0, 0, 0, 0]}
nhood_top_five_price_dict = copy.deepcopy(nhood_top_five_revenue_dict)
nhood_top_five_30dayBooked_dict = copy.deepcopy(nhood_top_five_revenue_dict)


for listing in listings:
    if listing['availability_30'] != '0':
        if listing['bedrooms'] != '':
            num_bedrooms = int(listing['bedrooms'])
        nhood = listing['neighbourhood_cleansed']
        price = listing['price']

        avail = int(listing['availability_30'])
        booked = 30 - avail

        if "," in price:
            price = price.replace(",", "")
        price = int(price[1:-3])
        rev = price * booked
        index_of_least_rev = 0
        index = 0
        for x in nhood_top_five_revenue_dict[nhood]:
            if x < nhood_top_five_revenue_dict[nhood][index_of_least_rev]:
                index_of_least_rev = index
            index += 1
        if rev > nhood_top_five_revenue_dict[nhood][index_of_least_rev]:
            nhood_top_five_revenue_dict[nhood][index_of_least_rev] = rev
            nhood_top_five_price_dict[nhood][index_of_least_rev] = price
            nhood_top_five_30dayBooked_dict[nhood][index_of_least_rev] = booked

print("top revenue" ,nhood_top_five_revenue_dict)
print(nhood_top_five_price_dict)
print(nhood_top_five_30dayBooked_dict)

nhood_top_five_total_rev = {'Bayview': 0.0, 'Bernal Heights': 0.0, 'Castro/Upper Market': 0.0, 'Chinatown': 0.0,
                       'Crocker Amazon': 0.0, 'Diamond Heights': 0.0, 'Downtown/Civic Center': 0.0, 'Excelsior': 0.0,
                       'Financial District': 0.0, 'Glen Park': 0.0, 'Golden Gate Park': 0.0, 'Haight Ashbury': 0.0,
                       'Inner Richmond': 0.0, 'Inner Sunset': 0.0, 'Lakeshore': 0.0, 'Marina': 0.0, 'Mission': 0.0,
                       'Nob Hill': 0.0, 'Noe Valley': 0.0, 'North Beach': 0.0, 'Ocean View': 0.0, 'Outer Mission': 0.0,
                       'Outer Richmond': 0.0, 'Outer Sunset': 0.0, 'Pacific Heights': 0.0, 'Parkside': 0.0,
                       'Potrero Hill': 0.0, 'Presidio': 0.0, 'Presidio Heights': 0.0, 'Russian Hill': 0.0,
                       'Seacliff': 0.0, 'South of Market': 0.0, 'Treasure Island/YBI': 0.0, 'Twin Peaks': 0.0,
                       'Visitacion Valley': 0.0, 'West of Twin Peaks': 0.0, 'Western Addition': 0.0}

for nhood in nhood_top_five_revenue_dict:
    tot = 0
    for rev in nhood_top_five_revenue_dict[nhood]:
        tot += rev
    nhood_top_five_total_rev[nhood] = tot

print(nhood_top_five_total_rev)

nhood_top_five_percentages = copy.deepcopy(nhood_top_five_revenue_dict)

for nhood in nhood_top_five_total_rev:
    index = 0
    for x in nhood_top_five_percentages[nhood]:
        nhood_top_five_percentages[nhood][index] = nhood_top_five_revenue_dict[nhood][index] / nhood_top_five_total_rev[nhood]
        index += 1

print(nhood_top_five_percentages)

nhood_top_five_proportioned_price = copy.deepcopy(nhood_top_five_revenue_dict)
nhood_top_five_proportioned_booked = copy.deepcopy(nhood_top_five_revenue_dict)

for nhood in nhood_top_five_percentages:
    index = 0
    for x in nhood_top_five_revenue_dict[nhood]:
        nhood_top_five_proportioned_price[nhood][index] = nhood_top_five_percentages[nhood][index] * nhood_top_five_price_dict[nhood][index]
        nhood_top_five_proportioned_booked[nhood][index] = nhood_top_five_percentages[nhood][index] * nhood_top_five_30dayBooked_dict[nhood][index]
        index += 1

print(nhood_top_five_proportioned_price)
print(nhood_top_five_proportioned_booked)

nhood_top_five_adjusted_price = copy.deepcopy(nhood_top_five_total_rev)
nhood_top_five_adjusted_bookings = copy.deepcopy(nhood_top_five_total_rev)
nhood_top_five_adjusted_revenue = copy.deepcopy(nhood_top_five_total_rev)

for nhood in nhood_top_five_adjusted_price:
    adj_price = 0
    adj_booked = 0

    index = 0
    for price in nhood_top_five_proportioned_price[nhood]:
        adj_price += nhood_top_five_proportioned_price[nhood][index]
        adj_booked += nhood_top_five_proportioned_booked[nhood][index]
    nhood_top_five_adjusted_price[nhood] = adj_price
    nhood_top_five_adjusted_bookings[nhood] = adj_booked
    nhood_top_five_adjusted_revenue[nhood] = adj_price * adj_booked

print(nhood_top_five_adjusted_price)
print(nhood_top_five_adjusted_bookings)
print(nhood_top_five_adjusted_revenue)


price_list =[]
bookings_list = []
rev_list = []
for nhood in nhood_top_five_adjusted_price:
    price_list.append(nhood_top_five_adjusted_price[nhood])
    bookings_list.append(nhood_top_five_adjusted_bookings[nhood])
    rev_list.append(nhood_top_five_adjusted_revenue[nhood])

content_dict = {"price": price_list, "bookings": bookings_list, "revenue": rev_list}

optimal_revenue_content = json.dumps(content_dict, sort_keys=True, indent=4)
optimal_revenue_file = open('OptimalRevenue.json', 'w')
optimal_revenue_file.write(optimal_revenue_content)
optimal_revenue_file.close()
