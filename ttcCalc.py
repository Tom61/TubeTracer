from numpy import pi, arccos, tan

class BendedTube:
    
    def __init__(self, points=False):
        self.p = points
        if points:
            self.calc()
        
    def length_of_line(self, p1, p2):
        l = 0
        for i in range(3):
            l += (p1[i]-p2[i])**2
        return l**0.5
        
    def calc(self):
        #theoretical lengths from point to point
        self.theoretic_len = list((map(self.length_of_line, self.p, self.p[1:])))
        
        #lengths of ledger lines to solve cosin theorem in the next step
        self.ledger_len = list((map(self.length_of_line, self.p, self.p[2:])))
        
        #angle (in radians)  between lines. Calc. by cosin theorem
        self.angle = list(map(lambda a,b,c: arccos((a**2-b**2-c**2)/(-2*b*c)),
                              self.ledger_len, self.theoretic_len, self.theoretic_len[1:]))
        
        #bending angle (in degree)
        self.bending_angle = [(pi-angle)*360/2/pi for angle in self.angle]
        
        #bow lengths
        self.bow_len = list(map(lambda radius, bend_angle: 2*pi*radius/360*bend_angle,
                                [p[3] for p in self.p if p[3]>0], self.bending_angle))
        
        #"cut off" or "over length" (from tangent point to coordinate point)
        self.over_len = list(map(lambda radius, angle: radius/tan(angle/2),
                                 [p[3] for p in self.p if p[3]>0], self.angle))
        
        #calc the true lengths of the straights
        self.real_len = self.theoretic_len.copy()
        for i in range(len(self.over_len)):
            self.real_len[i] -= self.over_len[i]
            self.real_len[i+1] -= self.over_len[i]
            
        #calc the total length
        self.len_sum = sum(self.real_len) + sum(self.bow_len)

    def setPoints(self, points):
        self.p = points
        self.calc()
        return

    def getTotalLength(self):
        return self.len_sum
    
    def getStraightLengths(self):
        return self.real_len
    
    def getBowLengths(self):
        return self.bow_len
    
    def getBendingAngles(self):
        return self.bending_angle
    
    def getResultSet(self):
        return self.len_sum, self.real_len, self.bow_len, self.bending_angle
