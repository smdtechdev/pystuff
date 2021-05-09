market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLights(junction):
    for key in junction.keys():
        if junction[key] == 'green':
            junction[key] = 'yellow'
            print(junction[key])
        elif junction[key] == 'yellow':
            junction[key] = 'red'
        elif junction[key] == 'red':
            junction[key] = 'green'
    assert 'red' in junction.values(), 'Neither light is red!' + str(junction)        
 
print(market_2nd)            
switchLights(market_2nd)
print(market_2nd)