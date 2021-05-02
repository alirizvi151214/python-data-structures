Problem:
Every organization follows a structure of all the positions. As every person in organization is an employee. An employee can be a manager OR a reportee according to their work profile and experience. For keeping the track of - who is the manager of whom, organizations (mainly HR department) create some files with employee code and manager code. But :-

1) How many reportees are coming under one manager?
2) If any employee resigns OR joins the organisation, then how the structure changes for nth level of hierarchy?

These are the problems which we may face.

Solution:
A simple python code, which will read that organisation level file and generate a dynamic organization level hierachy at Nth level.

Inputs: Give the Manager ID, Manager Name with tagged Reportee ID, Reportee Name.
(Refer sample_employee_details.csv file, which is having the details of each employee in organization)

Output: A python dictionary with a tree structure.
(Refer the code_output.txt file)