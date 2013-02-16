import sys
sys.path.append('snsapi')

import snsapi
from snsapi.platform import RSS
from snsapi.platform import RenrenBlog

def create_rss():
    config = RSS.new_channel()
    config['url'] = 'http://hupili.github.com/feeds/atom-all.xml'
    config['channel_name'] = 'github_rss_all'
    myrss = RSS(config)
    return myrss

def create_renren():
    config = RenrenBlog.new_channel()
    config.update({"app_key": "1c62fea4599e420fb4ac2a1fe38cc546",
    "app_secret": "151655bf6c87414e8571da69d8d7bd40",
    "channel_name": "renren_blog",
    })
    config.auth_info.update({
    "cmd_request_url": "(console_output)",
    "cmd_fetch_code": "(console_input)"
    })
    print config
    myrenren = RenrenBlog(config)
    myrenren.auth()
    return myrenren

import json
try:
    db = json.load(open('post_finger_print.json'))
except IOError:
    db = {}

import atexit
atexit.register(lambda: json.dump(db, open('post_finger_print.json', 'w')) )

def get_one_new_post(post_list):
    '''
    Only for RSSMessage list
    '''
    import hashlib

    for p in post_list:
        finger_print = hashlib.sha1(p.raw.summary.encode('utf-8')).hexdigest()
        if not finger_print in db:
            print "New post!"
            print p
            db[finger_print] = 1
            return p

if __name__ == '__main__':
    myrss = create_rss()
    myrenren = create_renren()

    post_list = myrss.home_timeline(2)
    post = get_one_new_post(post_list)
    if post:
        print "Get one new post. Forward to Renren"
        print post.raw.title
        myrenren.update(post.raw.summary, title=post.raw.title)
