#first time working

"""
import random
from sexpdata import dumps
from datetime import date
from dateutil.relativedelta import relativedelta
events = [
    'travel',    
    'meet',
    'call',
    'email',
    'mail',    
    'trial',
    'hearing',
    'depose'
]


arrs = []
def generate():
    global arrs
    require = False
    #the words that will be used to generate data
    vocab = [
        'activity',
        'submission',
        'meeting',
        'payment',
        'communicate',
        'document',
        'deliver',
        'purchase',
        'resume',
        'submit',
        'file',
        'schedule',
        'request',
        'provision',
        'build',
        'summons',
    ]
    #chooses a random time to leave
    go_time = random.randint(80, 150)
    #chooses a random time for each vocab word
    first_plan = [0.8, 0.9, 0.76]
    second_plan = [0.76, 0.7, 0.6]
    third_plan = [0.1, 0.2, 0.08, 0.15]
    fourth_plan = [0.25, 0.30, 0.35, 0.23]
    first = random.choice(list(first_plan))
    second = random.choice(list(second_plan))
    third = random.choice(list(third_plan))
    fourth = random.choice(list(fourth_plan))
    #amount of rules
    rule_count = random.randint(0,4)
    #multiplies those vocab values with the time to leave to get the days before the leave time
    first = first * go_time
    second = second * go_time
    third = third * go_time
    fourth = fourth * go_time
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)

    #choose a random word from the requirement_arr to be the requirement
    timeline = {}
    count = 0
    s = 0
    values = [first, second, third, fourth]
    while s < 5: 
        rules = []
        random.shuffle(vocab)
        random.shuffle(values)
        for event in vocab:
            rules.append(event)
            count += 1
            if count == rule_count:
                break
        condition = random.choice(list(rules))
        timeline[condition] = {conditions : v for conditions,v in zip(rules, values)}
        if condition not in timeline[condition]:
            timeline[condition] = {condition: first}
        s += 1
    test = [key for k,v in timeline.items() for key in timeline[k]]
    test = set(test)
    test = list(test)
    for keys in test:
        for k,v in timeline.items():
            if keys in timeline[k] and keys not in timeline:
                del timeline[k][keys]
            if keys in timeline[k] and keys in timeline and k != keys:
                timeline[k][keys] = "requirement"
                new_diction = timeline[k][keys]
                del timeline[k][keys]
                timeline[k][keys] = new_diction
    #creates the structure that will be turned into an s_expression
    return timeline, go_time


final_rule = []
def generateSentence():
    global final_rule
    plan = []
    timeline, go_time = generate()
    for k,v in timeline.items():
        for keys in timeline[k]:
            if timeline[k][keys] == 'requirement':
                timeline[k][keys] = timeline[keys]
                plan.append(keys)
    plan = set(plan)
    for each in plan:
        del timeline[each]
    final_rule = dictionary_walker({"activity" : {"activity" : 89, "submit" : {"submit" : 89, "summons" : {"summons" : 89}}, "provision" : {"provision" : 35}, "payment" : {"payment" : 82}}})
    print([{"activity" : {"activity" : 89, "submit" : {"submit" : 89}, "provision" : {"provision" : 35, "summons" : {"summons" : 89}}, "payment" : {"payment" : 82}}}])
    final_rule = ', '.join(final_rule)
    rule_final = final_rule
    final_rule = []
    return timeline, rule_final, go_time
    
plans = []
s = 0
i = 0
arr = ['-']
step = False
requirement = False
iteration = 0
def dictionary_walker(timelines):
    global s
    global arr
    global requirement
    global final_rule
    global i
    global step
    global iteration
    for k,v in timelines.items():
        if isinstance(v, dict):
            print(k, len(v))
            if isinstance(arr, str):
                arr = list(arr)
            if iteration >= 2:
                del arr[0]
                print(arr)
                iteration = 0
            if s >= 1:
                arr.append('-')
                s = 0
            if i >= 1 and step == False:
                arr.append('-')
                i = 0
            if requirement == True:
                if len(v) >= 2:
                    s += 1
                    step = True
            if step == True:
                if iteration == 1:   
                    print(k)                 
                    iteration += 1
                    step = False
                iteration += 1
            if len(v) >= 2 and requirement == False:
                requirement = True
                i +=1 
            dictionary_walker(v)
        else:
            arr = ''.join(arr)
            final_rule.append(arr + " " + k + " : " + str(v))
            if requirement == False:
                arr = ['-']
    print(final_rule)
    return final_rule

def sentence():
    plan, sentence, go_time = generateSentence()
    #gets todays date
    today = date.today()
    #adds todays date to the date to leave
    go_time = today + relativedelta(days=go_time)
    #formats the time to go into Full Month, the day (1- 31), the full Year
    go_time = format(go_time, '%B %d %Y')
    sentence = sentence.replace('_', ' ')
    planned = '{"SRC":' + ' "' + sentence + '",'
    #turn the s_expression format into an s_expression
    plan = dumps(plan)
    plan = plan.replace('\ ', ' ')
    plan = '"EXR":' + ' "' + plan + '"}'
    entire_plan = planned +plan
    return entire_plan


createData = 0

json_data = []
while createData < 1:    
    json_data.append(sentence())
    createData += 1

with open("data.txt", "w") as writetoFile:
    for data in json_data:
        writetoFile.write(data)
        writetoFile.write('\n')

"""













