
# * CLASS FOR MAKING CUBES #####################################################################

class Cubes:

    def __init__(self, color : str, volume : int): # &  WHEN WE CREATE AN OBJECT
         
         self.color  = color  # ~ SETTING THE OBJECT COLOR TO BE EQUAL TO THE FIRST VALUE IN THE PARENTHES
         self.volume = volume # ~ SETTING THE OBJECT VOLUME TO BE EQUAL TO THE SECOND VALUE IN THE PARENTHES

    def get_color(self):      # & Gives the color of the cube
         return self.color

    def get_volume(self):     # & Gives the volume of the cube
         return self.volume    

    def __add__(self, other): # & WHEN TWO OBJECTS ARE ADDED 
        
        if self.__class__ == other.__class__:     # ~ IF THE TWO OBJECTS ARE THE SAME CLASS
            return self.volume + other.volume
        
        else:                                     # ~ IF THE TWO OBJECTS AREN'T THE SAME CLASS
             return "On ne mélange pas les chiens et les chats"
        
# * CLASS FOR MAKING CIRCLES ###################################################################

class Circles:

    def __init__(self, color : str, volume : int, radius : int):
         self.color  = color
         self.volume = volume
         self.radius = radius

    def get_color(self):
         return self.color

    def get_volume(self):
         return self.volume
    
    def get_radius(self):
         return self.radius

    
    def __add__(self, other):
         if self.__class__ == other.__class__:
            
            return {                                       # ~ USING A DICTIONARY TO RETURN BOTH VALUES
                 "volume": self.volume + other.volume,
                 "radius" : self.radius + other.radius,   
                    }
         else:
              return "On ne mélange pas les chiens et les chats"


# ! MAIN ################################################################################

green_cube : Cubes = Cubes("Vert",8)    # ~ CREATING CUBES
red_cube   : Cubes = Cubes("Red", 10)


yelllow_circle : Circles = Circles("Yellow",10,5)    # ~ CREATING CIRCLES
purple_circle  : Circles = Circles("Purple",25,10)

print(f"Couleur: {green_cube.get_color()}\nVolume: {green_cube.get_volume()}\n ") # ~ USING GETTERS TO FIND THE COLOR AND VOLUME OF AN OBJECT


print(green_cube + red_cube)            # ~ ADDING TWO CUBES
print(green_cube + yelllow_circle + "\n")      # ~ ADDING A CUBE AND A CIRCLE

print(yelllow_circle + purple_circle)   # ~ ADDING TWO CIRCLES



