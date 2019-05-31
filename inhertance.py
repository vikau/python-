class car:
    def __init__(self,model_name,year,color):
        self.model=model_name
        self.year=year
        self.color=color

    def view_cars(self):
        print("{0} {1} {2}".format(self.model,self.year,self.color))

class sports_car(car):
    def __init__(self,model_name,year,color,speed):
        super().__init__(model_name,year,color)
        self.speed=speed
    def view_car(self):
          print("{0} {1} {2} {3}".format(self.model,self.year,self.color,self.speed))

jagur=sports_car("jagur",2017,"red",1200)
jagur.view_car()


         
    
