import math
import sys
import pprint


class Quadratic:
    """
    This is a quadratic class.
    """

    def __init__(self, a, b, c):
        """
        Quadratic class constructor.
            1. Initializes the coefficient a, b and c.
            2. Calls the required function to solve the quadratic equation.
        :param a:
        :param b:
        :param c:
        :return: none
        """
        self.error = None

        # check for errors in the inputs a, b and c
        # possible error includes:
        # 1. a = zero
        # 2. a, b and c being non-digits
        try:
            self.a = float(a)
            if self.a == 0:  # if a is zero raise an exception
                raise Exception("'a' can't be zero")
            self.b = float(b)
            self.c = float(c)

            self.discriminant = self.discriminant_fn()  # calculate discriminant
            self.equation = self.equation_fn()  # form equation using the coefficients
            self.roots = self.roots_fn()  # solve for roots
            self.error = None  # if the execution gets here.No error was encountered

        except Exception as e:
            self.error = str(e)  # convert the error to a string for display later
            if self.error == "'a' can't be zero":  # alert 'a' is zero
                pass
            else:  # alert coefficient error inputs
                self.error = f"Input for coefficient {self.error.split()[-1]} is invalid"

    def testValidity(self):
        """
        Checks whether the quadratic equation is valid by checking coefficient a
        :return: True or False
        """
        if self.a == 0:  # if a = 0 then the quadratic equation is not valid. Therefore, return False.
            return False
        else:  # if a is not 0 then the quadratic equation is valid. Therefore, return True.
            return True

    def equation_fn(self):
        """
        Form the quadratic equation
        :return: quadratic equation as a string
        """
        if self.testValidity():
            if self.a > 0 and self.b > 0 and self.c > 0:
                if self.a == 1 and self.b == 1:
                    return "x\u00b2 + x + " + str(self.c)
                elif self.a == 1:
                    return "x\u00b2 + " + str(self.b) + "x + " + str(self.c)
                elif self.b == 1:
                    return str(self.a) + "x\u00b2 + x + " + str(self.c)
                return str(self.a) + "x\u00b2 + " + str(self.b) + "x + " + str(self.c)

            elif self.a > 0 and self.b > 0 and self.c < 0:
                if self.a == 1 and self.b == 1:
                    return "x\u00b2 + x - " + str(abs(self.c))
                elif self.a == 1:
                    return "x\u00b2 + " + str(self.b) + "x - " + str(abs(self.c))
                elif self.b == 1:
                    return str(self.a) + "x\u00b2 + x - " + str(self.c)
                return str(self.a) + "x\u00b2 + " + str(self.b) + "x - " + str(abs(self.c))

            elif self.a > 0 and self.b > 0 and self.c == 0:
                if self.a == 1 and self.b == 1:
                    return "x\u00b2 + x"
                elif self.a == 1:
                    return "x\u00b2 + " + str(self.b) + "x"
                elif self.b == 1:
                    return str(self.a) + "x\u00b2 + x"
                return str(self.a) + "x\u00b2 + " + str(self.b) + "x"

            elif self.a > 0 and self.b < 0 and self.c > 0:
                if self.a == 1 and self.b == -1:
                    return "x\u00b2 - x + " + str(self.c)
                elif self.a == 1:
                    return "x\u00b2 - " + str(abs(self.b)) + "x + " + str(self.c)
                elif self.b == -1:
                    return str(self.a) + "x\u00b2 - x + " + str(self.c)
                return str(self.a) + "x\u00b2 - " + str(abs(self.b)) + "x + " + str(self.c)

            elif self.a > 0 and self.b < 0 and self.c < 0:
                if self.a == 1 and self.b == -1:
                    return "x\u00b2 - x - " + str(abs(self.c))
                elif self.a == 1:
                    return "x\u00b2 - " + str(abs(self.b)) + "x - " + str(abs(self.c))
                elif self.b == -1:
                    return str(self.a) + "x\u00b2 - x - " + str(abs(self.c))
                return str(self.a) + "x\u00b2 - " + str(abs(self.b)) + "x - " + str(abs(self.c))

            elif self.a > 0 and self.b < 0 and self.c == 0:
                if self.a == 1 and self.b == -1:
                    return "x\u00b2 - x"
                elif self.a == 1:
                    return "x\u00b2 - " + str(self.b) + "x"
                elif self.b == -1:
                    return str(self.a) + "x\u00b2 - x"
                return str(self.a) + "x\u00b2 - " + str(self.b) + "x"

            elif self.a > 0 and self.b == 0 and self.c > 0:
                if self.a == 1:
                    return "x\u00b2 + " + str(self.c)
                return str(self.a) + "x\u00b2 + " + str(self.c)

            elif self.a > 0 and self.b == 0 and self.c < 0:
                if self.a == 1:
                    return "x\u00b2 - " + str(abs(self.c))
                return str(self.a) + "x\u00b2 - " + str(abs(self.c))

            elif self.a > 0 and self.b == 0 and self.c == 0:
                if self.a == 1:
                    return "x\u00b2"
                return str(self.a) + "x\u00b2"

            elif self.a < 0 and self.b > 0 and self.c > 0:
                if self.a == -1 and self.b == 1:
                    return "-x\u00b2 + x + " + str(self.c)
                elif self.a == -1:
                    return "-x\u00b2 + " + str(self.b) + "x + " + str(self.c)
                elif self.b == 1:
                    return "-" + str(abs(self.a)) + "x\u00b2 + x + " + str(self.c)
                return "-" + str(abs(self.a)) + "x\u00b2 + " + str(self.b) + "x + " + str(self.c)

            elif self.a < 0 and self.b > 0 and self.c < 0:
                if self.a == -1 and self.b == 1:
                    return "-x\u00b2 + x - " + str(abs(self.c))
                elif self.a == -1:
                    return "-x\u00b2 + " + str(self.b) + "x - " + str(abs(self.c))
                elif self.b == 1:
                    return "-" + str(abs(self.a)) + "x\u00b2 + x - " + str(abs(self.c))
                return "-" + str(abs(self.a)) + "x\u00b2 + " + str(self.b) + "x - " + str(abs(self.c))

            elif self.a < 0 and self.b > 0 and self.c == 0:
                if self.a == -1 and self.b == 1:
                    return "-x\u00b2 + x"
                elif self.a == -1:
                    return "-x\u00b2 + " + str(self.b) + "x"
                elif self.b == 1:
                    return "-" + str(abs(self.a)) + "x\u00b2 + x"
                return "-" + str(abs(self.a)) + "x\u00b2 + " + str(self.b) + "x"

            elif self.a < 0 and self.b < 0 and self.c > 0:
                if self.a == -1 and self.b == -1:
                    return "-x\u00b2 - x + " + str(self.c)
                elif self.a == -1:
                    return "-x\u00b2 - " + str(self.b) + "x + " + str(self.c)
                elif self.b == -1:
                    return "-" + str(abs(self.a)) + "x\u00b2 - x + " + str(self.c)
                return "-" + str(abs(self.a)) + "x\u00b2 - " + str(self.b) + "x + " + str(self.c)

            elif self.a < 0 and self.b < 0 and self.c < 0:
                if self.a == -1 and self.b == -1:
                    return "-x\u00b2 - x - " + str(abs(self.c))
                elif self.a == -1:
                    return "-x\u00b2 - " + str(abs(self.b)) + "x - " + str(abs(self.c))
                elif self.b == -1:
                    return "-" + str(abs(self.a)) + "x\u00b2 - x - " + str(abs(self.c))
                return "-" + str(abs(self.a)) + "x\u00b2 - " + str(self.b) + "x - " + str(abs(self.c))

            elif self.a < 0 and self.b < 0 and self.c == 0:
                if self.a == -1 and self.b == -1:
                    return "-x\u00b2 - x"
                elif self.a == 1:
                    return "-x\u00b2 - " + str(self.b) + "x"
                elif self.b == -1:
                    return "-" + str(abs(self.a)) + "x\u00b2 - x"
                return "-" + str(abs(self.a)) + "x\u00b2 - " + str(self.b) + "x"

            elif self.a < 0 and self.b == 0 and self.c > 0:
                if self.a == -1:
                    return "-x\u00b2 + " + str(self.c)
                return "-" + str(abs(a)) + "x\u00b2 + " + str(c)

            elif self.a < 0 and self.b == 0 and self.c < 0:
                if self.a == -1:
                    return "-x\u00b2 - " + str(abs(self.c))
                return "-" + str(abs(self.a)) + "x\u00b2 - " + str(abs(self.c))

            elif self.a < 0 and self.b == 0 and self.c == 0:
                if self.a == -1:
                    return "-x\u00b2"
                return "-" + str(abs(self.a)) + "x\u00b2"
        else:
            return None

    def discriminant_fn(self):
        """
        Computes the discriminant which informs about the nature of the roots.
        :return: discriminant
        """
        if self.testValidity():
            discriminant = round(((self.b ** 2) - (4 * self.a * self.c)), 2)
            return discriminant
        else:
            return None

    def roots_fn(self):
        """
        Compute the roots.
        :return: roots of the quadratic equation as a tuple object with two items.
        """
        if self.testValidity():
            if self.discriminant == 0:
                # if discriminant is equal to zero, there is only one root:
                root = round(((-self.b / (2 * self.a)) + ((math.sqrt(self.discriminant)) / (2 * self.a))), 2)
                return root
            elif self.discriminant > 0:
                # if discriminant is greater than zero, there two real roots:
                root1 = round((((-self.b ** 2) / (2 * self.a)) + ((math.sqrt(self.discriminant)) / (2 * self.a))), 2)
                root2 = round((((-self.b ** 2) / (2 * self.a)) - ((math.sqrt(self.discriminant)) / (2 * self.a))), 2)
                return root1, root2
            else:
                # if the discriminant is less than zero then roots are not real i.e. a complex solution is obtained.
                root1 = complex((round(((-self.b ** 2) / (2 * self.a)), 2)),
                                (round((-(math.sqrt(abs(self.discriminant))) / (2 * self.a)), 2)))
                root2 = complex((round(((-self.b ** 2) / (2 * self.a)), 2)),
                                (round(((math.sqrt(abs(self.discriminant))) / (2 * self.a)), 2)))
                return root1, root2
        else:
            return "No roots. When coefficient 'a' is zero the equation is linear not quadratic."

    def working(self):
        if self.testValidity():
            working_dic = {'coefficients': {'a': self.a, 'b': self.b, 'c': self.c}, 'equation': self.equation,
                           'discriminant': f"b\u00b2-4ac" \
                                           f" = {self.b}\u00b2-(4*{self.a}*{self.c}) = {self.discriminant}"}
            if self.discriminant == 0:
                working_dic['nature of roots'] = 'Discriminant = 0: Double or repeated roots.'
                working_dic['roots'] = f'Applying the quadratic equation:' \
                                       f'\n [b\u00b2/2a] ± [√(b\u00b2-4ac)]/2a ' \
                                       f'= [{self.b}\u00b2/(2*{self.a})] ± [√({self.b}\u00b2 - (4*{self.a}*{self.c})/2*{self.a}] = {self.roots}'
            elif self.discriminant < 0:
                working_dic['nature of roots'] = 'Discriminant < 0: Two complex roots.'
                working_dic['roots'] = f'Applying the quadratic equation:' \
                                       f'\n [b\u00b2/2a] ± [√(b\u00b2-4ac)]/2a ' \
                                       f'= [{self.b}\u00b2/(2*{self.a})] ± [√({self.b}\u00b2 - (4*{self.a}*{self.c})/2*{self.a}] = {self.roots}'
            else:
                working_dic['nature of roots'] = 'Discriminant > 0: Two real roots'
                working_dic['roots'] = f'Applying the quadratic equation:' \
                                       f'\n [b\u00b2/2a] ± [√(b\u00b2-4ac)]/2a ' \
                                       f'= [{self.b}\u00b2/(2*{self.a})] ± [√({self.b}\u00b2 - (4*{self.a}*{self.c}))/2*{self.a}] = {self.roots}'
            return working_dic
        else:
            return None


