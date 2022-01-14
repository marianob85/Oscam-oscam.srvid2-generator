import re
from Kingofsat import Kingofsat
from pprint import pprint

providers = {
    "Polsat": ['1803', '1813', '1861'],
    "NC\+": ['0B01', '1884', '0100'],
    "Platforma Canal\+": ['0100'],
    "Telewizja na kartę": ['0B00'],
    'Nova': ['0500'],
    'ORF': ['0648', '0650', '0D95', '0D98'],
    'Sky': ['098D'],
    'HD \+': ['1830', '1843', '1860', '186A']
}


def findCaid(providerName):
    if providerName is None:
        return None, ['0000']
    for provider, value in providers.items():
        if re.search(provider, providerName, re.IGNORECASE):
            return provider, value
    return None, None


if __name__ == '__main__':
    kingOfSat = Kingofsat([130, 192])
    service = []
    with open("oscam.srvid2", 'wb') as srvFile:
        for _, orbitaldata in kingOfSat.getServices().items():
            for data in orbitaldata:
                if 'FTA' in data.Encryption:
                    continue
                provider, caids = findCaid(data.Platform)
                if caids:
                    caidsStr = ','.join(caids)
                    srvFile.write("{sid:04X}:{caids}|{channelName}|||{provider}\n".format(sid=data.ServiceID, caids=caidsStr, channelName=data.Name, provider=provider).encode("utf-8"))
                else:
                    print(f"Provider not found: {data.Platform}")
