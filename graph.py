def grapher(data, capacity, head):
# this code plots the graph of the rated values


# Author: Animish Murthy
# Date: 18/05/23

    import matplotlib.pyplot as plt
    from matplotlib import style
    import numpy as np
    from scipy.interpolate import make_interp_spline
    
    
    #Sets the initial subplots and creates the twin axes while shifting one a bit further away to have 3 y-axes in total
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
    
    
    #reads the data and creates lists
    for i in data:
        
        x = i[0]  
        x1.append(float(x))
        y = i[1]
        y1.append(float(y))
        y_=i[2]
        y2.append(float(y_))
        y__=i[3]
        y3.append(float(y__))
    
    
    #Here we see that x axis is created and the y values are made into splines with respect to X
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
    
# Author: Animish Murthy
# Date: 18/05/23


    #The values are plotted along with their scatter plots. The scatter plots are stored and unpacked values so that they can be used later
    ax.plot(X_, Y1_, 'g-')
    p1=ax.scatter(x1, y1, c='g', alpha=0.5, marker='o',label='Head') # type: ignore
    ax1.plot(X_,Y2_,'b-')
    p2=ax1.scatter(x1, y2, c='b', alpha=0.5, marker='p', label='Power') # type: ignore
    ax2.plot(X_,Y3_,'r-')
    p3=ax2.scatter(x1, y3, c='r', alpha=0.5, marker='x', label='Efficiency') # type: ignore
    p4=ax.scatter(capacity,head, marker=11, label='Guarenteed Value') # type: ignore
   
    
    #the limts on all the axes are set along with their labels
    ax.set_xlim(0, (max(x1)*1.1))
    ax.set_ylim(0, (max(y1)*1.1))
    ax1.set_ylim(0, (max(y2)*1.1))
    ax2.set_ylim(0, (max(y3)*1.1))

    ax.set_xlabel('Capacity (m\u00b3/hr)')
    ax.set_ylabel('Head(m)')
    ax1.set_ylabel('Power(kW)')
    ax2.set_ylabel('Efficiency(%)')
    
# Author: Animish Murthy
# Date: 18/05/23 

    # here we see the legend
    handles = [p1, p2,p3,p4]
    labels = [p1.get_label(), p2.get_label(), p3.get_label(), p4.get_label()]
    plt.legend(handles, labels,  loc='lower right')

    # the grid is created and the entire thing is plotted
    plt.grid(True, color='#5F2D9A')
    plt.show()
    
#                                        _                                               _
#                                       / \         \"""\		    /"""/       / \
# 				       /   \         \   \		   /   /       /   \
#                                     /     \         \   \		  /   /       /     \
#                                    /   _   \         \   \ 	         /   /       /   _   \
#                                   /   / \   \         \   \           /   /	    /   / \   \
#                                  /   /   \   \         \   \         /   /       /   /   \   \ 
#                                 /   /     \   \         \   \       /   /   	  /   /     \   \
#                                /    """""""    \         \   \     /   /       /    """""""    \ 
#                               /                 \	    \   \   /   /       /                 \
#                              /    /"""""""""\    \	     \   \ /   /       /    /""""""""""\   \
#                             /    /           \    \ 	      \   V   /	      /    /		\   \
#                            /    /             \    \         \     /       /    /		 \   \
#                            """""               """""          """""        """""                """"  