#second time working
"""
import random
from sexpdata import dumps
from datetime import date
from dateutil.relativedelta import relativedelta
events = [
    'travel',    
    'meet',
    'call',
    'email',
    'mail',    
    'trial',
    'hearing',
    'depose'
]


arrs = []
def generate():
    global arrs
    require = False
    #the words that will be used to generate data
    vocab = [
        'activity',
        'submission',
        'meeting',
        'payment',
        'communicate',
        'document',
        'deliver',
        'purchase',
        'resume',
        'submit',
        'file',
        'schedule',
        'request',
        'provision',
        'build',
        'summons',
    ]
    #chooses a random time to leave
    go_time = random.randint(80, 150)
    #chooses a random time for each vocab word
    first_plan = [0.8, 0.9, 0.76]
    second_plan = [0.76, 0.7, 0.6]
    third_plan = [0.1, 0.2, 0.08, 0.15]
    fourth_plan = [0.25, 0.30, 0.35, 0.23]
    first = random.choice(list(first_plan))
    second = random.choice(list(second_plan))
    third = random.choice(list(third_plan))
    fourth = random.choice(list(fourth_plan))
    #amount of rules
    rule_count = random.randint(0,4)
    #multiplies those vocab values with the time to leave to get the days before the leave time
    first = first * go_time
    second = second * go_time
    third = third * go_time
    fourth = fourth * go_time
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)

    #choose a random word from the requirement_arr to be the requirement
    timeline = {}
    count = 0
    s = 0
    values = [first, second, third, fourth]
    while s < 5: 
        rules = []
        random.shuffle(vocab)
        random.shuffle(values)
        for event in vocab:
            rules.append(event)
            count += 1
            if count == rule_count:
                break
        condition = random.choice(list(rules))
        timeline[condition] = {conditions : v for conditions,v in zip(rules, values)}
        if condition not in timeline[condition]:
            timeline[condition] = {condition: first}
        s += 1
    test = [key for k,v in timeline.items() for key in timeline[k]]
    test = set(test)
    test = list(test)
    for keys in test:
        for k,v in timeline.items():
            if keys in timeline[k] and keys not in timeline:
                del timeline[k][keys]
            if keys in timeline[k] and keys in timeline and k != keys:
                timeline[k][keys] = "requirement"
                new_diction = timeline[k][keys]
                del timeline[k][keys]
                timeline[k][keys] = new_diction
    #creates the structure that will be turned into an s_expression
    return timeline, go_time


final_rule = []
def generateSentence():
    global final_rule
    plan = []
    timeline, go_time = generate()
    for k,v in timeline.items():
        for keys in timeline[k]:
            if timeline[k][keys] == 'requirement':
                timeline[k][keys] = timeline[keys]
                plan.append(keys)
    plan = set(plan)
    for each in plan:
        del timeline[each]
    final_rule = dictionary_walker({"resume": {"resume": 20}, "activity" : {"activity" : 89, "submit" : {"submit" : 89, "summons" : {"summons" : 89}, "provision" : {"provision" : 35}}, "payment" : {"payment" : 82, "build" : {"build": 30}}},"leave": {"leave": 20}})
    print([{"activity" : {"activity" : 89, "submit" : {"submit" : 89}, "provision" : {"provision" : 35, "summons" : {"summons" : 89}}, "payment" : {"payment" : 82}}}])
    final_rule = ', '.join(final_rule)
    rule_final = final_rule
    final_rule = []
    return timeline, rule_final, go_time
    
plans = []
s = 0
i = 0
arr = ['-']
k_values = []
step = False
requirement = False
iteration = 0
wait_step = 0
start = True
def dictionary_walker(timelines):
    global s
    global arr
    global requirement
    global final_rule
    global i
    global step
    global iteration
    global wait_step
    global start
    global k_values
    for k,v in timelines.items():
        if isinstance(v, dict):
            print(k, len(v))
            if isinstance(arr, str):
                arr = list(arr)
            if iteration >= 2:
                del arr[0]
                iteration = 0
            if s >= 1:
                arr.append('-')
                s = 0
            if i >= 1 and step == False:
                arr.append('-')
                i = 0
            if requirement == True:
                if len(v) >= 2:
                    s += 1
                    wait_step = len(v)
                    step = True
            if wait_step >= 1 and step == True:
                print(wait_step)
                wait_step -=1
            if wait_step == 0:
                if iteration == 1:               
                    iteration += 1
                    step = False
                iteration += 1
            if len(v) >= 2 and requirement == False:
                requirement = True
                i +=1 
            dictionary_walker(v)
        else:
            arr = ''.join(arr)
            final_rule.append(arr + " " + k + " : " + str(v))
            if requirement == False:
                arr = ['-']
                iteration = 0
    print(final_rule)
    return final_rule

def sentence():
    plan, sentence, go_time = generateSentence()
    #gets todays date
    today = date.today()
    #adds todays date to the date to leave
    go_time = today + relativedelta(days=go_time)
    #formats the time to go into Full Month, the day (1- 31), the full Year
    go_time = format(go_time, '%B %d %Y')
    sentence = sentence.replace('_', ' ')
    planned = '{"SRC":' + ' "' + sentence + '",'
    #turn the s_expression format into an s_expression
    plan = dumps(plan)
    plan = plan.replace('\ ', ' ')
    plan = '"EXR":' + ' "' + plan + '"}'
    entire_plan = planned +plan
    return entire_plan


createData = 0

json_data = []
while createData < 1:    
    json_data.append(sentence())
    createData += 1

with open("data.txt", "w") as writetoFile:
    for data in json_data:
        writetoFile.write(data)
        writetoFile.write('\n')

"""


