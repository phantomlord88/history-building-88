import enum
class MyCase(enum.Enum):
    palace=1
    masjed=2
    shower=3
class MyDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


class City:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class HistoricalPlace:
    def __init__(self, name, build_date, category, area, city):
        self.name = name
        self.build_date = build_date  # Instance of MyDate
        self.category = category
        self.area = area
        self.city = city  # Instance of City

    def __str__(self):
        return (
            f"Name: {self.name}, Category: {self.category.name}, Area: {self.area} sqm, "
            f"Build Date: {self.build_date}, City: {self.city}" )