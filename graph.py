def grapher(data,gh):
    import matplotlib.pyplot as plt
    from matplotlib import style
    
    style.use('ggplot') # set plot style
    x1=[]
    y1=[]
    y2=[]
    for i in data:
        
        x = i[2]  
        x1.append(x)
        y = i[0]+i[1]+gh
        y1.append(y)
        y_=i[4]
        y2.append(y_)
    
    plt.plot(x1, y1, 'g')
    plt.plot(x1,y2)
    plt.grid(True, color='w')
    plt.show()
