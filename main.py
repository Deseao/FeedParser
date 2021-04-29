import feedparser
import sched, time

lastProcessedDate = time.strptime("Mon Jan 1 00:00:00 1970")

def pullArticles(lastHandled):
  d = feedparser.parse('https://engineering.fb.com/feed/')
  for post in d.entries:
    posttime = post.published_parsed
    # postDate = datetime.datetime(posttime.year, posttime.month, posttime.day, posttime.hour, posttime.minute, posttime.second)
    if posttime > lastHandled:
      #post is new
      #call filter on it once that function exists
      print(post.title)
    else:
      #post is old, we can break because the posts are sorted by time
      break
  return d.entries[0].published_parsed

#schedule = sched.scheduler(time.time, time.sleep)
#schedule.enter(3600, 1, pullArticles(lastProcessedDate))

print(time.asctime(lastProcessedDate))
lastProcessedDate = pullArticles(lastProcessedDate)
print(time.asctime(lastProcessedDate))

# find <sy:updatePeriod>
#d = feedparser.parse('https://engineering.fb.com/feed/')
#print(d.feed.sy_updateperiod)
#print(d.feed.sy_updatefrequency)