class Character:
    def __init__(self, name):
        self.name = name
        self.dialogues = {}

    def start_conversation(self):
        question = input("Ask a question: ")
        answer = self.dialogues.get(question.lower(), "I don't know the answer.")
        print(answer)

    def add_dialogue(self, question, response):
        self.dialogues[question] = response

    def respond_to_question(self, question):
        if question in self.dialogues:
            return self.dialogues[question]
        else:
            return "I don't know the answer to that question."


