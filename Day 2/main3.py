'''Create a program using maths and f-Strings that tells us how many days, weeks, months 
we have left if we live until 90 years old.It will take your current age
as the input and output a message with our time left in this format:

'''
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
months = ((90 * 12) - (int(age) * 12))
weeks = ((90 * 52)) - (int(age) * 52)
days = ((90 * 365) - (int(age) * 365))

print(f"You have {days} days, {weeks} weeks, and {months} months left.")


