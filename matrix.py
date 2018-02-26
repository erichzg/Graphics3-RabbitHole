import math


def print_matrix( matrix ):
    for r in range( len(matrix[0]) ):
        print( [matrix[c][r] for c in xrange(len(matrix))] )
    print( "\n" )
    return

def ident( matrix ):
    for c in range( len(matrix) ):
        for r in range( len(matrix[0]) ):
            if (c == r):
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0
    return

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    new_one = new_matrix( len( m2[0] ), len( m2 ) )
    for c in range( len(m2) ):
        for r in range( len(m2[0]) ):
            dot_row =  [m1[x][r] for x in xrange(len(m1))]
            new_one[c][r] = dot_product( dot_row, m2[c] )
    for c in range( len(m2) ):
        for r in range( len(m2[0]) ):
            m2[c][r] = new_one[c][r]

def dot_product( l1, l2 ):
    product = 0.0
    if (len(l1) != len(l2)):
        print("Invalid dot product")
        return
    for i in range( len(l1) ):
        product += l1[i] * l2[i]
    return product



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
