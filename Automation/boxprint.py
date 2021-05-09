import traceback

def boxPrint(symbol, w, h):
    try:
        if len(symbol) != 1:
            raise Exception('"symbol" needs to be a string of length 1')
        if (w < 2) or (h < 2):
            raise Exception('w or h need to be greater than or equal to 2')
    except:
        errFile = open('Automation\\files\\log.txt', 'a')
        errFile.write(traceback.format_exc())
        errFile.close()
        print('Traceback info was written to log.txt')
        
    print(symbol * w)
    
    for i in range (h - 2):
        print(symbol + (' ' * (w - 2)) + symbol)
        
    print(symbol * w)

boxPrint('!', 5, 10)
boxPrint('*', 10 , 5)
#boxPrint('*!', 10 , 5)
boxPrint('*', 1 , 1)