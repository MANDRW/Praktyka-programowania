class Attraction:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def show(self):
        return f"Atrakcja: {self.name}, Lokalizacja: {self.location}"


class Rome:
    def __init__(self):
        self.attractions = []

    def add_attraction(self, attraction):
        self.attractions.append(attraction)

    def show(self):
        return f"Atrakcje: {[attraction.show() for attraction in self.attractions]}"

    def show_number(self, number):
        if 0 <= number < len(self.attractions):
            return self.attractions[number]
        return None


class Guide:
    def __init__(self, rome):
        self.place = 0
        self.rome = rome

    def show(self):
        if not self.rome.attractions:
            return "Brak atrakcji"
        attraction = self.rome.show_number(self.place)
        self.place = (self.place + 1) % len(self.rome.attractions)
        return attraction.show()


def main():
    rome = Rome()
    rome.add_attraction(Attraction("Atrakcja1", "Rzym"))
    rome.add_attraction(Attraction("Atrakcja2", "Rzym"))

    guide = Guide(rome)
    print(guide.show())
    print(guide.show())
    print(guide.show())


if __name__ == "__main__":
    main()