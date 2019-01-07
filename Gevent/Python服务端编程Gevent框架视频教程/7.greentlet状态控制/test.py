import gevent

def win():
    return 'you win'

def fail():
    raise Exception('you fail at failing')

winner = gevent.spawn(win)
loser = gevent.spawn(fail)

try:
    gevent.joinall([winner, loser])
except Exception as e:
    print e

print loser.ready()
print loser.successful()
print loser.exception