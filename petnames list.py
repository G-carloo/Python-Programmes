def selction_sort(petNames):
    "sorts out petnames in ascending order"
#definning list to be sorted
    pets =["Danny Boy","Georgy Girl","Satchi","_Bullet","Miss Daisy","Guffy","Lady","Tinky","Eleonor",
             "_Tiger","Master","Abigail","Queen","Trevor","Snuffels"]

#setting a range
    for i in range (0, pets(petNames) - 1):
        minIndex = i
        for A in range (i+1, pets(petNames)):
            if petNames(A) < petNames(minIndex):
                minIndex = A
            if minIndex != i:
                petNames(A), petNames(minIndex) == petNames(minIndex), petNames(A)

selection_sort(pets)
print(pets)
