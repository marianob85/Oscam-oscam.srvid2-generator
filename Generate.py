from Kingofsat import Kingofsat
from pprint import pprint

if __name__ == '__main__':

    #output.write("%s:%04X|%s|%s|%s\n" % (caid, int(sid), name, channel, satellite))

    providers = {
        "Polsat": ['1803', '1813', '1861'],
        "NC\+": ['0B01', '1884', '0100'],
        "Platforma Canal\+": ['0100'],
        "Telewizja na kartę":['0B00'],
        'Nova': ['0500'],
        'ORF': ['0648', '0650', '0D95', '0D98'],
        'Sky': ['098D'],
        'HD \+':['1830', '1843', '1860', '186A']
    }

    kingOfSat = Kingofsat([130, 192])
    for _, orbitaldata in kingOfSat.getServices().items():
        for data in orbitaldata:
            pass
