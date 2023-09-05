from datetime import datetime  # Import the datetime module for working with dates and times.
from dateutil.relativedelta import relativedelta  # Import relativedelta for date calculations.
import inference  # Import the 'inference' module (presumably containing some inference logic).
import json  # Import the JSON module for working with JSON data.

# Initialize variables with more meaningful names following best coding practices.
child_count = 0
is_current_node_parent = False
json_values = []  # Initialize an empty list to store JSON values.
generated_rules = []  # Initialize an empty list to store generated rules.
has_requirements = False
last_encountered_keys = []  # Initialize an empty list to store the last encountered key in the dictionary.
is_head_parent = False
current_values = 0  # Initialize a variable to store values during processing.

def process_active_node(active_node, leave_time):
    # Process the active node and calculate the event date based on the current date and provided leave_time.

    # Get today's date.
    current_date = datetime.now()
    current_date = format(current_date, '%B %d %Y')

    # Parse the provided 'leave_time' into a datetime object.
    leave_time = datetime.strptime(leave_time, '%B %d %Y')
    leave_time = format(leave_time, '%B %d %Y')

    # Convert 'current_date' and 'leave_time' into integers.
    current_datetime = datetime.strptime(str(current_date), '%B %d %Y')
    leave_datetime = datetime.strptime(str(leave_time), '%B %d %Y')

    # Convert 'current_date' back into a datetime object.
    current_date = datetime.strptime(current_date, '%B %d %Y')

    # Calculate the number of days between today and the provided 'leave_time'.
    days_difference = leave_datetime - current_datetime
    days_difference = days_difference.days

    # Calculate the event date by adding the number of days to the current date.
    event_date = current_date + relativedelta(days=int(days_difference))

    # Return the active node and the event date.
    return active_node[0], event_date

def process_time(active_node, event_date):
    # Process time values in the active node and generate rules.

    global child_count
    global has_requirements
    global json_values
    global is_current_node_parent
    global last_encountered_keys
    global current_values
    global generated_rules

    # Dictionary walker to traverse the active_node.
    for key, value in active_node.items():
        if isinstance(value, dict):
            if has_requirements:
                if is_current_node_parent:
                    child_value = value[key]
                    value[key] = child_value + json_values[0]
                    child_count -= 1
                    if child_count == 0:
                        is_current_node_parent = False
                        has_requirements = False
                        json_values = []

                # Check if there are more than one child nodes.
                if len(value) >= 2:
                    current_values = json_values[0]
                    del json_values[0]
                    child_count = len(value)
                    json_values.append(value[key])
                    last_encountered_keys.append(list(value)[-1])

                try:
                    if key == last_encountered_keys[1]:
                        json_values[0] = current_values
                        has_requirements = False
                except:
                    if not last_encountered_keys:
                        pass
                    elif key == last_encountered_keys[0]:
                        json_values[0] = current_values
                        has_requirements = False

            if not has_requirements:
                json_values = []

            # Check if there are more than one child nodes and start processing.
            if len(value) >= 2 and not has_requirements:
                json_values.append(value[key])
                has_requirements = True
                is_current_node_parent = True
                last_encountered_keys.append(list(value)[-1])

            # Recursively process child nodes.
            process_time(value, event_date)
        else:
            rule_dict = {}
            rule_dict[key] = value
            days = rule_dict[key]

            # Calculate the desired date based on the event date and the days value.
            desired_date = event_date - relativedelta(days=int(days))

            # Generate a rule string with the calculated date.
            generated_rule = str(key + ': ' + format(desired_date, '%D'))
 
            # Append the rule to the generated rules collection.
            generated_rules.append(generated_rule)

    return generated_rules

def process_input(node, leave_time):
    global child_count
    global has_requirements
    global json_values
    global is_current_node_parent
    global last_encountered_keys
    global current_values
    global generated_rules
    # Process the input 'node' using inference logic and generate rules based on the provided 'leave_time'.

    # Perform inference to obtain an active node.
    active_node = inference.infer(node)

    # Process the active node and calculate the event date.
    active_node, event_date = process_active_node(active_node, leave_time)

    # Process time values in the active node and generate rules.
    rules = process_time(active_node, event_date)
    #reset all values
    child_count = 0
    is_current_node_parent = False
    json_values = []  # Initialize an empty list to store JSON values.
    generated_rules = []  # Initialize an empty list to store generated rules.
    has_requirements = False
    last_encountered_keys = []  # Initialize an empty list to store the last encountered key in the dictionary.
    is_head_parent = False
    current_values = 0  # Initialize a variable to store values during processing.

    # Return the generated rules.
    return rules
