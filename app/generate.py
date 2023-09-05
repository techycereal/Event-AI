import random  # Import the random module for generating random values.
from sexpdata import dumps  # Import a library for working with S-expressions.
from datetime import date  # Import the date class from the datetime module.
from dateutil.relativedelta import relativedelta  # Import relativedelta for date calculations.

# Define a list of possible events.
event_types = [
    'travel',    
    'meet',
    'call',
    'email',
    'mail',    
    'trial',
    'hearing',
    'depose' 
]

# Define a list of vocabulary words.
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

final_rules = []  # Initialize an empty list to store the final rules.
requirements_greater_than_two = 0
is_requirement = 0
set_requirement = ['-']
first_key = ""
has_requirement = False
iteration = 0
step_down = 0
last_key = 0
start = True
remove_from = []

# Define a function to create requirements for the timeline.
def create_requirements(key, timeline_keys):
    timeline = {}
    timeline_keys[0] = key
    timeline = {key: random.randint(10, 150)}  # Create a requirement with a random duration.
    return timeline

# Define a function to generate a timeline.
def generate():
    leave_time = random.randint(80, 150)  # Choose a random time to leave.
    
    # Choose random values for each vocab word.
    first_plan = [0.8, 0.9, 0.76]
    second_plan = [0.76, 0.7, 0.6]
    third_plan = [0.1, 0.2, 0.08, 0.15]
    fourth_plan = [0.25, 0.30, 0.35, 0.23]
    first = random.choice(list(first_plan))
    second = random.choice(list(second_plan))
    third = random.choice(list(third_plan))
    fourth = random.choice(list(fourth_plan))
    
    # Determine the number of rules.
    rule_count = random.randint(0, 4)
    
    # Calculate days before the leave time based on random values.
    first = first * leave_time
    second = second * leave_time
    third = third * leave_time
    fourth = fourth * leave_time
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)

    # Choose a random word from vocab to create conditions in the timeline.
    values = [first, second, third, fourth]
    timeline = {}
    timeline = create_timeline(vocab, values, rule_count, timeline)
    timeline_keys = [key for k, v in timeline.items() for key in timeline[k]]
    timeline_keys = set(timeline_keys)  # Remove duplicate keys.
    timeline_keys = list(timeline_keys)
    
    # Create requirements in the timeline.
    for key in timeline_keys:
        for k, v in timeline.items():
            if key in timeline[k] and key not in timeline:
                del timeline[k][key]
            if key in timeline[k] and key in timeline and k != key:
                timeline[k][key] = 'has_requirement'
                modified_timeline = timeline[k][key]
                del timeline[k][key]
                timeline[k][key] = modified_timeline
    
    return timeline, leave_time, timeline_keys

# Define a function to create conditions in the timeline.
def create_timeline(vocab, values, rule_count, timeline):
    stop_iteration = 0
    iterations = 0
    while iterations < 5:
        rules = []
        random.shuffle(vocab)
        random.shuffle(values)
        
        # Create rules for events based on shuffled vocab and values.
        for event in vocab:
            rules.append(event)
            stop_iteration += 1
            if stop_iteration == rule_count:
                break
        condition = random.choice(list(rules))
        timeline[condition] = {conditions: v for conditions, v in zip(rules, values)}
        
        # If a condition is not found, create a random duration for it.
        if str(condition) not in str(timeline[condition]):
            timeline[condition] = {condition: random.randint(10, 150)}
        iterations += 1
    return timeline

# Define a function to generate a sentence.
def generate_sentence():
    global final_rules
    plan = []
    timeline, leave_time, timeline_keys = generate()
    
    # Add requirements to the timeline and remove duplicates.
    for key, value in timeline.items():
        for key_item in timeline[key]:
            if timeline[key][key_item] == 'has_requirement':
                timeline[key][key_item] = create_requirements(key_item, timeline_keys)
                plan.append(key_item)
    
    plan = set(plan)
    
    # Delete conditions that have become requirements.
    for each in plan:
        del timeline[each]
    
    final_rules = dictionary_walker(timeline)
    final_rules = ', '.join(final_rules)
    rule_final = final_rules
    final_rules = []
    return timeline, rule_final, leave_time

# Define a recursive function to traverse the timeline dictionary.
def dictionary_walker(timeline):
    global set_requirement
    global has_requirement
    global final_rules
    global is_requirement
    global first_key
    global iteration
    global step_down
    global last_key
    
    for key, value in timeline.items():
        if isinstance(value, dict):
            if last_key >= 1:
                is_requirement = True
                last_key -= 1
            if is_requirement == True:
                set_requirement.append('-')
            if last_key == 0:
                is_requirement = False
            if len(value) == 1:
                pass
            else:
                last_key = len(value) - 1
            dictionary_walker(value)
        else:
            set_requirement = ''.join(set_requirement)
            final_rules.append(set_requirement + " " + key + " : " + str(value))
            set_requirement = ['-']
    
    return final_rules

# Define a function to create a sentence.
def create_sentence():
    plan, generated_sentence, leave_time = generate_sentence()
    today = date.today()  # Get today's date.
    leave_time = today + relativedelta(days=leave_time)  # Add days to today's date.
    leave_time = format(leave_time, '%B %d %Y')  # Format the date.
    generated_sentence = generated_sentence.replace('_', ' ')  # Replace underscores with spaces.
    planned = '{"SRC":' + ' "' + generated_sentence + '",'
    plan = dumps(plan)  # Convert the plan to an S-expression.
    plan = plan.replace('\ ', ' ')
    plan = '"EXR":' + ' "' + plan + '"}'
    entire_plan = planned + plan
    return entire_plan

create_data_count = 0
rule_data = []

# Generate 1000 sentences and store them in a list.
while create_data_count < 1000:
    rule_data.append(create_sentence())
    create_data_count += 1

# Write the generated sentences to a file.
with open("test.json", "w") as write_to_file:
    for rule in rule_data:
        write_to_file.write(rule)
        write_to_file.write('\n')
        
create_data_count = 0
while create_data_count < 7000:
    rule_data.append(create_sentence())
    create_data_count += 1

with open("train.json", "w") as write_to_file:
    for rule in rule_data:
        write_to_file.write(rule)
        write_to_file.write('\n')