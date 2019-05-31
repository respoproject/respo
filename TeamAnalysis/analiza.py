#importing pandas for data analysis as well as using to read excel files
import pandas as pd
#importing random package for generating random data
import random as r
#importing numpy package for data computing
import numpy as np
#sys and os is used to write in terminal outputs
import sys, os

# Blocks for printing a function in the user interface
def blockPrint():
    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    return old_stdout

# Enables printing a function in the user interface
def enablePrint(a):
    sys.stdout = a

# Prints list's elements with commas.
def list_out(list): 
     return ", ".join(map(str, list))


''' This is the first model to find comptences and it uses four parameters that are:
param: job_column_index identifies it is an integer for the specific job 
param: ocene is the mark of the current state of the specific employee (e.g. X employee mark for english comptence is 5) 
param: potrebno identifies the required mark by company for the specific comptence (e.g. Required mark for english language is 10)
param: view that identifies the way of calculating which can be optimistic or pessimistic 

it returns maximal absolute lack between given mark and requirement
'''
def maximal_absolute_lack(job_column_index, ocene, potrebno, view):
    """
    Returns which competencies should be improved first with the maximal absolute lack statistical model.

    :param job_column_index: index referencing job column in data sheet
    :param ocene: evaluated values
    :param potrebno: required competences
    :param view: optimistic or pessimistic
    """
    maximal_lack = 0
    p = []
    o = []
    rows = []
    for i in range(len(ocene[:,job_column_index])):
        a = ocene[i, job_column_index]
        b = potrebno[i, job_column_index]
        try:
            int(a)
            a_not_a_number = False
        except:
            a_not_a_number = True
        try:
            int(b)
            b_not_a_number = False
        except:
            b_not_a_number = True
        if (b_not_a_number or (b<0) or (b>100)) and (a_not_a_number or (a<0) or (a>100)):
            print("Row {}: no requirement, no current mark.".format(str(i)))
            continue
        elif b_not_a_number or b<0 or b>100:
            print("Row {}: no requirement.".format(str(i)))
            continue
        elif a_not_a_number or a < 0 or a > 100:
            print("Row {}: no current mark. View: {}.".format(str(i), view))
            if view == "optimistic":
                continue
            elif view == "pessimistic":
                maximal_lack = float("Inf")
                p.append(b)
                o.append("no mark")
                rows.append(i)
        else:
            if b - a >= maximal_lack:
                maximal_lack = b - a
    if maximal_lack == float('Inf'):
        return ("required: " + list_out(p),"current mark: " + list_out(o), "absolute lack: " + str(maximal_lack), "improve row: " + list_out(rows))
    elif maximal_lack == 0:
        return "All competences satisfy the requirements."
    else:
        for i in range(len(ocene[:,job_column_index])):
            a = ocene[i, job_column_index]
            b = potrebno[i, job_column_index]
            try:
                if b - a == maximal_lack:
                    p.append(b)
                    o.append(a)
                    rows.append(i)
            except:
                pass
    return ("required: " + list_out(p),"current mark: " + list_out(o), "absolute lack: " + str(maximal_lack), "improve row: " + list_out(rows))


