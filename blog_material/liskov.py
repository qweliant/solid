class T(object):
     
     def __init__(self, name):
          self.name = name
     def get_name(self):
          return self.name
     def is_subtype(self):
          return False

class S(T):
     def is_subtype(self):
          return True

obj = S("Omar")
print(obj.get_name(), obj.is_subtype())

obj = S("Kenard")
print(obj.get_name(), obj.is_subtype())
