# Rules Engine
### Create complex rules from data structures to return a dependency graph

# Sample Rule
    travel to Japan, 
        - passport : 113 
            --getId: 90 
            --money: 67 
                ---makeMoney: 169, 
        - ticket : 99, 
        - hotel : 14, 
        - vaccine : 32

# Sample Result
    travel to Japan on 7/12/2023
        - get passport on 5/1/2023
            -- get id on 4/1/2023


# Installing

    $ git clone [ALEX DO THIS]
    $ pip install -r requirements.txt

# Code sample
    
    import Processapp
   
    rules = """- passport : 113 
            --getId: 90 
            --money: 67"""
    time = 'July 12 2023'
            
    #gets the time and passes the rules variable in from the processData function in Processapp script
    json_data, json_datas, event_date = Processapp.processData(rules, time)
    
    #gets the complete rules from the processTime function in Processapp script
    processTime = Processapp.processTime(json_data, json_datas, event_date)

    print(processTime)