if __name__ == "__main__":
    # self test code
    if len(sys.argv) > 1:
        # obtain inputs through the command line
        coeff_lst = []
        try:
            coeff_lst.append(sys.argv[1])
            coeff_lst.append(sys.argv[2])
            coeff_lst.append(sys.argv[3])
            q = Quadratic(*coeff_lst)
            w = q.working()
            if q.error == None:
                print("\tSolution:")
                print("Coefficients.")
                print("a = " + str(w['coefficients']['a']))
                print("b = " + str(w['coefficients']['b']))
                print("c = " + str(w['coefficients']['c']))
                print("Discriminant = " + str(w['discriminant']))
                print(str(w['nature of roots']))
                print(str(w['roots']))
            else:
                print(q.error)
        except:
            print(q.error)
    else:
        # Fetch input from user
        def get_coeff():
            """
            Fectch all the coefficient a, b and c from the terminal
            :return:
            """
            coeff_lst = []
            for coeff in range(3):
                if coeff == 0:
                    coeff = "a"
                elif coeff == 1:
                    coeff = "b"
                else:
                    coeff = "c"
                while True:
                    try:
                        coefficient = input("Enter coefficient " + coeff + ": ")
                        coefficient = float(coefficient)
                        coeff_lst.append(coefficient)
                        if coeff_lst[0] == 0:
                            print("Coefficient 'a' can't be zero")
                            coeff_lst.clear()
                        else:
                            break
                    except Exception as e:
                        print(e)
                        print("'" + str(coefficient) + "' is not a valid value for coefficient '" + str(
                            coeff) + "' .Try again!")
                        continue

            return coeff_lst


        while True:
            print("-------------------------------------------------------------")
            coeff_lst = get_coeff()
            q = Quadratic(*coeff_lst)

            if q.error:
                print(q.error)
            else:
                w = q.working()
                print("\tSolution:")
                print("Coefficients.")
                print("a = " + str(w['coefficients']['a']))
                print("b = " + str(w['coefficients']['b']))
                print("c = " + str(w['coefficients']['c']))
                print("Discriminant = " + str(w['discriminant']))
                print(str(w['nature of roots']))
                print(str(w['roots']))

            x = input("Type 'x' to quit or Enter to solve another equation --> ")
            if x.lower() == 'x':
                exit()
