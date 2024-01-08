'''
#Emptty dictionary
programming_dictionary={}
print(programming_dictionary)

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                          123: "Numerical Data as Shown"}
print(programming_dictionary)
print(programming_dictionary["Bug"])
print(programming_dictionary[123])

#Add New Item to dictionary
programming_dictionary["Loop"]="Round and Round"
print(programming_dictionary)

#OverRide a dictionary
programming_dictionary["Bug"]="Moth in your computer"
print(programming_dictionary)

#Loop through a Dictionary

for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
    print(programming_dictionary)
'''    
###########################################################################################
#NESTING


#NESTING DICTIONARY IN DICTIONARY
    
travel_log1 = {
        "France":{"cities":['Paris','Frankfrut','Italy'],"visits":12},
        "India":{"cities":["Delhi","Mumbai","Raipur007"],"visits":15},
        }
print(travel_log1)
print(travel_log1["France"])

travel_log2 = [
    {
        "Country":"France",
        "cities":['Paris','Frankfrut','Italy'],
        "visits":12
     },
    {
        "Country":"India",
        "cities":["Delhi","Mumbai","Raipur007"],
        "visits":15
    },
    ]
print(travel_log2)

##########################################################################################

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string
travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Your code here 👇
def add_new_country(name, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = name
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

############################################################################
'''
issue to call a particular thing in dictionary resolved
order={
"starter":{1:"Dosa",2:"Samosa"},
"main":{1:["Curry","Fries"],"hello":"streak",3:"Murga"},
"desert":{},
}

print(order["main"][1][0])
print(order["main"][3])
print(order["main"]["hello"])
print(order["main"][3][0]) #Single-Term
'''
