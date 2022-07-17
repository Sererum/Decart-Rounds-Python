
class TreeBroko:

    def __init__(self, quantity_main_rounds: int, depth_immersion: int):
        self.quantity_main_rounds = quantity_main_rounds
        self.depth_immersion = depth_immersion

    def generate_tree(self):
        tree = []

        for i in range(self.quantity_main_rounds + 1):
            tree.append(Fraction(i, 1))

        for _ in range(self.depth_immersion):

            for i in range(len(tree) - 1):
                tree.insert(i * 2 + 1, tree[i * 2].get_mediant(tree[i * 2 + 1]))

        return tree


class Fraction:

    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def get_value(self):
        return self.numerator / self.denominator

    def get_mediant(self, fraction):
        return Fraction(self.numerator + fraction.get_numerator(), self.denominator + fraction.get_denominator())

