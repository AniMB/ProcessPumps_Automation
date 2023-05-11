def grapher(data):
    import matplotlib.pyplot as plt
    from matplotlib import style
    
    
    x1=[]
    y1=[]
    y2=[]
    y3=[]
    fig, ax=plt.subplots()
    fig.subplots_adjust(left=0.25)
    
    ax1=ax.twinx()
    ax2=ax.twinx()
    ax2.spines["left"].set_position(("axes", -0.2))
    ax2.yaxis.tick_left()
    ax2.yaxis.set_label_position("left")
    ax2.spines["left"].set_visible(True)
    
    for i in data:
        
        x = i[0]  
        x1.append(x)
        y = i[1]
        y1.append(y)
        y_=i[2]
        y2.append(y_)
        y__=i[3]
        y3.append(y__)
    
    p1,=ax.plot(x1, y1, 'g',label='Head')
    p2,=ax1.plot(x1,y2,'b-', label='Power')
    p3,=ax2.plot(x1,y3,'r-', label='Efficiency')
    
    
    ax.set_xlabel('Capacity')
    ax.set_ylabel('Head')
    ax1.set_ylabel('Power')
    ax2.set_ylabel('Efficiency')
    
    
    ax.legend(handles=[p1, p2, p3])
    
    plt.grid(True, color='#000')
    plt.show()
# refer to this'https://matplotlib.org/3.4.3/gallery/ticks_and_spines/multiple_yaxis_with_spines.html'
# and https://stackoverflow.com/questions/58337823/matplotlib-how-to-display-and-position-2-yaxis-both-on-the-left-side-of-my-grap
