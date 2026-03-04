def oldest_person(people_dictionary):
    if not people_dictionary:
        return

    oldest_name = None
    max_age = -1
    new_york_residents = []

    for name, info in people_dictionary.items():
        if info["age"] > max_age:
            max_age = info["age"]
            oldest_name = name
        if info["city"] == "New York":
            new_york_residents.append(name)
    return (oldest_name, max_age), new_york_residents


people = {
    "Alice": {"age": 30, "city": "New York"},
    "Bob": {"age": 25, "city": "Los Angeles"},
    "Charlie": {"age": 35, "city": "Chicago"},
}
oldest, living_in_new_york = oldest_person(people)
print(oldest, living_in_new_york)
