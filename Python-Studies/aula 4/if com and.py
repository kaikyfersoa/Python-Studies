#por que não 2 ifs?
#caso dois ifs apareçam juntos, eles vão rodar juntos de maneira independente

score = int(input("What is your score: "))

if score > 7 and score < 9:
    print(f"You got an B")
elif score > 9 and score < 10:
    print(f"You got an A")
elif score == 10:
    print(f"You got an A+")
else:
    print(f"You got an F")