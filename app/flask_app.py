from flask import Flask, request, render_template
import Processapp
app = Flask(__name__)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        rules = request.form.get('rules')
        time = request.form.get('time')
        #gets the time and passes the rules variable in from the processData function in Processapp script
        rule = Processapp.process(rules, time)
        print(rule)
        #puts the info on the webapp
        return render_template('post.html', time=time, rule=rule)

    # otherwise handle the GET request
    return render_template('index.html')