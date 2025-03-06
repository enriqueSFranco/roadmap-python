from typing import Dict

def decodeMessage(key: str, message: str) -> str:
  substitution_table: Dict[str, str] = {}
  
  for char in key:
    if char == ' ' or char in substitution_table:
      continue
    substitution_table[char] = chr(ord('a') + len(substitution_table))
  
  decoded_message = ''.join(substitution_table.get(char, char) for char in message)
  
  return decoded_message
    
print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))