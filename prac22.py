quiz={
    "question":"capital of pakistan",
    "answer":"islamabad"
}

print(quiz["question"])

ans=input("enter your answer: ").lower()
if ans==quiz["answer"]:
    print("correct")

else:
    print("false")