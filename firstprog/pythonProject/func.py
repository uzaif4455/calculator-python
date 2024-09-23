'''def complicate_func(x,y,*args):
    print(x,y,args)

complicate_func(1,2,4,5,5,6,6.6,6,44,3,2,2,1,)'''
#output:1 2 (4, 5, 5, 6, 6.6, 6, 44, 3, 2, 2, 1)

#def args and kwargs
# def complicate_func(*args,**kwargs):
#     print(args,kwargs)
#
# complicate_func(1,2,3,4,x="10",book="80rs",day="sunday")#output:(1, 2, 3, 4)
# {'x': '10', 'book': '80rs', 'day': 'sunday'}
'''def complicate_func(a,b,c= False,d= True):
    print(a,b,c,d)

complicate_func(*[1,2],**{"c":"hello","d":"fine"})'''
            #ye upar ka *args hai or ye **kwargs hai
# (The args stands for arguments that are passed to the function whereas kwargs stands
# for keyword arguments which are passed along with the values into the function.)
