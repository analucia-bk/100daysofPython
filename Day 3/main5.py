print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
word1 = ["t", "r", "u", "e"]
word2 = ["l", "o", "v", "e"]
point_true_name1 = 0
point_true_name2 = 0
point_love_name1 = 0
point_love_name2 = 0
## Laço para gerar pontuação
for letter in name1:
    if letter in word1:
        point_true_name1 += 1
for letter in name2:
    if letter in word1:
        point_true_name2 += 1
total_true = point_true_name2 + point_true_name1
for letter in name1:
    if letter in word2:
        point_love_name1 +=1
for letter in name2:
    if letter in word2:
        point_love_name2 +=1
total_love = (point_love_name1 + point_love_name2)
result= str(total_true) + str(total_love)
love_score = int(result)
## Condições
if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")