def maximal_relative_lack(job_column_index, ocene, potrebno, view):
    """
        Returns which competencies should be improved first with the maximal relative lack statistical model.

        :param job_column_index: index referencing job column in data sheet
        :param ocene: evaluated values file
        :param potrebno: required competences file
        :param view: optimistic or pessimistic
        """
    maximal_lack = 1
    p = []
    o = []
    rows = []
    for i in range(len(ocene[:,job_column_index])):
        a = ocene[i, job_column_index]
        b = potrebno[i, job_column_index]
        try:
            int(a)
            a_not_a_number = False
        except:
            a_not_a_number = True
        try:
            int(b)
            b_not_a_number = False
        except:
            b_not_a_number = True
        if (b_not_a_number or b<0 or b>100) and (a_not_a_number or a<0 or a>100):
            print("Row {}: no requirement, no current mark.".format(str(i)))
            continue
        elif b_not_a_number or b<0 or b>100:
            print("Row {}: no requirement.".format(str(i)))
            continue
        elif a_not_a_number or a<0 or a>100:
            print("Row {}: no current mark. View: {}.".format(str(i), view))
            if view == "optimistic":
                continue
            elif view == "pessimistic":
                maximal_lack = 0
                p.append(b)
                o.append("no mark")
                rows.append(i)
        else:
            if round(a/b,2) <= maximal_lack:
                maximal_lack = round(a/b,2)
    if maximal_lack == 0:
        return ("required: " + list_out(p), "current mark: " + list_out(o),"relative lack: " + str(maximal_lack), "improve row: " + list_out(rows))
    elif maximal_lack == 1:
        return "All competences satisfy the requirements."
    else:
        for i in range(len(ocene[:,job_column_index])):
            a = ocene[i, job_column_index]
            b = potrebno[i, job_column_index]
            try:
                if round(a/b,2) == maximal_lack:
                    p.append(b)
                    o.append(a)
                    rows.append(i)
            except:
                pass
    return ("required: " + list_out(p), "current mark: " + list_out(o),"relative lack: " + str(maximal_lack), "improve row: " + list_out(rows))


def most_important_competence_that_lack(job_column_index, ocene, potrebno, view):
    """
        Returns which competencies should be improved first with the most_important_competence_that_lack statistical model.

        :param job_column_index: index referencing job column in data sheet
        :param ocene: evaluated values file
        :param potrebno: required competences file
        :param view: optimistic or pessimistic
        """
    l = []
    p = []
    o = []
    rows = []
    maximal_lack = 0
    for i in range(len(ocene[:,job_column_index])):
        a = ocene[i, job_column_index]
        b = potrebno[i, job_column_index]
        try:
            int(a)
            a_not_a_number = False
        except:
            a_not_a_number = True
        try:
            int(b)
            b_not_a_number = False
        except:
            b_not_a_number = True
        if (b_not_a_number or b<0 or b>100) and (a_not_a_number or a<0 or a>100):
            print("Row {}: no requirement, no current mark.".format(str(i)))
            continue
        elif b_not_a_number or b<0 or b>100:
            print("Row {}: no requirement.".format(str(i)))
            continue
        elif a_not_a_number or a<0 or a>100:
            print("Row {}: no current mark. View: {}.".format(str(i), view))
            if view == "optimistic":
                continue
            elif view == "pessimistic":
                maximal_lack = float("Inf")
                p.append(b)
                o.append("no mark")
                rows.append(i)
        else:
            if b - a >= 0:
                l.append((b,a,i))
    if maximal_lack == float('Inf'):
        return ("required: " + list_out(p),"current mark: " + list_out(o), "absolute lack: " + str(maximal_lack), "improve row: " + list_out(rows))
    elif l == []:
        return "All competences satisfy the requirements."
    else:
        l.sort(reverse=1)
        for i in range(len(l)-1):
            if (l[i][0] > l[i][1]):
                p.append(l[i][0])
                o.append(l[i][1])
                rows.append(l[i][2])
                maximal_lack = l[i][0] - l[i][1]
                if l[i][0] == l[i+1][0]:
                    continue
                else:
                    return ("required: " + list_out(p),"current mark: " + list_out(o), "absolute lack: " + str(maximal_lack), "improve row: " + list_out(rows))


