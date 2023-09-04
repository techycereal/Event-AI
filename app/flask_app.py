from flask import Flask, request, render_template  # Import necessary modules from Flask.
import app_process  # Import the process_app module.

app = Flask(__name__)  # Create a Flask web application.

@app.route('/', methods=['GET', 'POST'])  # Define a route for '/' and allow GET and POST requests.
def submit():
    # Handle the POST request
    if request.method == 'POST':
        input_rules = request.form.get('rules')  # Get the 'rules' input value from the POST request.
        input_time = request.form.get('time')  # Get the 'time' input value from the POST request.
        
        # Call the 'process' function from the 'app_process' script, passing 'input_rules' and 'input_time' as arguments.
        result_rule = app_process.process_input(input_rules, input_time)
        print(result_rule)  # Print the 'result_rule' variable to the server log for debugging purposes.
        
        # Render an HTML template 'post.html' and pass 'input_time' and 'result_rule' as variables to the template.
        return render_template('post.html', time=input_time, rule=result_rule)

    # Otherwise, handle the GET request
    return render_template('index.html')  # Render an HTML template 'index.html' for the GET request.