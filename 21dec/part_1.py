puzzle_input = [line.replace("\n", "") for line in open('puzzle_input.txt').readlines()]


class Food:
    def __init__(self, ingredients, contains):
        self.ingredients, self.contains = (ingredients, contains)

    def __repr__(self):
        return f"<Food {' '.join(self.ingredients)} (contains {', '.join(self.contains)})"

foods = []
for line in puzzle_input:
    line = [i.strip().replace(")", "") for i in line.split("(contains")]
    line[0] = line[0].split(" ")
    line[1] = line[1].split(", ")
    foods.append(Food(line[0], line[1]))


class Analyzer:
    def __init__(self, foods):
        self.foods = foods

        # ditctionary of ingredients. per example; "mxmxckd": "dairy"
        self.dictionary = {}

    def analyze(self):
        # fill dictionary and logiquiz the most out of it
        for food in self.foods:
            for contain in food.contains:
                if contain not in self.dictionary:
                    self.dictionary[contain] = food.ingredients
                else:
                    new_lst = []
                    for ingredient in food.ingredients:
                        if ingredient in self.dictionary[contain]:
                            new_lst.append(ingredient)
                    self.dictionary[contain] = new_lst

                # know an ingredient
                if len(self.dictionary[contain]) == 1:
                    known_ingredient = self.dictionary[contain][0]
                    for key in self.dictionary:
                        if key == contain:
                            continue
                        if known_ingredient in self.dictionary[key]:
                            self.dictionary[key].remove(known_ingredient)

        # === get safe ingredients ===
        # get all ingredients
        ingredients = []
        for food in self.foods:
            ingredients += food.ingredients

        # remove the possible allergeen ingredients
        for key in self.dictionary:
            for allergeen in self.dictionary[key]:
                while allergeen in ingredients:
                    ingredients.remove(allergeen)

        return ingredients

def main():
    analyzer = Analyzer(foods)
    ingredients = analyzer.analyze()
    print(ingredients)
    print(len(ingredients))


if __name__ == "__main__":
    main()
