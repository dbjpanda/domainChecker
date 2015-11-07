from getWords import getwords
from pythonwhois import get_whois as whois

def check(domains, limit = 20):
    results = {}
    if type(domains) == list:
        for i,domain in enumerate(domains):
            if i < limit:
                if not whois('{0}.com'.format(domain))['contacts']['registrant']:
                    results[domain] = False
                else:
                    results[domain] = True
    else:
        domain = domains
        if not whois('{0}.com'.format(domain))['contacts']['registrant']:
            results[domain] = False
        else:
            results[domain] = True
    return results

if __name__ == "__main__":
    import csv
    f = open('output','w')
    writer = csv.writer(f)
    data = check(getwords(5),3)
    for result in data:
        csv.writerow(result)