"""
from datetime import datetime
from dateutil.relativedelta import relativedelta
import inference

def processData(time):
    #active_node = inference.infer(rules)
    active_node = [{"build" : {"build" : 81}, "meeting" : {"meeting" : 13, "purchase" : {"purchase" : 81, "file" : {"file" : 81}}}, "activity" : {"activity" : 81}}]
    #get todays date
    date = datetime.now()
    date = format(date, '%B %d %Y')
    #get the date of the time you want to leave
    time = datetime.strptime(time, '%B %d %Y')
    time = format(time, '%B %d %Y')
    #Turns "date" and "time" into integers
    dt1 = (datetime.strptime(str(time), '%B %d %Y'))
    dt2 = (datetime.strptime(str(date), '%B %d %Y'))
    #turns date back into type "datetime.datetime"
    date = datetime.strptime(date, '%B %d %Y')
    #find how many days are between today and the time you want to leave
    result = dt1 - dt2
    result = result.days
    #turns the time you want to leave into type "datetime.datetime"
    event_date = date + relativedelta(days=int(result))
    #deletes the time value
    del active_node[0]['rule']['time']
    active_node = active_node[0]
    context = active_node
    processTime(active_node, context, event_date)
    return active_node, context, event_date

jsonValue = []
lists = []
layer = 0
requirementArr = []
def processTime(data, context, event):
    global layer
    for k, v in data.items():
        if isinstance(v, dict):
            jsonValue.append(k)
            if k == 'requirements':     
                for value in v:
                    requirementArr.append(value)
                #deletes the "requirement" value and gets the value before
                index = jsonValue.index('requirements')
                index = index - 1
                iterations = 0
                carryValue = []
                #gets the value holding the requirements
                for headValue in context['rule'][jsonValue[index]][jsonValue[index]]:
                    carryValue.append(headValue)
                    #gets the value of the first requirements
                    requirementValues = context['rule'][jsonValue[index]][jsonValue[index]]['requirements'][requirementArr[iterations]]
                    #the "getPassport" value is added to the requirement value
                    newRequirementValue = requirementValues + context['rule'][jsonValue[index]][jsonValue[index]][str(carryValue[0])]
                    #the requirement is replaced with new added value
                    v[requirementArr[iterations]] = newRequirementValue
                    iterations += 1
                    if iterations == len(requirementArr):
                        break 
                for value in v:
                    #if there are more requirements
                    if isinstance(v[value], dict):
                        iterations = 0
                        for values in v[value]:
                            #gets the value of the last set of requirements
                            lastRequirements = context['rule'][jsonValue[index]][jsonValue[index]]['requirements']['moreBefore'][values]
                            #adds the last value in the first requirement list to the "moreBefore" value
                            lastRequirements = lastRequirements + newRequirementValue
                            #replaces the "moreBefore" requirement with the added one
                            v[value][values] = lastRequirements
                            iterations += 1
                            if iterations == len(v[value]):
                                break
            processTime(v, context, event)       
        else:
            if layer < 7:
                dictionary = {}
                dictionary[k] = v
                day = dictionary[k]
                desired_date = event - relativedelta(days=int(day))
                final = str(k + ': ' + format(desired_date, '%D'))
                lists.append(final)
                print(final)
                layer += 1
        if layer == 7:
            return lists

processData('July 12 2023')
"""

password = 'hh1kk4'
i = 0

while i < 3:
    print(password)
    i +=1

"""
for word in password:
    print(word)
    if word.isnumeric():
        print(word)
        password = password.replace(word, '_')

print(password)
"""