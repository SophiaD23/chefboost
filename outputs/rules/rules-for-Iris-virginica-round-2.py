def findDecision(obj): #obj[0]: Sepal length, obj[1]: Sepal width, obj[2]: Petal length, obj[3]: Petal width
   if obj[2]<=4.7:
      if obj[3]<=1.3:
         return -0.21194155514240265
      elif obj[3]>1.3:
         if obj[0]>5.7:
            return -0.21194155514240265
         elif obj[0]<=5.7:
            return 0.03805844485759735
   elif obj[2]>4.7:
      if obj[1]<=3.3:
         if obj[0]>5.7:
            if obj[3]>1.3:
               return 0.5776811838150024
         elif obj[0]<=5.7:
            return 0.5776811838150024
      elif obj[1]>3.3:
         if obj[0]>5.7:
            if obj[3]>1.3:
               return 0.4238830804824829