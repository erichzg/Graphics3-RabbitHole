from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for pair in range( len(matrix)/2 ):
        x0 = matrix[2*pair][0]
        y0 = matrix[2*pair][1]
        x1 = matrix[2*pair + 1][0]
        y1 = matrix[2*pair + 1][1]
        #print("x0: " + str(x0) + ", y0: " + str(y0))
        #print("x1: " + str(x1) + ", y1: " + str(y1))
        draw_line(x0, y0, x1, y1, screen, color)

def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point( matrix, x0, y0, z0 )
    add_point( matrix, x1, y1, z1 )

def add_point( matrix, x, y, z=0 ):
    matrix.append( [x, y, z, 1] )

def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = math.trunc( x0 )
    y0 = math.trunc( y0 )
    x1 = math.trunc( x1 )
    y1 = math.trunc( y1 )

    if (x0 > x1):
        x = x1
        x1 = x0
        x0 = x
        y = y1
        y1 = y0
        y0 = y
    else:
        x = x0
        y = y0
        
    if (x1 == x0):
        if (y1 > y0):
            while (y <= y1):
                plot(screen, color, x, y)
                y += 1
            return
        while (y >= y1):
            plot(screen, color, x, y)
            y -= 1
        return
    
    A = y1-y0
    B = x0-x1

    if ((-1.0) * A/B >= 1):
        d = A + 2 * B
        while (y <= y1):
            plot(screen, color, x, y)
            if (d < 0):
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B

    elif ((-1.0) * A/B >= 0):
        d = 2 * A + B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d > 0):
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A

    elif ((-1.0) * A/B <= -1):
        d = A - 2 * B
        while (y >= y1):
            plot(screen, color, x, y)
            if (d > 0):
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B
            
    elif ((-1.0) * A/B < 0):
        d = 2 * A - B
        while (x <= x1):
            plot(screen, color, x, y)
            if (d < 0):
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
    
        
