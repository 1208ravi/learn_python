import pickle              # import module first

# grades variable
grades = {'Bart':75, 'Lisa':98, 'Milhouse':80, 'Nelson':65}

f = open('gradesdict.p', 'w')   # Pickle file is newly created where foo1.py is
pickle.dump(grades, f)          # dump data to f
f.close()
