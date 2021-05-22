from itertools import product
alpha= {
   "a" : 0,
   "b" : 1,
   "c" : 2,
   "d" : 3,
   "e" : 4,
   "f" : 5,
   "g" : 6,
   "h" : 7,
}

def knight_moves(init_pos,final_pos):
    x1,y1=list(init_pos.strip())
    #print(y1)
    y=int(y1)-1
    #print(y)
    x=alpha[x1]
    #print(x)

    x2,y2=list(final_pos.strip())

    y2=int(y2)-1

    x2=alpha[x2]
    final_pos=(x2,y2)

    total_moves = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))

    valid_moves=[]
    for x,y in total_moves:
        #print(x,y)
        if x>=0 and y>=0 and x<8 and y<8:
            xy=(x,y)
            valid_moves.append(xy)
    #print(valid_moves)
    f=0
    for i in valid_moves:
        
        if i==final_pos:
            print('valid')
            f=1

    if f==0:
        print('not valid')
        
# enter your move here
knight_moves('a5','c6')