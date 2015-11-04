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
    data = check(getwords(5),3)
    import pdb;pdb.set_trace()
