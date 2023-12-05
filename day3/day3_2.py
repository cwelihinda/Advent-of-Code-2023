import re
class Row:
    def __init__(self, row):
        self.data = row
        nums = re.finditer(r'\d+', row)
        potential_gears = re.finditer(r'\*', row)
        self.potential_gears = []
        for pg in potential_gears:
            self.potential_gears.append(int(pg.span()[0]))
        self.row_info = []
        for i in nums:
            self.row_info.append((int(i.group(0)), int(i.span()[0]), int(i.span()[1])))
    def check_gears(self, prev_row, next_row):
        if(len(self.potential_gears) == 0):
            return 0
        total = 0
        for gear in self.potential_gears:
            gears_in_range_prev = prev_row.has_gear_in_range(gear)
            gears_in_range_curr = self.has_gear_in_range(gear)
            gears_in_range_next = next_row.has_gear_in_range(gear)
            
            gears_in_range_total = [*gears_in_range_prev, *gears_in_range_curr, *gears_in_range_next]
            val = 0
            if(len(gears_in_range_total) == 2):
                val = gears_in_range_total[0] * gears_in_range_total[1]
            total += val
        return total
    def has_gear_in_range(self, column):
        gears_in_range = []
        for nums in self.row_info:
            if((column < nums[2] and column >= nums[1]) or (nums[1] - 1 == column) or (nums[2] == column)):
                gears_in_range.append(nums[0])
        return gears_in_range
    
    
with open("day3_input.txt") as file:
    lines = file.readlines()
    lines.append("".ljust(len(lines[0]), "."))
    total = 0
    for i in range(len(lines)):
        row = Row(lines[i])
        val = row.check_gears(Row(lines[i - 1]), Row(lines[(i + 1)% len(lines) ]))
        total += val
    print(total)