from analiza import *
import pandas as pd

def improve_competence(current_marks_excel_table, required_marks_of_competence_excel_table, model, job_column_index, table_of_importance=None, model2=maximal_absolute_lack, number=70, view="optimistic"):
    marks = pd.read_excel(current_marks_excel_table)
    komp = pd.read_excel(required_marks_of_competence_excel_table)
    if table_of_importance == None:
        table_of_importance1 = komp.iloc
    else:
        df = pd.read_excel(table_of_importance)
        table_of_importance1 = df.iloc
    ocene = marks.iloc
    potrebno = komp.iloc
    if model == importance_over_number:
        return importance_over_number(job_column_index, current_marks_excel_table, required_marks_of_competence_excel_table, table_of_importance, view, num=number, model=model2)
    elif model == improve_comp_by_formula:
        return improve_comp_by_formula(job_column_index, ocene, potrebno, table_of_importance1, view)
    else:
        return model(job_column_index, ocene, potrebno, view)