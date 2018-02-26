from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print( "new matrix: " )
print_matrix( matrix )
print( "setting to identity matrix" )
ident( matrix )
print_matrix( matrix )

print( "original edge matrix" )
edge_matrix = [ [1, 2, 3, 1], [4, 5, 6, 1] ]
print_matrix( edge_matrix )

print( "original square matrix" )
square_matrix = [ [7, 8, 9, 10], [11, 12, 13, 14], [15, 16, 17, 18], [19, 20, 21, 22] ]
print_matrix( square_matrix )

print( "square matrix x edge matrix" )
matrix_mult( square_matrix, edge_matrix )
print_matrix( edge_matrix )

print( "adding an edge to the edge matrix" )
add_edge( edge_matrix, 10, 20, 0, 100, 30, 0 )
print_matrix( edge_matrix )

print( "setting edge matrix to 0" )
edge_matrix = new_matrix( 4, 2 )
print_matrix( edge_matrix )

print( "adding a drawing" )
for n in range( 0, 100 ):
    x = 250 + 250 * math.cos( n * 2 * math.pi / 100 )
    y = 250 + 250 * math.sin( n * 2 * math.pi / 100 )
    add_point( edge_matrix, x, y, 0 )
print_matrix( edge_matrix )

draw_lines( edge_matrix, screen, color )
display(screen)
save_extension(screen, 'img.png')
