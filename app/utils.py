import json
import re

def s_express_to_json(s_exp):
    #converts s_expression to JSON
    #replacing values
    s_exp = '(' + s_exp + ')'
    s_exp = s_exp.replace(':', '')
    s_exp = s_exp.replace('(', '{').replace(')', '}').replace(' ', ' : ').replace('} ', '},').replace(',:', ',')
    for character in s_exp:
        if character.isnumeric():
            #for all numbers that are formatted like "132 :" replace it with "132,"
            s_exp = s_exp.replace(f'{character} :', f'{character},')
    #gets rid of the first and last curly brace
    s_exp = str(s_exp)[1:-1]
    #finds all words
    regex = r'\w+'
    list1=re.findall(regex,s_exp)
    i = 0
    #wrap every word with double quotes
    for word in list1:
        if word.isdigit():
            pass
        else:
            s_exp = s_exp.replace(f'{word}', f'"{word}"')
            s_exp = s_exp.replace('""', '"')
            i += 1
    s_exp = '[' + s_exp + ']'
    #if a word has two double quotes it gets rid of it
    s_exp = s_exp.replace('""', '"')
    s_exp = json.loads(s_exp)
    #turns it into json
    return s_exp