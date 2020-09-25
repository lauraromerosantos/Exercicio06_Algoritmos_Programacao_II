'''
Construa um algoritmo que possua uma tupla com os números escritos por extenso
de “zero” a “nove”. Peça ao usuário para digitar um nome de 0 a 9 e retorne 
a ele o número por extenso, sem usar estruturas condicionais (if e switch).
'''

tuple = ('zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')

index = int(input('Enter a number from zero to nine: '))

while True:
  if 0 <= index <= 9:
    print("-"*30)
    print('Number {} is inside the range.'.format(tuple[index]))
    break
  else:
    print('You typed a number out of range. Try again.')
    break



