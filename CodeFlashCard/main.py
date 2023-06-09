import os

class Flashcard:
    def __init__(self, file_path):
        self.file_path = file_path
        self.flashcard_lines, self.flashcard_comments = self.load_file()

    def load_file(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"No file found at: {self.file_path}")

        code_lines = []
        code_comments = []

        with open(self.file_path, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                if line and not line.lstrip().startswith('#'):
                    code_lines.append(line)
                elif line.lstrip().startswith('#'):
                    code_comments.append(line.lstrip()[1:].strip())

        if len(code_comments) < len(code_lines):
            code_comments.extend([''] * (len(code_lines) - len(code_comments)))

        return code_lines, code_comments

    def ask_question(self, line_no, previous_line, comment):
        prompt = "\n{}\n# {}\nType line {}:".format(previous_line, comment, line_no)
        return input(prompt)

    def run_flashcard(self):
        correct_answers = 0

        for i, (line, comment) in enumerate(zip(self.flashcard_lines, self.flashcard_comments), start=1):
            failure_score = 0
            answer = self.ask_question(i, f'{i-1}: {self.flashcard_lines[i-2]}' if i > 1 else '', comment)
            hint_words = line.split()

            while answer.strip() != line.strip():
                if failure_score < len(hint_words):
                    print(f"Incorrect! Here's a hint: {' '.join(hint_words[:failure_score+1])}")
                else:
                    print(f"You've exhausted all hints. The correct line was: {line}")
                    break
                answer = self.ask_question(i, f'{i-1}: {self.flashcard_lines[i-2]}' if i > 1 else '', comment)
                failure_score += 1

            if answer.strip() == line.strip():
                correct_answers += 1
                print("Correct!")

        return correct_answers, failure_score

def main():
    print("Welcome to the Code Flashcard Game!")
    print("Guess the missing lines of code based on the provided prompts.")
    print("Which program would you like to test? Type 1, 2 or 3")
    programChoice = int(input())
    if programChoice == 1:
        flashcard = Flashcard('TestThis.txt')
    elif programChoice == 2:
        flashcard = Flashcard('Unique.txt')
    else:
        flashcard = Flashcard('dependencies.txt')

    num_correct_answers, num_failures = flashcard.run_flashcard()

    print("\nGame over! You answered {} line(s) correctly.".format(num_correct_answers))
    print("Failure score: {}".format(num_failures))

if __name__ == "__main__":
    main()
