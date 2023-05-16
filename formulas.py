def bar_to_m_h2o(bar):
    m=bar*10
    return m

# Author: Animish Murthy
# Date: 18/05/23

def efficiency(h,q,sg,eta,p):
    effi=(h*q*sg)/(367*eta*p)
    return effi

def ratedq(n1,n2,q1):
    q2=(n2/n1)*q1
    return q2

def ratedh(n1,n2,h1):
    h2=((n2/n1)**2)*h1
    return h2

def ratedp(n1,n2,p1):
    p2=((n2/n1)**3)*p1
    return p2

# Author: Animish Murthy
# Date: 18/05/23
