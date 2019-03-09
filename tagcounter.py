import sys
import urllib2
from HTMLParser import HTMLParser
from collections import Counter


class TagCounter(HTMLParser):
    def __init__(self, top):
        HTMLParser.__init__(self)
        self.TOP = top
        self.__counters = Counter()

    def handle_starttag(self, tag, attrs):
        self.__counters[tag] += 1

    @property
    def counters(self):
        return self.__counters

    def get_top(self):
        return self.__counters.most_common(self.TOP)

    def print_top(self, t_spaces=29):
        table = self.get_top()
        title = 'TOP'
        # spaces for header
        balancer = 0 if t_spaces % 2 else 1
        h_spaces = (t_spaces-len(title)+balancer) / 2
        # Header of table
        print '|%s%s%s|' % ('_' * h_spaces, title, '_' * h_spaces)
        for k, v in table:
            # calculate spaces between key and value
            difk = t_spaces - len(k)
            spaces = difk - len(str(v)) + balancer
            print '|%s%s%s|' % (k, ' ' * spaces, v)
        # Footer of table
        print '|%s|' % ('_' * (t_spaces+balancer))
        print '\n'

    def get_sum(self):
        return sum(self.__counters.values())

    def print_sum(self):
        return 'Total tags html %s' % self.get_sum()


if __name__ == '__main__':
    try:
        url = sys.argv[1]
    except IndexError:
        url = 'www.ordergroove.com/company'
    try:
        top = int(sys.argv[2])
    except IndexError:
        top = 5
    try:
        width = int(sys.argv[3])
    except IndexError:
        width = 29
    try:
        data = urllib2.urlopen('http://' + url).read()
        tag = TagCounter(top)
        tag.feed(data)
        tag.close()
        tag.print_top(width)
        print tag.print_sum()
    except urllib2.URLError:
        print 'wrong url: "%s"\nplease check it' % url

