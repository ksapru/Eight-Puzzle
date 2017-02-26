#
# board.py (Final Project)
#
# A Board class for the Eight Puzzle
#
# name: Sophia Fondell
# email: sfondell@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: Danielle Yoseloff
# partner's email: yoseloff@bu.edu
#

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[0] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.

        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = int(digitstr[3*r + c])
                if int(digitstr[3*r + c]) == 0:
                       self.blank_r = r
                       self.blank_c = c
                       
        ### Add your other method definitions below. ###
                       
    def __repr__(self):
        '''A method that returns a string representation of a board object
        '''
        string = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == 0:
                    string += '_ '
                else:
                    string += str(self.tiles[r][c]) + ' '
            string += '\n'

        return string

    def move_blank(self, direction):
        '''A method that takes as input a string direction that specifies the
        direction in which the blank should move and that attempts to modify
        the contents of the called Board object accordingly
        '''
        directions = 'up down left right'
        if direction not in directions:
            print('Please enter a valid direction')
            return False
        
        row = self.blank_r
        col = self.blank_c
        
        if direction == 'up':
            if row - 1 >= 0:
                number = self.tiles[row - 1][col]
                blank = self.tiles[row][col]
                self.tiles[row - 1][col] = blank
                self.tiles[row][col] = number
                self.blank_r = row - 1
                return True
            else:
                return False
        elif direction == 'down':
            if row + 1 <= len(self.tiles) - 1:
                number = self.tiles[row + 1][col]
                blank = self.tiles[row][col]
                self.tiles[row + 1][col] = blank
                self.tiles[row][col] = number
                self.blank_r = row + 1
                return True
            else:
                return False
        elif direction == 'left':
            if col - 1 >= 0:
                number = self.tiles[row][col - 1]
                blank = self.tiles[row][col]
                self.tiles[row][col - 1] = blank
                self.tiles[row][col] = number
                self.blank_c = col - 1
                return True
            else:
                return False
        elif direction == 'right':
            if col + 1 <= len(self.tiles[0]) - 1:
                number = self.tiles[row][col + 1]
                blank = self.tiles[row][col]
                self.tiles[row][col + 1] = blank
                self.tiles[row][col] = number
                self.blank_c = col + 1
                return True
            else:
                return False

    def digit_string(self):
        '''A method that creates and returns a string of digits that
        corresponds to the current contents of the called Board object's
        tiles attribute
        '''
        string = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                string += str(self.tiles[r][c])

        return string

    def copy(self):
        '''A method that returns a newly-constructed Board object that is a
        deep copy of the called object
        '''
        new_board = Board(self.digit_string())
        return new_board

    def num_misplaced(self):
        '''A method that counts and returns the number of tiles in the called
        board object that are not where they should be in the goal state
        '''
        goal = '012345678'
        count = 0
        current_board = self.digit_string()
        for x in range(len(goal)):
            if int(goal[x]) == 0:
                pass
            elif goal[x] != current_board[x]:
                count += 1
        return count

    def distance(self):
        '''A method that counts and returns the total distance that all of the
        tiles are away from their goal spots
        '''
        goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                 for r1 in range(len(goal)):
                    for c1 in range(len(goal[0])):
                         if self.tiles[r][c] == goal[r1][c1]:
                             a = abs(r - r1)
                             b = abs(c - c1)
                             d = a + b
                             count += d
        return count

    def __eq__(self, other):
        '''A method that overloads the == operator creating a version of the
        operator that works for board objects, returns True if the called object
        (self) and the argument(other) have the same values for the tiles
        attribute and false otherwise
        '''
        if self.tiles == other.tiles:
            return True
        else:
            return False
                            
        
    
            
        
        
            
            

    

    
