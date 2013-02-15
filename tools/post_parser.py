import sys
import re

class PostParser(object):
    """docstring for PostParser"""
    def __init__(self, stream):
        super(PostParser, self).__init__()
        self.stream = stream

    def parse(self):
        return self.parse_compiled_post(self.stream)
        
    def parse_compiled_post_meta(self, arg):
        pt_meta = re.compile('([^:]+):(.+)')
        r = pt_meta.match(arg)
        if r:
            return {r.groups()[0]: r.groups()[1]}
        else:
            return {}

    def parse_compiled_post(self, fp):
        pt_hpl = re.compile('<!-- hpl ([^ ]+) (.+) -->')
        in_body = False
        body = ""
        ret = {}
        while (True):
            line = fp.readline()
            if not line:
                break
            r = pt_hpl.match(line)
            if r:
                #print "line %s" % line
                cmd = r.groups()[0]
                arg = r.groups()[1]
                if cmd == "body":
                    if arg == "begin":
                        in_body = True
                    else:
                        in_body = False
                elif cmd == "meta":
                    ret.update(self.parse_compiled_post_meta(arg))
            elif in_body:
                body += line
        ret['body'] = body
        return ret

if __name__ == '__main__':
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as fp:
            parsed = PostParser(fp).parse()
            for (k, v) in parsed.iteritems():
                print "%s: %s" % (k, v)
        #parsed = PostParser(sys.argv[1]).parse()
        #for (k, v) in parsed.iteritems():
        #    print "%s: %s" % (k, v)
    else:
        print '''usage: %s {filename}
    {filename} is the compiled HTML file name under your '_site' directory
        ''' % sys.argv[0]

