import logging

logging.basicConfig(filename='Automation\\files\\logs.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.DEBUG) # disables any logging.debug calls

logging.debug('Program Start')

def factorial(n):
    logging.info('Start of factorial(%s)' % (n))
    total = 1
    #for i in range(n + 1): range starts at zero if you dont specify two values so it starts multiplying by 0 instead of 1
    for i in range(1, n + 1):
        total *= i
        logging.info('i is %s, total is %s' % (i,total))
    logging.info('Return value is %s' % total)    
    return total

print(factorial(5))

logging.debug('Program End')
        