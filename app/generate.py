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
final_rule = []
requirementsGreaterthanTwo = 0
is_requirement = 0
set_requirement = ['-']
step_up = False
has_requirement = False
iteration = 0
step_down = 0
last_key = ""

def generate():
    #the words that will be used to generate data
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

    #choose a random word from the has_requirement_set_requirement to be the has_requirement
    values = [first, second, third, fourth]
    timeline = {}
    timeline = create_timeline(vocab, values, rule_count, timeline)
    timeline_keys = [key for k,v in timeline.items() for key in timeline[k]]
    #gets rid of duplicate keys
    timeline_keys = set(timeline_keys)
    timeline_keys = list(timeline_keys)

    #creating requirements in timeline
    for keys in timeline_keys:
        for k,v in timeline.items():
            if keys in timeline[k] and keys not in timeline:
                del timeline[k][keys]
            if keys in timeline[k] and keys in timeline and k != keys:
                timeline[k][keys] = "has_requirement"
                modified_timeline = timeline[k][keys]
                del timeline[k][keys]
                timeline[k][keys] = modified_timeline
    return timeline, go_time


def create_timeline(vocab, values, rule_count, timeline):
    stop_iteration = 0
    iterations = 0
    #creating conditions in the timeline
    while iterations < 5:
        rules = []
        random.shuffle(vocab)
        random.shuffle(values)
        for event in vocab:
            rules.append(event)
            stop_iteration += 1
            if stop_iteration == rule_count:
                break
        condition = random.choice(list(rules))
        timeline[condition] = {conditions : v for conditions,v in zip(rules, values)}
        if condition not in timeline[condition]:
            timeline[condition] = {condition: random.randint(10, 150)}
        iterations += 1
    return timeline

def generateSentence():
    global final_rule
    plan = []
    timeline, go_time = generate()
    #if a key exists as a requirement and as a condition delete the condition and left with key
    for k,v in timeline.items():
        for keys in timeline[k]:
            if timeline[k][keys] == 'has_requirement':
                timeline[k][keys] = timeline[keys]
                plan.append(keys)
    #deletes duplicates
    plan = set(plan)
    for each in plan:
        del timeline[each]
    final_rule = dictionary_walker(timeline)
    final_rule = ', '.join(final_rule)
    rule_final = final_rule
    final_rule = []
    return timeline, rule_final, go_time

def dictionary_walker(timelines):
    global requirementsGreaterthanTwo
    global set_requirement
    global has_requirement
    global final_rule
    global is_requirement
    global step_up
    global iteration
    global step_down
    global last_key
    for k,v in timelines.items():
        print(v)
        if isinstance(v, dict):
            if isinstance(set_requirement, str):
                set_requirement = list(set_requirement)
            #move on to the next condition after requirements are processed and met
            if k == last_key:
                if len(v) == 1:
                    has_requirement = False
                elif len(v) >= 2:
                    last_key = list(v)[-1]
            
            if iteration >= 2:
                del set_requirement[0]
                iteration = 0
            
            #for conditions with more than 1 requirement
            if requirementsGreaterthanTwo >= 1:
                set_requirement.append('-')
                requirementsGreaterthanTwo = 0
            
            #creates first requirement
            if is_requirement >= 1 and step_up == False:
                set_requirement.append('-')
                is_requirement = 0
            #for conditions with more than 1 requirement
            if has_requirement == True:
                if len(v) >= 2:
                    requirementsGreaterthanTwo += 1
                    step_down = len(v)
                    step_up = True
            if step_down >= 1 and step_up == True:
                step_down -=1
            if step_down == 0:
                if iteration == 1:               
                    iteration += 1
                    step_up = False
                iteration += 1
            #the start of processing requirements
            if len(v) >= 2 and has_requirement == False:
                has_requirement = True
                is_requirement +=1 
                last_key = list(v)[-1]
            dictionary_walker(v)
        else:
            set_requirement = ''.join(set_requirement)
            final_rule.append(set_requirement + " " + k + " : " + str(v))
            if has_requirement == False:
                set_requirement = ['-']
                iteration = 0
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

rule_data = []
while createData < 500:    
    rule_data.append(sentence())
    createData += 1

with open("data.txt", "w") as writetoFile:
    for rule in rule_data:
        writetoFile.write(rule)
        writetoFile.write('\n')