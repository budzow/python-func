def some_function(a, b):
   if a:
       b = 24
   else:
       b = 31
   print(b)
some_function(True, 31)
some_function(False, 24)
some_function(31, 31)
some_function(24, 24)
