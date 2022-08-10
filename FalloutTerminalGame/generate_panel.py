import random


class Generator:
    result = []
    words = ["ACCOUNT", "ADVANCE", "ALLONGE", "ANNUITY", "ARREARS", "AUCTION", "AUDITOR", "AUTARKY"]
    secret = random.choice(words)

    def generate_panel(self):
        random.shuffle(self.words)
        rand_idx = random.randint(0, 7)
        sighs = "!@#$%^&*()';%:?"
        for i in range(0, 8):
            word_choice = random.randint(0, 2)
            self.result.append([])
            for x in range(3):
                if word_choice == x:
                    word = self.words.pop()
                    pattern = list(random.choices(sighs, k=7))
                    pattern.insert(rand_idx, word)
                else:
                    pattern = list(random.choices(sighs, k=14))
                self.result[i].append(f"0xF{random.randint(650, 710)} {''.join(pattern)}")
        return self.text(self.result)

    def text(self, lst: list):
        string_ = ''
        for line in lst:
            string_ += ' '.join(line)
            string_ += '\n'
        return string_
