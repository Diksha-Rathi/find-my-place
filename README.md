# find-my-place

Find the perfect place near you.

The user enters the district or city name. A search provides the top 20 results in any of the following categories.<br>

* Fire Station
* Hospital
* Hotel
* Metro Station
* Park
* Police Station
* Restaurant
* Shopping Mall

The following details are presented for all the listed places matching the query:

* Address
* Local Phone Number
* International Phone Number

The search results include places within a radius of 10 kilometers sorted in the order of their importance. Ranking will favor prominent places within the specified area. Prominence can be affected by a place's ranking in Google's index, global popularity, and other factors.

The web application is currently live on heroku. 

## Setup Instructions

* Clone the source.
```sh
$ git clone git@github.com:diksha-rathi/find-my-place.git
```
* Install the requirements
```sh
$ pip install -r /path/to/requirements.txt
```

* Generate Google API key.
  1. Visit https://developers.google.com/console and log in with a Google Account.
  2. A new project with the name API Project is created for you. Use it or create a new project.
  3. Click <b>Enable Google APIs for use in your apps</b>.
  4. Browse for the following APIs under Google Maps APIs section, and set its status to "On".
    * Google Places API Web Service
    * Google Maps Geolocation API 
  5. Once you've enabled the APIs, click <b>Credentials</b> from the left navigation of the Developer Console.
  6. In the "Public API access", click <b>Create new Key</b>.
  7. Choose <b>Server Key</b>.
  8. If you'd like to restrict requests to a specific IP address, do so now.
  9. Click <b>Create</b>.
  
  Keep your key secret.

## Run the project

```sh
$ cd find-my-place/find-my-place
$ python manage.py
```

## Todo

* Fix the Contact Us section.
* Login system to allow users to save search results.

## Wish to contribute?

* Send patches for above mentioned todos.
* Suggest new features.
* Fix bugs.

## Project Mentors

* Pankaj Kumar Choudhary- My mentor at HCL Infotech Ltd, Noida.
* Tapasweni Pathak

#### Thanks for creating the following:

* Django
* Bootstrap
* Google Places API
* Python Google Places

I started this project during my 6- weeks training with HCL Infotect Ltd, Noida between June- July 2015.
