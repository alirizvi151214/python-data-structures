__author__ = 'ali.rizvi3110@gmail.com'

import json
import csv
import traceback


def create_hierarchy_tree():

    """
    Method for reading organization file and process it line by line
    to fetch the details of each employee
    """

    hierarchy = {}

    try:
        with open('sample_employee_details.csv', 'r') as org_emp_file:
            emp_details_lines = csv.reader(org_emp_file)
            # Skipping the File header record
            next(emp_details_lines)
            for each_record in emp_details_lines:
                # calling the main logic method to create hierarchy
                hierarchy = super_json({each_record[0]: each_record[2]}, each_record[1], each_record[3], hierarchy)

        return hierarchy
    except:
        print("Error while reading the organization employee details file")
        traceback.print_exc()
        return {}


def super_json(emp_manager_code_dict, emp_name, l1_name, hierarchy):

    """ Hierarchy creation logic """

    self = list(emp_manager_code_dict.keys())[0]
    l1 = list(emp_manager_code_dict.values())[0]
    if not l1:
        l1 = 'NA'
    if self not in hierarchy:
        hierarchy[self] = {"id": self, "Name": emp_name, "reportees": []}
    if l1 not in hierarchy:
        hierarchy[l1] = {"id": l1, "Name": l1_name, "reportees": []}
    hierarchy[l1]["reportees"].append(hierarchy[self])
    return hierarchy


if __name__ == "__main__":

    org_hierarchy = create_hierarchy_tree()
    if not bool(org_hierarchy):
        print("Please check the exception error !!")
    else:
        for each_user in org_hierarchy:
            print("each_user ", str(each_user), str(json.dumps(org_hierarchy[each_user])))