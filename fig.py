import math
	class Figura():
	    
	    def __init__(self):
	        pass
	    def dame_area(self): 
	        return None
	    def dame_perimetro(self):
	        return None
	    
	
	class Circulo(Figura):
	    def __init__(self, radio):
	        self.radio=radio
	    def dame_area(self):
	        area=math.pi*self.radio**2
	        return area
	        
	circulo1=Circulo(1)
	print (circulo1.dame_area())
