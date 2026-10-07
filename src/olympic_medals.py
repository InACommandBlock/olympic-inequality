class MedalsTable:
    def __init__(self):
        self.by_country = []


class MedalsCountry:
    def __init__(self):
        self.medals_by_year = {}


class Medal:
    def __init__(self, name, type, contest):
        self.name = name
        self.type = type
        self.contest = contest

    def __str__(self):
        return f"{self.name} won {self.type} in {self.contest}"


def read():
    pass


if __name__ == '__main__':
    table = read()
    # output and test


