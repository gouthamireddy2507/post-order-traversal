tt2= (6,(5,(),()),(4,(),()))
tt1= (7,(3,(),()),(2,(),()))
tt = (9, tt1,tt2)

def postorder1(pts,sofarl):
    if pts==[]:
        return sofarl
    else:
        (t,ts) = (pts[0],pts[1:])
        if t[1] ==() and  t[2]  == ():
            sofarl = sofarl +[t[0]]
        else:
            (n,lt,rt) = t
            ts = [lt] +[rt] +  [(n,(),())] + ts
            sofarl = sofarl
    return postorder1(ts,sofarl)

def postorder2(t,sofar2):
    if t[1] == () and t[2] == ():
        return sofar2 + [t[0]]
    else:
        return postorder(t[2],(postorder(t[1],(sofar2)))) + [t[0]]

def postorder3(pts, sofar3):
    if pts == []: return sofar3
    else:
        (t,ts) = (pts[0], pts[1:])
        if t(1) ==() and t[2] == ():
            sofar3 = sofar3 + [t[0]]        
        else:
            (n,lt,rt) = t
            ts = [lt] + [rt] + [(n,(),())] + ts
            sofar3 = sofar3
    return postorder3(ts, sofar)
    
def postorder4(t):
    pts = [t]
    sofarl = []
    while (pts !=[]):
        (t,ts) = (pts[0],pts[1:])
        if t[1] ==() and  t[2]  == ():
                  sofarl = sofarl +[t[0]]
                  pts = ts
        else:
                (n,lt,rt) = t
                pts = [lt] + [rt] + [(n,(),())] + ts
    return sofarl


