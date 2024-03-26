class City:
    def get_name(self):
        return "Strasbourg, Toulouse, Marseille, Birmingham, Manchester, Sydney, Melbourne, Canberra"


class Strasbourg(City):
    def get_name(self):
        return "Strasbourg"


class Toulouse(City):
    def get_name(self):
        return "Toulouse"


class Marseille(City):
    def get_name(self):
        return "Marseille"


class Birmingham(City):
    def get_name(self):
        return "Birmingham"


class Manchester(City):
    def get_name(self):
        return "Manchester"


class Sydney(City):
    def get_name(self):
        return "Sydney"


class Melbourne(City):
    def get_name(self):
        return "Melbourne"


class Canberra(City):
    def get_name(self):
        return "Canberra"




class France(Marseille, Toulouse, Strasbourg):
    pass


class UK(Birmingham, Manchester):
    pass


class Australia(Sydney, Melbourne, Canberra):
    pass

class Europe (France,UK):
    pass



france = France()
australia = Australia()


print(france.get_name())        
print(australia.get_name())