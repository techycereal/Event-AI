from datetime import datetime
from dateutil.relativedelta import relativedelta
import inference
import json

children = 0
is_parent = False
jsonValue = []
rule_collection = []
has_requirement = False
last_key = []
head_parent = False
values = 0

def processactive_node(active_node, time):
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
    return active_node[0], event_date


def processTime(active_node, event):
    #processes time for values in active_node
    global children
    global has_requirement
    global jsonValue
    global is_parent
    global last_key
    global values
    global rule_collection
    #dictionary walker
    for k, v in active_node.items():
        if isinstance(v, dict):
            if has_requirement == True:
                if is_parent == True:
                    child = v[k]
                    v[k] = child + jsonValue[0]
                    children -= 1
                    if children == 0:
                        is_parent = False
                        has_requirement = False
                        jsonValue = []
                if len(v) >= 2:
                    values = jsonValue[0]
                    del jsonValue[0]
                    children = len(v)
                    jsonValue.append(v[k])
                    last_key.append(list(v)[-1])
                try:
                    if k == last_key[1]:
                        jsonValue[0] = values
                        has_requirement = False
                except:
                    if not last_key:
                        pass
                    elif k == last_key[0]:
                        jsonValue[0] = values
                        has_requirement = False
            if has_requirement == False:
                jsonValue = []
            if len(v) >= 2 and has_requirement == False:
                jsonValue.append(v[k])
                has_requirement = True
                is_parent = True
                last_key.append(list(v)[-1])
            processTime(v, event)
        else:
            dictionary = {}
            dictionary[k] = v
            day = dictionary[k]
            desired_date = event - relativedelta(days=int(day))
            rule = str(k + ': ' + format(desired_date, '%D'))
            rule_collection.append(rule)
    return rule_collection


def process(node, time):
    active_node = inference.infer(node)
    active_node, event_date = processactive_node(active_node, time)
    rule = processTime(active_node, event_date)
    return rule