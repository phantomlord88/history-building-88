from models import MyDate, City, HistoricalPlace,MyCase

# لیست نگهداری اطلاعات
historical_places = []

# افزودن داده
def add_historical_place():
    try:
        name = input("Enter name: ")
        day = int(input("Enter build date (day): "))
        month = int(input("Enter build date (month): "))
        year = int(input("Enter build date (year): "))
        build_date = MyDate(day, month, year)
        for i in MyCase:
            print(f"{i.value} )  {i.name}")
        a=int(input('enter number for Category : '))
        category=MyCase(a)
        area = float(input("Enter area (sqm): "))
        city_name = input("Enter city name: ")
        city = City(city_name)

        place = HistoricalPlace(name, build_date, category, area, city)
        historical_places.append(place)
        print("Historical place added successfully!")
    except ValueError as e:
        print(f"Invalid input: {e}")
       
       

# حذف داده
def remove_historical_place():
    name = input("Enter name of the place to remove: ")
    global historical_places
    initial_count = len(historical_places)
    historical_places = [p for p in historical_places if p.name != name]
    if len(historical_places) < initial_count:
        print("Historical place removed successfully.")
    else:
        print("No place found with the given name.")

# نمایش داده‌ها
def display_historical_places():
    if not historical_places:
        print("No historical places available.")
    for place in historical_places:
        print(place)

# جستجوی مکان‌های داخل یک شهر
def search_places_in_city():
    city_name = input("Enter city name to search: ")
    found = False
    for place in historical_places:
        if place.city.name == city_name:
            print(place)
            found = True
    if not found:
        print("No places found in the specified city.")

# منوی اصلی
def main():
    while True:
        print("\n1. Add Historical Place")
        print("2. Remove Historical Place")
        print("3. Display All Places")
        print("4. Search Places by City")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_historical_place()
        elif choice == "2":
            remove_historical_place()
        elif choice == "3":
            display_historical_places()
        elif choice == "4":
            search_places_in_city()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()