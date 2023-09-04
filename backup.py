from datetime import datetime
from dateutil.relativedelta import relativedelta
import inference
import json

def processData(active_node, time):
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

jsonValue = []
lists = []
layer = 0
requirementArr = []
requirement = False
parent_num = 0
children = 0
x = 0
last_key = []
head_parent = False
values = 0
def processTime(data, event):
    global layer
    global requirement
    global jsonValue
    global parent_num
    global children
    global x
    global last_key
    global head_parent
    global values
    global lists
    for k, v in data.items():
        if isinstance(v, dict):
            if requirement == True:
                if parent_num == 1:
                    child = v[k]
                    v[k] = child + jsonValue[0]
                    children -= 1
                    if children == 0:
                        parent_num = 0
                        requirement = False
                        jsonValue = []
                if len(v) >= 2:
                    values = jsonValue[0]
                    head_parent = True
                    del jsonValue[0]
                    children = len(v)
                    jsonValue.append(v[k])
                    last_key.append(list(v)[-1])
                try:
                    if k == last_key[1]:
                        jsonValue[0] = values
                        requirement = False
                except:
                    if not last_key:
                        pass
                    elif k == last_key[0]:
                        jsonValue[0] = values
                        requirement = False
            if requirement == False:
                jsonValue = []
            if len(v) >= 2 and requirement == False:
                jsonValue.append(v[k])
                requirement = True
                parent_num = 1
                last_key.append(list(v)[-1])
            processTime(v, event)
        else:
            dictionary = {}
            dictionary[k] = v
            day = dictionary[k]
            desired_date = event - relativedelta(days=int(day))
            final = str(k + ': ' + format(desired_date, '%D'))
            lists.append(final)
    return lists


def process(node, time):
    active_node = inference.infer(node)
    active_node, event_date = processData(active_node, time)
    final = processTime(active_node, event_date)
    return final