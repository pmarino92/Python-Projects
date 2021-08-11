
class Bird: #blueprint for a bird
    name = "No Name Given"
    feather_color = ""
    beak_color = ""

    def fly(self):
        print("Some birds can fly and some can not")
        
    def walk(self):
        print("Walking")

class Eagle(Bird): #Creating a child class: Eagle
    name = "Bald Eagle"
    feather_color = "Black and White"
    beak_color = "Yellow"
    wing_span = "6 feet"
    weight = "17 pounds"
    
    def fly(self): #Using polymorphism here to change parent method
        print("Bald Eagles can in fact fly")

    def walk(self): #Using polymorphism here to change parent method
        print("Bald Eagles look ridiculous when they walk")

class Ostrich(Bird): #Creating another a child class: Ostrich
    name = "Ostrich"
    feather_color = "Gray"
    beak_color = "Yellow and Red"
    top_speed = "43 mph"
    height = "7 ft"

    def fly(self): #Using polymorphism here to change parent method
        print("Ostriches are unable to fly")

    def walk(self): #Using polymorphism here to change parent method
        print("Ostriches are superb runners") 
    
        












if __name__ == "__main__":
    eagle = Eagle()
    print(eagle.fly())
    print(eagle.walk())

    ostrich = Ostrich()
    print(ostrich.fly())
    print(ostrich.walk())
