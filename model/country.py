class Country:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __hash__(self):
        return hash(self.code)

    def __eq__(self, other):
        return self.code == other.code

    def __repr__(self):
        return f"Country(code='{self.code}', name='{self.name}')"


class CountryDAO:
    def __init__(self):
        # Dizionario per mappare i codici agli oggetti Country
        self.countries = {}

    def get_country_by_code(self, code):
        # Restituisce l'oggetto Country corrispondente al codice, o None se non esiste
        return self.countries.get(code, None)

    def add(self, country):
        self.countries[country.code] = country

    def reset(self):
        self.countries = {}









