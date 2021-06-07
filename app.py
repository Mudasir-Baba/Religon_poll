poll = {}
pooling_is_going = True

while pooling_is_going:
    name = input('What is your name: ')
    response = input('What is your religon: ')
    poll[name] = response

    repeat = input('Would you like to pass this poll to another person(Yes/no): ').lower()
    if repeat == 'no':
        pooling_is_going = False

religons = []
print('\nThe polling is complete. \nThe results are below: ')
for name, response in poll.items():
    print(f'{name.title()} follows {response.title()}')
    
# You can also create an empty list "religons" and append it the values of dictionaries i.e the religons and then 
# compare which religon repeats the most times and declare it the most abundant religon like a real poll.  
