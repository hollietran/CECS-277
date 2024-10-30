class Map:
    _instance = None

    def __new__(cls):
        # if the map hasn't been constructed, then construct it and store it in the instance class variable and return it
        # if it has, then just return the instance
        if cls._instance == None:
            cls._instance = super(Map, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        # Create and fill the 2D map list from the file contents.
        # The map stores the contents of the file and the revealed list is useed to determine whether the contents of the map are displayed or not ('x' if not displayed).
        if not hasattr(self, 'map'):
            self.map = self._load_map_from_file()  # Assuming this loads your map layout
            self.revealed = [[False for _ in range(len(self.map[0]))] for _ in range(len(self.map))]
            # Reveal the start position (0, 0)
            self.revealed[0][0] = True

    def _load_map_from_file(self):
        # Loads the map data from a file and returns a 2D list
        map_data = []
        with open("map.txt", "r") as file:
            for line in file:
                map_data.append(list(line.strip()))
            return map_data
        
    def __getitem__(self, row):
        # overloaded [] operator -- returns the specified row from the map
        # Notes: his operator can be used to access a row (ex. m[r]) or can be used to access a value at a row and column (ex. m[r][c])
        return self.map[row]

    def __len__(self):
        # returns the number of rows in the map list.
        # Notes: if you want to know the number of rows, use len(m) and column is len(m[r])
        return len(self.map)

    def show_map(self, loc):
        # returns the map as a string in the format of a 5x5 matrix of characters
        # Unrevealed locations are 'x' and the hero's location is a '*'

        display_map = []

        for row in range(len(self.map)):
            display_row = []
            for col in range(len(self.map[row])):
                if (row, col) == loc:
                    display_row.append('*')  # Hero's position
                elif self.revealed[row][col]:
                    display_row.append(self.map[row][col])  # Revealed map location
                else:
                    display_row.append('x')  # Unrevealed locations
            display_map.append(' '.join(display_row))
        return '\n'.join(display_map)
    
    def reveal(self, loc):
        # sets the value in the 2D revealed list at the specified location to True
        row, col = loc
        self.revealed[row][col] = True

    def remove_at_loc(self, loc):
        # overwrties the character in the map list at the specified location with an 'n'
        row, col = loc
        self.map[row][col] = 'n'
    
    