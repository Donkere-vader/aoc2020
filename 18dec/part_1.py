import re


puzzle_input = [line.strip().replace(" ", "") for line in open('puzzle_input.txt')]


def product(lst):
    if len(lst) == 0:
        return 0
    tot = 1
    for i in lst:
        tot *= i
    return tot


class Calculator:
    def __init__(self, sums):
        self.sums = sums
        self.outputs = []

    def c_expression(self, expression):
        if "+" in expression:
            expression = [int(i) for i in expression.split("+")]
            return sum(expression)
        elif "*" in expression:
            expression = [int(i) for i in expression.split("*")]
            return product(expression)

    def remove_parentheses(self, s):
        open_parantheses = None
        parentheses_pairs = []
        skip = 0
        for idx, char in enumerate(s):
            if char == "(":
                if open_parantheses is None:
                    open_parantheses = idx
                else:
                    skip += 1
            elif char == ")":
                if skip > 0:
                    skip -= 1
                else:
                    parentheses_pairs.append(
                        (open_parantheses, idx)
                    )
                    open_parantheses = None

        s_lst = list(s)
        for pair in parentheses_pairs:
            expression = s[pair[0]+1:pair[1]]
            if "(" in expression:
                expression = self.remove_parentheses(expression)

            while "+" in expression or "*" in expression:
                print(s)
                expression = self.calculate_left_pair(expression)

            for i in range(pair[0], pair[1]+1):
                if len(expression) > i - pair[0]:
                    s_lst[i] = expression[i - pair[0]]
                else:
                    s_lst[i] = ""
        return "".join(s_lst)

    def calculate_left_pair(self, s):
        lst_s = list(s)
        nums = re.split("\\+|\\*", s)
        expression_length = len(nums[0]) + len(nums[1]) + 1
        subtract = s[:expression_length]

        result = self.c_expression(subtract)
        for i in range(expression_length):
            lst_s[i] = ""
        lst_s[0] = result
        return "".join([str(i) for i in lst_s])

    def calculate(self, s):
        print(s)
        s = self.remove_parentheses(s)
        print(s)
        while "+" in s or "*" in s:
            print(s)
            s = self.calculate_left_pair(s)
        self.outputs.append(int(s))

    def start(self):
        for s in self.sums:
            self.calculate(s)


def main():
    calculator = Calculator(
        puzzle_input
    )
    calculator.start()
    print(sum(calculator.outputs))


if __name__ == "__main__":
    main()
