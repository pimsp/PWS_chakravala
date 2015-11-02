def modinv(n,m):
    """Finds an x with nx + my = 1 (the inverse of n mod m), assuming that ggd(n,m)=1"""
    x_prev = 1
    x = 0
    ggd_prev = n
    ggd = abs(m)
    while ggd!=1:
        ratio = ggd_prev//ggd
        x_prev,x = x,x_prev-ratio*x
        ggd_prev,ggd = ggd,ggd_prev%ggd
    return x%m

def smallest_solution_Pell(d):
    """Finds the smallest positive integers a,b that fulfill Pell's equation: x**2-d*y**2=1, using the Chakravala method"""
    a,b = int(d**0.5)+1,1
    k = a**2-d*b**2
    #print(a,b,k)
    while k!=1:
        m_0 = (-a*modinv(b,k))%k
        m_1 = (int(d**0.5+0.5)//k)*k + m_0
        p_1 = m_1**2-d
        if p_1>0:
            m_2 = m_1 - abs(k)
        else:
            m_2 = m_1 + abs(k)
        p_2 = m_2**2-d
        if abs(p_1)<abs(p_2):
            m = m_1
        else:
            m = m_2
        #print(a,b,k,m_0,m_1,p_1,m_2,p_2,m)
        a,b,k = (a*m+d*b)//abs(k),(a+b*m)//abs(k),(m**2-d)//k
        #print(a,b,k,a**2-d*b**2)
    return [a,b]

class ZfZsqrtd():
    def __init__(self,a,b,d,f=-1):
        if f==-1:
            self.a = a
            self.b = b
        else:
            self.a = a%f
            self.b = b%f
        self.d = d
        self.f = f
    def __add__(self,other):
        if self.d == other.d and self.f == other.f:
            return ZfZsqrtd(self.a + other.a, self.b + other.b, self.d, self.f)
    def __mul__(self, other):
        if self.d == other.d and self.f == other.f:
            return ZfZsqrtd(self.a*other.a + self.d*self.b*other.b, self.a*other.b + self.b*other.a, self.d, self.f)
    def __str__(self):
        if f!=-1:
            return str(self.a)+"+"+str(self.b)+"sqrt{"+str(self.d)+"} (mod "+str(self.f)+")"
        return str(self.a)+"+"+str(self.b)+"sqrt{"+str(self.d)+"}"

def orde(a,f):
    c = a
    count = 1
    while c.b%f != 0:
        c*=a
        count+=1
    return count
