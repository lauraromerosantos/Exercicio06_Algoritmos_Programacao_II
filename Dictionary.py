'''
Construa um algoritmo que peça ao usuário para informar o nome, a nota01 e a nota02 de um aluno. 
Guarde estas informações em um dicionário. Após, calcule a nota final deste aluno [(nota01 + nota02)/2]
e adicione ao dicionário. Ao final, imprima todos os dados do dicionário.
'''

name = input('Enter the name of the student: ')
note_01 = float(input('Type a note 1: '))
note_02 = float(input('Type a note 2: '))

student = {
    'name': name, 
    'note_01':note_01, 
    'note_02':note_02
    }

average = (student['note_01'] + student['note_02'])/2
student['average'] = average


print("-"*60)
print("Dictionary")
print(student)
print("-"*60)

'''
for chave, valor in student.items():
    print (f"{chave} - {valor}")

'''
