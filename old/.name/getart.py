import os
import argparse
import requests
from html.parser import HTMLParser
from selenium import webdriver

link = 'http://patorjk.com/software/taag/'
tail = '#p=display&f={style}&t={text}'

p = argparse.ArgumentParser()
p.add_argument('-t', '--text', required=True, help='Text to asciify')
p.add_argument('-d', '--dir', default='art', help='directory to put downloads in')
p.add_argument('-v', '--verbose', action='store_true', help='print stuff to see progress')
args = p.parse_args()


if not os.path.exists(args.dir):
    if args.verbose:
        print('Making directory {}'.format(args.dir))
    os.mkdir(args.dir)

class OptionParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.record = 0
        self.opts = []

    def handle_starttag(self, tag, attrs):
        if tag == 'option':
            self.record = 1
        else:
            self.record = 0
    def handle_endtag(self, tag):
        pass
    def handle_data(self, data):
        if self.record:
            if len(' '.join(data.split())):
                self.opts.append(data)

def getstyles():
    global link
    try:
        OP = OptionParser()
        dat = requests.get(link).text
        OP.feed(dat)
    except Exception as e:
        if args.verbose:
            print('Couldn\'t fetch art from site: {}'.format(link))
        raise e
    return OP.opts

def getlinkstyles():
    global link, tail, args
    for s in getstyles():
        yield '{}{}'.format(link, tail).format(style=s, text=args.text), s

def style2file(s):
    return '_'.join(s.split())

if args.verbose:
    print('Grabbing links')
for req, style in getlinkstyles():
    driver = webdriver.PhantomJS()
    if args.verbose:
        print(' --> {}'.format(req))
    driver.get(req)
    pre = driver.find_elements_by_tag_name('pre')
    if len(pre) > 0:
        if len(pre) > 1 and args.verbose:
            print('\tFound more than one pre tag. Using first.')
        pre = pre[0]
    else:
        if args.verbose:
            print('\tNo pre txt found. Omitting.')
        continue
    with open('{}{}{}.art'.format(args.dir, os.sep, style2file(style)), 'w') as out:
        out.write(pre.text + '\n')
    driver.close()
    del driver

if args.verbose:
    print('Done')