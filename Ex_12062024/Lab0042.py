score = int(input("Enter the score \n"))
if score >= 90:
    print("Grade A")
elif score>=80 and score<90:
    print("Grade B")
elif score>=70 and score<80:
    print("Grade C")
elif score>=60 and score<70:
    print("Grade D")
elif score>=50 and score<60:
    print("Grade E")
else:
    print("Grade F")