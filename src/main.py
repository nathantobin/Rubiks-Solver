from CubeFace import CubeFace
from Cube import Cube

def main():
    white_face   = CubeFace('white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white')
    red_face     = CubeFace('red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red')
    blue_face    = CubeFace('blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue')
    orange_face  = CubeFace('orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange')
    green_face   = CubeFace('green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green')
    yellow_face  = CubeFace('yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow')
    cube = Cube(white_face, red_face, blue_face, orange_face, green_face, yellow_face)
    
if __name__ == "__main__":
    main()