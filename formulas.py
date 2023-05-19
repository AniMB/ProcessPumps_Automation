def bar_to_m_h2o(bar):  # convert the value in bars to m
    m=bar*10
    return m

# Author: Animish Murthy
# Date: 18/05/23

def efficiency(h,q,sg,eta,p):  # Calculates the efficiency 
    effi=(h*q*sg)/(367*eta*p)
    return effi

def ratedq(n1,n2,q1):   # Calculates the proportionate capacity with respect to the RPM
    q2=(n2/n1)*q1
    return q2

def ratedh(n1,n2,h1):  # Calculates the proportionate head with respect to the RPM
    h2=((n2/n1)**2)*h1
    return h2

# Author: Animish Murthy
# Date: 18/05/23

def ratedp(n1,n2,p1):  # Calculates the proportionate power with respect to the RPM
    p2=((n2/n1)**3)*p1
    return p2


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



