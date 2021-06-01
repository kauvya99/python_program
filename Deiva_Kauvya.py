import sys
import csv
def max_mark(d):
	m = max(d)
	indices=[i for i, j in enumerate(d) if j == m]
	return indices
def display(s,list1):
	for i in list1:
	      print("Topper in",s,"is",name[i])
fname= sys.argv[1]
filename = open(fname, 'r')
file = csv.DictReader(filename)
name = []
maths = []
biology = []
english = []
physics = []
chemistry = []
hindi = []
for col in file:
	name.append(col['Name'])
	maths.append(col['Maths'])
	biology.append(col['Biology'])
	english.append(col['English'])
	physics.append(col['Physics'])
	chemistry.append(col['Chemistry'])
	hindi.append(col['Hindi'])

maths_index=max_mark(maths)
display("Maths",maths_index)

bio_index=max_mark(biology)
display("Biology",bio_index)

eng_index=max_mark(english)
display("English",eng_index)

physics_index=max_mark(physics)
display("Physics",physics_index)

chemistry_index=max_mark(chemistry)
display("Chemistry",chemistry_index)

hindi_index=max_mark(hindi)
display("Hindi",hindi_index)

