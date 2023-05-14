
up_s = '|'
down_s = '_'
space = " "

# 8 display 

space_size = 1

class Display():
    def __init__(
        self,
        top = space,
        l1_left = space,
        l1_center = space,
        l1_right = space,
        l2_left = space, 
        l2_center = space,
        l2_right = space,  
    ):
        # [
        #  [" ", "_", " "],  top
        #  ["|", "_", "|"],  l1
        #  ["|", "_", "|"]   l2
        # ]
        #    _
        #   |_|
        #   |_|   
        # 
        #  
         
        self.display_matrix = [
            [space, top, space],
            [l1_left, l1_center, l1_right],
            [l2_left, l2_center, l2_right]
        ]

    def get_matrix(self):
        return self.display_matrix

    def increace_vertical(self, repetitions = 1):
        # Vertical increace add new lines on matrix
        # insert a new vector on display_matrix[n-2] and display_matrix[1]
        vertical_line_up = [" "] * (len(self.display_matrix[0]))
        vertical_line_button = vertical_line_up.copy()
        if self.display_matrix[1][0] is up_s:
            vertical_line_up [0] = up_s
        if self.display_matrix[1][-1] is up_s:
            vertical_line_up[-1] = up_s
        if self.display_matrix[-1][0] is up_s:
            vertical_line_button[0] = up_s
        if self.display_matrix[-1][-1] is up_s:
            vertical_line_button[-1] = up_s
        for r in range(repetitions -1):
            self.display_matrix.insert(1, vertical_line_up)
            self.display_matrix.insert(-1, vertical_line_button)
        return self
        
    def increace_horizontal(self, repetitions=0):
        # This method increace in horizontal inserting 
        # horizontal character in possitions where only can be 
        # horizontal characters, in vector[1] to vector[n-2]
        columns = len(self.display_matrix)
        for i in range(columns):
            h_char = self.display_matrix[i][1]
            for r in range(repetitions):
                self.display_matrix[i].insert(1, h_char)
        return self

class DisplayNumbers:
    def __init__(self):
        self.final_display_number = []
        one = Display(l1_right=up_s, l2_right=up_s)
        two = Display(top=down_s, l1_center=down_s, l1_right=up_s, l2_left=up_s,l2_center=down_s)
        three = Display(
            top=down_s, l1_center=down_s, l1_right=up_s,
            l2_right=up_s, l2_center=down_s,
            
        ) 
        four = Display(
            l1_left=up_s,
            l1_center=down_s,
            l1_right=up_s,
            l2_right=up_s
        ) 
        five = Display(
            top=down_s,
            l1_left=up_s,l1_center=down_s,
            l2_center=down_s, l2_right=up_s
        )
        six = Display(
            top=down_s,
            l1_left=up_s,l1_center=down_s,
            l2_left=up_s,l2_center=down_s, l2_right=up_s
        )
        seven = Display(
            top=down_s,
            l1_right=up_s,
            l2_right=up_s
        ) 
        eight = Display(
            top=down_s,
            l1_left=up_s, l1_center=down_s, l1_right=up_s,
            l2_left=up_s, l2_center=down_s, l2_right=up_s
        )
        nine = Display( 
            top=down_s,
            l1_left=up_s,
            l1_center=down_s,
            l1_right=up_s,
            l2_right=up_s
        )
        zero = Display(
            top=down_s,
            l1_left=up_s, l1_right=up_s,
            l2_left=up_s,l2_center=down_s, l2_right=up_s
        )
        self.numbers = {
            '1': one,
            '2': two,
            '3': three,
            '4': four,
            '5': five,
            '6': six,
            '7': seven,
            '8': eight,
            '9': nine, 
            '0': zero
        }


    def print_matrix(self, number_matrix):
        # This method print a matrix nxm
        for i in range(len(number_matrix)):
            line = ""
            for j in range(len(number_matrix[i])):
                line = line + number_matrix[i][j]
            print(line)

    def join_number_displays(self, final_matrix, number_matrix, idex=0):
        columns = len(number_matrix)
        raws = len(number_matrix[0])
        for i in range(columns):
            try:
                final_matrix[i].extend(number_matrix[i])
            except IndexError as ie:
                final_matrix.insert(i, number_matrix[i])
        return final_matrix

    def display_a_number(self, number, hight=0, weight=0):
        n_list = list(str(number))
        for n in n_list:
            number_matrix = self.numbers[n].increace_horizontal(
                    repetitions=weight
                ).increace_vertical(
                    repetitions=hight
                ).get_matrix()
            print(number_matrix)
            self.join_number_displays(
                final_matrix=self.final_display_number,
                number_matrix=number_matrix
            )
        self.print_matrix(self.final_display_number)
    
if __name__ == "__main__":
    d_n = DisplayNumbers()
    d_n.display_a_number(1234567890, hight=2, weight=2)
    