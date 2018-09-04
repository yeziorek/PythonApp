import ClassIterationFor
  
def iterator():
    myclass = ClassIterationFor.MyNumbers()
    myiter = iter(myclass)
    for x in myiter:
        print(x)