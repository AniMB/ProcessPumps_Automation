def grapher(data):
    import matplotlib.pyplot as plt
    from matplotlib import style
    import numpy as np
    from scipy.interpolate import make_interp_spline
    
    
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
        x1.append(float(x))
        y = i[1]
        y1.append(float(y))
        y_=i[2]
        y2.append(float(y_))
        y__=i[3]
        y3.append(float(y__))
    
    X_ = np.linspace(min(x1), max(x1), 10000)
    # for head and capacity
    X_Y1_Spline = make_interp_spline(x1, y1)
    
    Y1_ = X_Y1_Spline(X_)
    
    # for Power and capacity
    X_Y2_Spline = make_interp_spline(x1, y2) 
    Y2_ = X_Y2_Spline(X_)
    
    # for Efficiency and capacity
    X_Y3_Spline = make_interp_spline(x1, y3)
    Y3_ = X_Y3_Spline(X_)
    
    
    p1,=ax.plot(X_, Y1_, 'g-',label='Head')
    ax.scatter(x1, y1, c='g', alpha=0.5, marker='o') # type: ignore
    p2,=ax1.plot(X_,Y2_,'b-', label='Power')
    ax1.scatter(x1, y2, c='b', alpha=0.5, marker='p') # type: ignore
    p3,=ax2.plot(X_,Y3_,'r-', label='Efficiency')
    ax2.scatter(x1, y3, c='r', alpha=0.5, marker='x') # type: ignore
    
    ax.set_xlim(0, (max(x1)*1.1))
    ax.set_ylim(0, (max(y1)*1.1))
    ax1.set_ylim(0, (max(y2)*1.1))
    ax2.set_ylim(0, (max(y3)*1.1))
    
    
    
    ax.set_xlabel('Capacity')
    ax.set_ylabel('Head')
    ax1.set_ylabel('Power')
    ax2.set_ylabel('Efficiency')
    
    
    ax.legend(handles=[p1, p2, p3])
    def map_range(value, old_min, old_max, new_min, new_max):
    
    # Maps a value from the old range [old_min, old_max] to the new range [new_min, new_max]
    
        old_range = old_max - old_min
        new_range = new_max - new_min
        scaled_value = (value - old_min) / old_range
        return new_min + (scaled_value * new_range)


    def onclick(event,x1,y3):
                   
        duty_point_x= event.xdata
        duty_point_y=event.ydata
        ax.plot([duty_point_x,duty_point_x],[duty_point_y, 0], 'C8--')
        plt.plot([duty_point_x, 0],[duty_point_y, duty_point_y], 'C8--')
        ax.annotate(f'{map_range(duty_point_x,0, (max(y3)),0, (max(x1))):.2f}', xy=(duty_point_x, 0), xytext=(duty_point_x+0.5, 0.5), )
        plt.annotate(f'{duty_point_y:.2f}', xy=(0, duty_point_y), xytext=(0.5, duty_point_y+0.5))
        plt.scatter([duty_point_x], [duty_point_y], s=100)
        plt.show()
    
    ax.figure.canvas.mpl_connect('button_press_event', lambda event :onclick(event, x1, y3))
        
        
    
    
    plt.grid(True, color='#5F2D9A')
    plt.show()
    
# refer to this'https://matplotlib.org/3.4.3/gallery/ticks_and_spines/multiple_yaxis_with_spines.html'
# and https://stackoverflow.com/questions/58337823/matplotlib-how-to-display-and-position-2-yaxis-both-on-the-left-side-of-my-grap
# bottom limit should be zero for all
