# Rules Engine
### Create complex rules from data structures to return a dependency graph

# Sample Rule
    Day of entering information: 9/4/2023
    Time to leave: January 9 2024 
        - passport : 90,
            --getId: 40, 
            --money: 37, 
        - ticket : 80, 
        - hotel : 30,

# Sample Result
    Leave on 1/9/2024
        - get passport on 5/1/2023
            -- get id on 4/1/2023


# Installing

    $ git clone [ALEX DO THIS]
    $ pip install -r requirements.txt
