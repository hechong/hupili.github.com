import sys
if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as fp:
            print len(fp.read().decode('utf-8'))
    else:
        print "usage: %s {filename}" % sys.argv[0]

