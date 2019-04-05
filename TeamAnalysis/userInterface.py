from analiza import *
from main import *
import time

while True:
    current_marks_excel_table = input("\nCurrent marks excel table ('.xlsx' required at end): ")
    try:
        with open(current_marks_excel_table,'r') as dat:
            break
    except:
        print("File not found. Try again!")
    

while True:
    required_marks_of_competence_excel_table = input("\nRequired marks of competence excel table ('.xlsx' required at the end): ")
    try:
        with open(required_marks_of_competence_excel_table,'r') as dat:
            break
    except:
        print("File not found. Try again!")

models = {'maximal_absolute_lack': maximal_absolute_lack, 
'maximal_relative_lack': maximal_relative_lack,
'most_important_competence_that_lack': most_important_competence_that_lack,
'improve_comp_by_formula': improve_comp_by_formula,
'importance_over_number': importance_over_number,
None: None
}

while True:
    model = input("\nModel to determine competence to improve (possibilities: maximal_absolute_lack/ \n/maximal_relative_lack/most_important_competence_that_lack/ \n/improve_comp_by_formula/importance_over_number): ")
    if model in models:
        break
    else:
        print("Model does not exist. Try again!")

if models[model] == importance_over_number:
    while True:
        mod = input("\nSecond model needed (possibilities same as above): ")
        if mod not in models:
            print("Model does not exist. Try again!")
            continue
        else:
            break
    while True:
        n = input("\nAbove which number are competences more important: ")
        try:
            n = int(n)
        except:
            print("The input must be a number. Try again!")
        if n>100 or n<0:
            print("Number should be between 0 and 100. Try again!")
        else:
            break
else:
    mod, n = None, None

if mod == "improve_comp_by_formula" or model == "improve_comp_by_formula":
        tof = input("\nTable of importance (can be None): ")
        try:
            with open(tof, 'r') as dat:
                pass
        except:
            print("File not found. Default table: {}.".format(required_marks_of_competence_excel_table))
            tof = None
else:
    tof = None

while True:
    v = input("\nView (optimistic/pessimistic): ")
    if v == "optimistic" or v == "pessimistic":
        break
    else:
        print("View should be optimistic or pessimistic. Try again!")

while True:
    job_column_index = input("\nJob to watch (column index from 0 on): ")
    try:
        job_column_index = int(job_column_index)
        break
    except:
        print("Must be an integer. Try again!")

print("\n\n")
print(improve_competence(current_marks_excel_table, required_marks_of_competence_excel_table, models[model], job_column_index, table_of_importance=tof, model2=models[mod], number=n, view=v))

time.sleep(10)