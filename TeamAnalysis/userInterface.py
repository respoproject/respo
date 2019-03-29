from analiza import *
from main import *
import time

current_marks_excel_table = input("Current marks excel table ('.xlsx' required at end): ")
required_marks_of_competence_excel_table = input("\nRequired marks of competence excel table ('.xlsx' required at the end): ")
while True:
    model = input("\nModel to determine competence to improve (possibilities: maximal_absolute_lack/ \n/maximal_relative_lack/most_important_competence_that_lack/ \n/improve_comp_by_formula/importance_over_number): ")

    models = {'maximal_absolute_lack': maximal_absolute_lack, 
    'maximal_relative_lack': maximal_relative_lack,
    'most_important_competence_that_lack': most_important_competence_that_lack,
    'improve_comp_by_formula': improve_comp_by_formula,
    'importance_over_number': importance_over_number,
    None: None
    }

    if models[model] == importance_over_number:
        mod = input("\nSecond model needed (possibilities same as above): ")
        n = int(input("\nAbove which number are competences more important: "))
    else:
        mod, n = None, None
    view = input("\nView (optimistic/pessimistic): ")
    job_column_index = int(input("\nJob to watch (column index from 0 on): "))
    print("\n\n")
    print(improve_competence(current_marks_excel_table, required_marks_of_competence_excel_table, models[model], job_column_index, model2=models[mod], number=n))

time.sleep(10)