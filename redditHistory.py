#!/usr/bin/env python 

import praw
import optparse
import os, sys
import pprint

opts = optparse.OptionParser()
opts.set_usage("Usage: %prog [options] [<file>]")
opts.add_option("--verbose", dest="verbose",action="store_true",default=False,help="Output all data for debugging")
global options
(options,args)=opts.parse_args()

userName = sys.argv[1]
print userName

#userName = "controler12"
r = praw.Reddit(user_agent='Test Script by /u/bboe')
#r.login('username', 'password')
user = r.get_redditor(userName)
gen = user.get_submitted()

karma_by_subreddit = {}
for thing in gen:
	subreddit = thing.subreddit.display_name
	karma_by_subreddit[subreddit] = (karma_by_subreddit.get(subreddit, 0) + thing.score)
pprint.pprint(karma_by_subreddit)