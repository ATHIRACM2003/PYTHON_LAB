#9. get rear element
abc = ('python', 'learn', 'includehelp')
print("The tuple=",abc)
out= list(i[len(i) - 1] for i in abc)
print("Output list: " + str(out))
