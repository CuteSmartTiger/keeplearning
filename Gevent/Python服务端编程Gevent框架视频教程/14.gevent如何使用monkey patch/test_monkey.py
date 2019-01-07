class Moneky(object):
   def eat(self):
      print 'i want to eat banana'

m = Moneky()
m.eat()
def common_eat(self):
   print 'sorry, here only hv rice'
Moneky.eat = common_eat
m.eat()