from ttcCalc import BendedTube

points = [[  0.0,    0.0,   0.0,  0.0],
          [-50.0,    0.0,   0.0, 20.0],
          [-40.0,  -40.0,  20.0, 20.0],
          [-40.0,  -40.0,  50.0, 20.0],
          [-70.0,  -60.0,  80.0, 20.0],
          [-70.0, -120.0,  70.0, 20.0],
          [-80.0, -120.0, 200.0, 20.0],
          [-40.0, -155.0, 200.0,  0.0]]

class Model:
    
    def __init__(self):
        self.points = []
        self.tube = BendedTube()
        
    def setData(self,points):
        self.points = points
        return
    
    def getData(self):
        return self.points

    def getResult(self):
        self.tube.setPoints(self.points)
        self.result = self.tube.getResultSet()
        return self.result


model = Model()
model.setData(points)
print(model.getResult())




    
    
    
