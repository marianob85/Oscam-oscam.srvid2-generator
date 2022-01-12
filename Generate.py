from Kingofsat import Kingofsat
from pprint import pprint

if __name__ == '__main__':
    kingOfSat = Kingofsat([130])
    for _, orbitaldata in kingOfSat.getServices().items():
        for data in orbitaldata:
            pprint(vars(data))