global CLASSES
CLASSES = [] 

def Reg(cls):
    if type(cls) == type([]):
        CLASSES.extend(cls)
    else:
        CLASSES.append(cls)