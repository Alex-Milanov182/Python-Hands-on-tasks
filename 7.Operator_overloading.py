

class Distance():
    def __init__(self, meters=0, centimeters=0, millimeters=0):
        self.meters = meters
        self.centimeters = centimeters
        self.millimeters = millimeters

    @property
    def meters(self):
        return self._meters

    @meters.setter
    def meters(self, value):
        self._meters = value

    @property
    def centimeters(self):
        return self._centimeters

    @centimeters.setter
    def centimeters(self, value):
        self._centimeters = value

    @property
    def millimeters(self):
        return self._millimeters

    @millimeters.setter
    def millimeters(self, value):
        self._millimeters = value

    
    def __str__(self):
        return f"{self.meters} m, {self.centimeters} cm, {self.millimeters} mm"

    def __repr__(self):
        return f"Distance(meters={self.meters}, centimeters={self.centimeters}, millimetres={self.millimeters})"

    def __add__(self, other):
        return Distance(
                self.meters + other.meters,
                self.centimeters + other.centimeters,
                self.millimeters + other.millimeters
            )
       
        

    def __sub__(self, other):
        
        total = abs((self.meters*1000 + self.centimeters*10 + self.millimeters) - (other.meters*1000 + other.centimeters*10 + other.millimeters)) 
         
        
        meters = total // 1000          # Get whole meters
        centimeters = (total % 1000) // 10  # Get whole centimeters
        millimeters = total % 10        # Get remaining millimeters
        return f"{meters} m, {centimeters} cm, {millimeters} mm"

    

        

    def __iadd__(self, other):
        
            self.meters += other.meters
            self.centimeters += other.centimeters
            self.millimeters += other.millimeters
            return self


    def __isub__(self, other):
            
            total = abs((self.meters*1000 + self.centimeters*10 + self.millimeters))
            total2 = abs((other.meters*1000 + other.centimeters*10 + other.millimeters))
            total -= total2

            meters = total // 1000          # Get whole meters
            centimeters = (total % 1000) // 10  # Get whole centimeters
            millimeters = total % 10        # Get remaining millimeters
            return f"{meters} m, {centimeters} cm, {millimeters} mm"
 

    
    
def main():
    dist_a = Distance(1, 55, 33)  
    dist_b = Distance(3, 0, 0)
    dist_c = dist_a + dist_b
    dist_d = dist_a - dist_b
    
    
    
    dist_b -= dist_a
    print(dist_a)
    print(dist_b)
    print(dist_d)

    


if __name__ == "__main__":
    main()
