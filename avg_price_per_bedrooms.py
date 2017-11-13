import csv
import copy
import json

filename = 'listings.csv'
file = open(filename, encoding="utf8")
listings = csv.DictReader(file)

nhood_bedroom_price_dict = {'Bayview': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Bernal Heights': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Castro/Upper Market': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Chinatown': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Crocker Amazon': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Diamond Heights': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Downtown/Civic Center': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Excelsior': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Financial District': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Glen Park': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Golden Gate Park': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Haight Ashbury': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Inner Richmond': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Inner Sunset': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Lakeshore': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Marina': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Mission': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Nob Hill': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Noe Valley': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'North Beach': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Ocean View': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Outer Mission': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Outer Richmond': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Outer Sunset': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Pacific Heights': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Parkside': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Potrero Hill': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Presidio': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Presidio Heights': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Russian Hill': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Seacliff': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'South of Market': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Treasure Island/YBI': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Twin Peaks': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Visitacion Valley': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'West of Twin Peaks': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
'Western Addition': {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 10:0},
}
nhood_bedroom_count_dict = copy.deepcopy(nhood_bedroom_price_dict)
avg_nhood_bedroom_price_dict = copy.deepcopy(nhood_bedroom_price_dict)

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
        nhood_bedroom_price_dict[nhood][num_bedrooms] += price
        nhood_bedroom_count_dict[nhood][num_bedrooms] += 1

for nhood in avg_nhood_bedroom_price_dict:
    for nBedrooms in avg_nhood_bedroom_price_dict[nhood]:
        if nhood_bedroom_count_dict[nhood][nBedrooms] != 0:
            avg_nhood_bedroom_price_dict[nhood][nBedrooms] = nhood_bedroom_price_dict[nhood][nBedrooms] / \
                                                             nhood_bedroom_count_dict[nhood][nBedrooms]

print(nhood_bedroom_price_dict)
print(nhood_bedroom_count_dict)
print(avg_nhood_bedroom_price_dict)

avg_nhood_bedroom_price_content = json.dumps(avg_nhood_bedroom_price_dict, sort_keys=True, indent=4)
avg_nhood_bedroom_price_file = open('AveragePricePerListingByBedroomPerNeighbourhood.json', 'w')
avg_nhood_bedroom_price_file.write(avg_nhood_bedroom_price_content)
avg_nhood_bedroom_price_file.close()

