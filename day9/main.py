test_dictionary = {
    "Bug": "An error that prevent the program from running",
    "Function": "A bloc of code that you can call and do the same calculation",
    "Loop": "A construct that runs a block of code multiple times"
}
print(test_dictionary["Bug"])
test_dictionary["Conditional"] = "A conditional statement that runs a block of code if the condition is true"
capitals = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
     },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    }
]

for key in test_dictionary:
    print(test_dictionary[key])