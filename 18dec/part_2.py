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
        print("c_expressions", expression)
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
                print(expression)
                expression = self.calculate_pairs(expression)

            for i in range(pair[0], pair[1]+1):
                if len(expression) > i - pair[0]:
                    s_lst[i] = expression[i - pair[0]]
                else:
                    s_lst[i] = ""
        return "".join(s_lst)

    def calculate_pairs(self, s):
        lst_s = list(s)
        nums = re.split("\\+|\\*", s)
        sum_pairs = []
        product_pairs = []
        idx = 0

        print("==========")
        print(s)
        for i, num in enumerate(nums[1:]):
            print(i, idx, num, (nums[i], i))
            expression_length = len(num) + len(nums[i]) + 1
            subtract = s[idx:expression_length + idx]
            print(expression_length, subtract, len(nums[i]) + 1)
            idx += len(nums[i]) + 1
            if "+" in subtract:
                sum_pairs.append(subtract)
            elif "*" in subtract:
                product_pairs.append(subtract)

        print("results:", s, sum_pairs, product_pairs)
        if len(sum_pairs) > 0:
            pair = sum_pairs[0]
        else:
            pair = product_pairs[0]
        print("pair:", pair)
        result = self.c_expression(pair)
        print("result:", result)
        expression_length = len(pair)
        idx = s.index(pair)
        print(idx, expression_length + idx)
        for i in range(idx, expression_length + idx):
            lst_s[i] = ""
        lst_s[idx] = result
        print("============")
        return "".join([str(i) for i in lst_s])

    def calculate(self, s):
        print(s)
        s = self.remove_parentheses(s)
        print(s)
        while "+" in s or "*" in s:
            print(s)
            s = self.calculate_pairs(s)
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