def improve_comp_by_formula(job_column_index, ocene, potrebno, table_of_importance_loc, view):
    """
    Returns which competencies should be improved first with the improve competence by formula statistical model.

    :param job_column_index: index referencing job column in data sheet
    :param ocene: evaluated values file
    :param potrebno: required competences file
    :param table_of_importance_loc: table of importance
    :param view: optimistic or pessimistic
    """
    formula_lack = 0
    p = []
    o = []
    rows = []
    if table_of_importance_loc == None:
        table_of_importance_loc = potrebno
    for i in range(len(ocene[:,job_column_index])):
        a = ocene[i, job_column_index]
        b = potrebno[i, job_column_index]
        c = table_of_importance_loc[i, job_column_index]
        try:
            int(c)
        except:
            continue
        try:
            int(a)
            a_not_a_number = False
        except:
            a_not_a_number = True
        try:
            int(b)
            b_not_a_number = False
        except:
            b_not_a_number = True
        if (b_not_a_number or b<0 or b>100) and (a_not_a_number or a<0 or a>100):
            print("Row {}: no requirement, no current mark.".format(str(i)))
            continue
        elif b_not_a_number or b<0 or b>100:
            print("Row {}: no requirement.".format(str(i)))
            continue
        elif a_not_a_number or a<0 or a>100:
            print("Row {}: no current mark. View: {}".format(str(i), view))
            if view == "optimistic":
                continue
            elif view == "pessimistic":
                formula_lack = float("Inf")
                p.append(b)
                o.append("no mark")
                rows.append(i)
        else:
            if (b - a)*c >= formula_lack:
                formula_lack = (b - a)*c
    if formula_lack == float('Inf'):
        return ("required: " + list_out(p), "current mark: " + list_out(o), "lack by formula: " + "Inf", "improve row: " + list_out(rows))
    elif formula_lack == 0:
        return "All competences satisfy the requirements."
    else:
        for i in range(len(ocene[:,job_column_index])):
            a = ocene[i, job_column_index]
            b = potrebno[i, job_column_index]
            c = table_of_importance_loc[i, job_column_index]
            try:
                if (b - a)*c == formula_lack:
                    p.append(b)
                    o.append(a)
                    rows.append(i)
            except:
                pass
    return ("required: " + list_out(p), "current mark: " + list_out(o), "lack by formula: " + str(formula_lack), "improve row: " + list_out(rows))


def importance_over_number(job_column_index, ocene_file, potrebno_file, table_of_importance, view, num=70, model=maximal_absolute_lack):
    """
    Returns which competencies should be improved first with the importace over number statistical model.

    :param job_column_index: index referencing job column in data sheet
    :param ocene: evaluated values file
    :param potrebno: required competences file
    :param table_of_importance_loc: table of importance
    :param view: optimistic or pessimistic
    :param num: importance number
    :param model: model that should be used
    :return:
    """
    if 0 > num or num > 100:
        print("Number should be between 0 and 100.")

    df1 = pd.read_excel(potrebno_file)
    df2 = pd.read_excel(ocene_file)

    over_n_indexes = []
    under_n_indexes = []

    for i in range(len(df1.iloc[:, job_column_index])):
        try:
            int(df1.iloc[i, job_column_index])
            not_a_number = False
        except:
            not_a_number = True
        if not_a_number:
            over_n_indexes.append(i)
        elif df1.iloc[i, job_column_index] >= num:
            over_n_indexes.append(i)
        else:
            under_n_indexes.append(i)
    
    new_potrebno1 = df1.iloc[over_n_indexes, [job_column_index]]
    new_ocene1 = df2.iloc[over_n_indexes, [job_column_index]]
    
    new_potrebno2 = df1.iloc[under_n_indexes, [job_column_index]]
    new_ocene2 = df2.iloc[under_n_indexes, [job_column_index]]

    potrebno = new_potrebno1.iloc
    ocene = new_ocene1.iloc

    for i in range(len(ocene[:,0])):
        printing = blockPrint()
        if model == improve_comp_by_formula:
            if (potrebno[i, 0] >= num) and (model(0, ocene, potrebno, table_of_importance, view) != "All competences satisfy the requirements."):
                enablePrint(printing)
                print("Over {} needs to be improved:".format(str(num)))
                return model(0, ocene, potrebno, table_of_importance, view)
        else:
            if (potrebno[i, 0] >= num) and (model(0, ocene, potrebno, view) != "All competences satisfy the requirements."):
                enablePrint(printing)
                print("Over {} needs to be improved:".format(str(num)))
                return model(0, ocene, potrebno, view)
        enablePrint(printing)

    potrebno = new_potrebno2.iloc
    ocene = new_ocene2.iloc

    print("Under {} needs to be improved:".format(str(num)))
    return model(0, ocene, potrebno, view)

