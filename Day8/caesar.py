logo = '''
     _______.___________.    _______ .______   .___________.
    /       |           |   /  _____||   _  \  |           |
   |   (----`---|  |----`  |  |  __  |  |_)  | `---|  |----`
    \   \       |  |       |  | |_ | |   ___/      |  |
.----)   |      |  |       |  |__| | |  |          |  |
|_______/       |__|        \______| | _|          |__|
'''

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text,amount_shift,input_direction):
  return_text = ""
  if input_direction == "decode":
    amount_shift *= -1
  for i in range(0, len(input_text)):
    if input_text[i] in alphabet:
      index = alphabet.index(input_text[i])
      new_index = index + amount_shift
      return_text += alphabet[new_index % len(alphabet)]
  print(f"The {input_direction}d text is '{return_text}'")

again = True

while again:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(input_text=text,amount_shift=shift,input_direction=direction)
  answer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if answer == 'no':
    again = False
    print("Bye~")
