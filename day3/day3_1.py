import re
class Row:
    def __init__(self, row):
        self.data = row
        nums = re.finditer(r'\d+', row)
        self.row_info = []
        for i in nums:
            self.row_info.append((i.group(0), i.span()[0], i.span()[1]))
    def check_num(self, prev_row, next_row):
        row = self.data
        symbols = "`~!@#$%%^&*()_+-=[{}]\\|;:'\",<>/?"
        total = 0
        for info in self.row_info:
            is_symbol = False
            values = ""
            for i in range(info[1], info[2]):
                if(i > 0 and info[1] == i):
                    is_symbol = is_symbol or (row[i  - 1] in symbols) or (prev_row[i- 1]  in symbols) or (next_row[i- 1]  in symbols) 
                is_symbol = is_symbol or (prev_row[i] in symbols) or (next_row[i] in symbols)
                if(i < len(row) - 2 and i == info[2] - 1):
                    is_symbol = is_symbol or (row[i  + 1] in symbols) or (prev_row[i + 1]  in symbols) or (next_row[i + 1]  in symbols)
            if is_symbol:
                total += int(info[0])
        return total
                
with open("day3_input.txt") as file:
    lines = file.readlines()
    lines.append("".ljust(len(lines[0]), "."))
    total = 0
    for i in range(len(lines)):
        row = Row(lines[i])
        val = row.check_num(lines[i - 1], lines[(i + 1)% len(lines) ])
        total += val
        
    print(total)
