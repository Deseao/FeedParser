import feedparser
import sched, time

updatePeriodSecondsMap = {
  'hourly': 60 * 60,
  'daily': 24 * 60 * 60,
  'weekly': 7 * 24 * 60 * 60,
  'monthly': 30 * 24 * 60 * 60,
  'yearly': 365 * 24 * 60 * 60
}
scheduler = sched.scheduler(time.time, time.sleep)

def pullArticles(lastHandled):
  d = feedparser.parse('https://engineering.fb.com/feed/')
  for post in d.entries:
    if post.published_parsed > lastHandled:
      #call filter instead of printing title once that function exists
      print(post.title)
    else:
      break
  scheduleNextCheck(updatePeriodSecondsMap[d.feed.sy_updateperiod]/ int(d.feed.sy_updatefrequency), d.entries[0].published_parsed)


def scheduleNextCheck(delay, lastHandled):
  scheduler.enter(delay, 1, pullArticles(lastHandled))

def start():
  d = feedparser.parse('https://engineering.fb.com/feed/')
  scheduleNextCheck(updatePeriodSecondsMap[d.feed.sy_updateperiod]/int(d.feed.sy_updatefrequency), time.strptime("Mon Jan 1 00:00:00 1970"))

start()