class Question:
    def __init__(self, prompts,answer):
        self.prompts = prompts
        self.answer = answer

question_prompts = [
    "What color is the sky?\n(a) Red\n(b) Blue\n(c) Purple\n\n",
    "What color is the moon?\n(a) White\n(b) Black\n(c) Pink\n\n"
]

questions = [
    Question(question_prompts[0],"b"),
    Question(question_prompts[1],"a")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompts)
        if answer == question.answer:
            score += 1
    print(f"You got {score} / {len(questions)} Correct")

run_test(questions)