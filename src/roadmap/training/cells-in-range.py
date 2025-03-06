from typing import List

def col_letter_to_num(col_letter):
  return ord(col_letter) - ord('A') + 1

def num_to_col_letter(col_num):
  return chr(col_num + ord('A') - 1)

def extract_range_info(s):
  col_start, row_start, col_end, row_end = s[0], int(s[1]), s[3], int(s[4])
  
  col_start_num = col_letter_to_num(col_start)
  col_end_num = col_letter_to_num(col_end)
  
  return [col_start_num, col_end_num, row_start, row_end]

def cellsInRange(s: str) -> List[str]:
  col_start_num, col_end_num, row_start, row_end = extract_range_info(s)
  cells = []
  for row in range(row_start, row_end + 1):
    for col in range(col_start_num, col_end_num + 1):
      cell = "{}{}".format(num_to_col_letter(col), row)
      cells.append(cell)
  
  cells.sort()
  
  return cells

print(cellsInRange("K1:L2")) # ["K1","K2","L1","L2"]