from numpy import pi, arccos, tan

class BendedTube:
    
     def lineLength(self, line):
        length = 0
        for i in range(3):
            length += (line[0][i]-line[1][i])**2
        length = length**0.5
        return length
    
     def getResultSet (self, points):
         
        #theoretical lengths of lines
        theoretical_len = []
        for i in range (len(points)-1):
            theoretical_len.append(self.lineLength((points[i], points[i+1])))
        real_len = list(theoretical_len)
        
        #bending-angle & bow-length & real-length
        angle = []
        bend_angle = []
        bow_len = []
        for i in range (1, len(points)-1):
            a = self.lineLength((points[i-1],points[i+1]))
            # a = ledger line for cosin theorem
            b = theoretical_len[i-1]
            c = theoretical_len[i]
            angle.append(arccos((a**2-b**2-c**2)/(-2*b*c)))
            bend_angle.append((pi-angle[i-1])*360/2/pi)
            bow_len.append(pi*2*points[i][3]/360*bend_angle[i-1])
            over_len = points[i][3]/tan(angle[i-1]/2)
            real_len[i-1] -= over_len
            real_len[i] -= over_len
        len_Sum = (sum(real_len)+sum(bow_len))
        return len_Sum, real_len, bow_len, bend_angle


tube = BendedTube()

# INPUT POINTn [Xn, Yn, Zn, RADIUSn]

points = [[  0.0,    0.0,   0.0,  0.0],
          [-49.1,    0.0,   0.0, 20.0],
          [-39.7,  -41.0,  20.6, 20.0],
          [-39.7,  -38.8,  49.6, 20.0],
          [-72.7,  -59.8,  80.0, 20.0],
          [-72.7, -122.9,  71.7, 20.0],
          [-78.1, -119.3, 201.6, 20.0],
          [-37.0, -154.4, 199.8,  0.0]]

result = tube.getResultSet(points)

print ('straight length 1 ={0:7.1f}'.format(result[1][0]))
for i in range (len(points)-2):
    print ('bow length.....{0:2} ={1:7.1f}  (bend.Angle = {2:5.1f} Degree'
           .format(i+1,result[2][i],result[3][i]))
    print ('straight length{0:2} ={1:7.1f}'.format(i+2,result[1][i+1]))
print (28*'-')
print ('SUM LENGTH....... ={0:7.1f}'.format(result[0]))
print (28*'=')
                           


