# Rules Engine
### The Rules Engine is a powerful tool that allows you to create complex rules from data structures, enabling you to generate a dependency graph. It provides a flexible and efficient way to model dependencies and relationships within your data.

# Sample Rule
    Time to leave: January 9 2024 
        - meet: 90, --deliver: 40, --email: 37, - document : 80, - build: 30

# Sample Result
    Leave on 1/9/2024
        ['meeting: 10/11/23', 'deliver: 09/01/23', 'email: 09/04/23', 'document: 10/21/23', 'build: 12/10/23']


# Installing

    $ git clone https://github.com/techycereal/Event-AI.git
    $ python3 -m venv venv
    $ source /venv/bin/activate
    $ pip install -r requirements.txt

#Generate Data
    $ python3 generate.py

#Train the model
    $ python3 plan.py     --model_name_or_path google/flan-t5-small     --do_train     --do_eval     --train_file train.json     --validation_file test.json     --source_prefix "order: "     --output_dir tst-summarization     --overwrite_output_dir     --per_device_train_batch_size=4     --per_device_eval_batch_size=4     --predict_with_generate

#Run the Flask App
    $ export FLASK_APP=flask_app.py
    $ python3 -m flask run
