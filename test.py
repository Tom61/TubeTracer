from ttcCalc import BendedTube


points = [[  0.0,    0.0,   0.0,  0.0],
          [-50.0,    0.0,   0.0, 20.0],
          [-40.0,  -40.0,  20.0, 20.0],
          [-40.0,  -40.0,  50.0, 20.0],
          [-70.0,  -60.0,  80.0, 20.0],
          [-70.0, -120.0,  70.0, 20.0],
          [-80.0, -120.0, 200.0, 20.0],
          [-40.0, -155.0, 200.0,  0.0]]


myTube = BendedTube(points)

print ()
print ('Gerade Längen ')
print (myTube.getStraightLengths())
print ()
print ('Biegewinkel ')
print (myTube.getBendingAngles())
print ()
print ('Bogenlängen ')
print (myTube.getBowLengths())
print ()
print ('Gesamtlänge = ',myTube.getTotalLength())
