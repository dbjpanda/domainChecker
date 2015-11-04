import urllib2, csv
import bs4

def getwords(num):
    try:
        f = open('words{0}.txt'.format(num),'r')
        data = filter(None,f.read().split('\n'))
    except:
        site = urllib2.urlopen('http://www.poslarchive.com/math/scrabble/lists/common-{0}.html'.format(num))
        soup = bs4.BeautifulSoup(site.read())
        data = soup.find('pre').text.replace('\n',' ').split()
        f = open('words{0}.txt'.format(num),'w')
        for line in data:
            print >> f, line
    f.close()
    return data

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print getwords(sys.argv[1])
    else:
        print getwords(5)
