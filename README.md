# misaac3.github.io
Github hosted site for Capital One Summit Coding Challange

This is my repository for the Captial One Summit Coding Challange.
The objective is:

    "To solve this challenge, build a web application that provides the following functionality:

        1.) Visualize the data: Graph some (any 3) interesting metrics, maps, or trends from the dataset.
        2.) Price estimation: Given the geo-location (latitude and longitude) of a new property,
            estimate the weekly average income the homeowner can make with Airbnb.
        3.) Bookings optimization: Given the geo-location (latitude and longitude) of a property,
            what is the ideal price per night that will yield maximum bookings."
       
My plan is to use the JavaScript plot.ly API to graph the data from the given csv files.
With python, I used the csv and json libraries to parse the data and output into a JSON file to be used in the web application. The given csv files are assumed to be in the directory as the python scripts.

***A major assumption I have made is any listings with 0 availability in the next 30 days are NOT included in the calculations, but I assume if it is not available, it is booked. For example, a listing with 10 days available in the next 30 days would be assumed to be booked for 20 days in the next 30.***

I have chose to graph the average price of each neighbourhood, the average review of listings in a certain price range, and the average availability of each neighbourhood.

The graphs were generated using plot.ly (https://plot.ly/javascript/)

To generate a estimated weekly income from a given geolocation, I calculated the two closest neighbourhoods based on average geolocation and then used the average price and availability of each to create a weighted estimate. The closer the given geolocation is to an average neighbourhood geoloaction, the higher it is weighted.

To generate an optimal price, I calculated the price and bookings of the highest revenue generating listings and found the weighted price and expected bookings. The higher the revenue, the higher that listing is weighted.

Photo credits to:
https://Airbnb.com
http://www.capoliticalreview.com/wp-content/uploads/2014/11/San-Francisco.jpg
