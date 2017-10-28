import csv
import json

filename = 'listings.csv'
file = open(filename, encoding="utf8")
reader = csv.DictReader(file)

num = 2
worst_score = 100
ws_num = 0
price_neighbor_dict = {}
price_review_dict = {}
review_neighbor_dict = {}
for line in reader:
    print(num, 'neighbourhood:', line['neighbourhood'], 'price:', line['price'], 'review_scores_rating:',
          line['review_scores_rating'])

    if line['price'] is not '':
        if line['neighbourhood'] is not '':
            price_neighbor_dict['price'] = line['neighbourhood']
        if line['review_scores_rating'] is not '':
            price_review_dict['price'] = line['review_scores_rating']
    if line['neighbourhood'] is not '' and line['review_scores_rating'] is not '':
        review_neighbor_dict[] =








    if line['review_scores_rating'] is not '':
        curr_score = int(line['review_scores_rating'])
        if curr_score < worst_score:
            worst_score = curr_score
            ws_num = num
    num += 1
print('\nthe worst score is', worst_score, 'at line', ws_num)
