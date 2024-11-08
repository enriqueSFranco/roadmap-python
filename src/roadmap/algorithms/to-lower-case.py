def toLowerCase(s: str) -> str:
  result = ""
  for char in s:
    if "A" <= char <= "Z":
      result += char(ord(char) + 32)
    else: result += char
  return result

print(toLowerCase(""))