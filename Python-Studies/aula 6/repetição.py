start = int(input("start: "))
end = int(input("end: "))
step = int(input("end: "))

for i in range(start, end, step):
    if i % 10 == 0:
       print(i)

alunos = ["Rodrigo", "Antonio", "Pedro"]

for aluno in range(len(alunos)):
    print(aluno)