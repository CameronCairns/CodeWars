def traverse_nodes(matrix, position, x, y, visited, traversal):
    while(position[0]+y < len(matrix) and
          position[1]+x < len(matrix[0]) and
          matrix[position[0]+y][position[1]+x][1] != True):
        matrix[position[0]][position[1]][1] = True
        traversal.append(matrix[position[0]][position[1]][0])
        position[0] += y
        position[1] += x
        visited += 1
    return visited, position

def snail(array):
    total_nodes = sum(len(sub_array) for sub_array in array)
    visited = 0
    traversal = []
    pos = [0, 0]
    matrix = [[[node, False] for node in sub_array] for sub_array in array]
    while(visited < total_nodes-1):
        visited, pos = traverse_nodes(matrix, pos, 1, 0, visited, traversal) #Traverse right
        visited, pos = traverse_nodes(matrix, pos, 0, 1, visited, traversal)#Traverse down 
        visited, pos = traverse_nodes(matrix, pos, -1, 0, visited, traversal)#Traverse left
        visited, pos = traverse_nodes(matrix, pos, 0, -1, visited, traversal)#Traverse up
    if(pos[0] < len(matrix) and pos[1] < len(matrix[0])):
        traversal.append(matrix[pos[0]][pos[1]][0])
    return traversal

if __name__ == '__main__':
    array = [[1,2,3],
             [4,5,6],
             [7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    print(snail(array), expected)

# BEST SOLUTION SUBMITTED
#def snail(array):
#    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
