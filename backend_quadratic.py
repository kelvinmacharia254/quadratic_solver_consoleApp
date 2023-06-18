import math
import sys
import pprint
from exceptions import CoeffsError, CoeffAError

class Quadratic:
    """
    This is a quadratic class.
    """

    def __init__(self, *args):
        """
        Quadratic class constructor.
            1. Initializes the coefficient a, b and c from args.
            2. Calls the required function to solve the quadratic equation.
            3. Print initialized objects to check status.
            4. Call discriminant(), equation(), roots() of the object to get solution if no error reported in step 3.
        :param args:
        :return: none
        """
        # get 1st element of the args tuple which could be an empty list or with more items.
        if len(args) != 0:
            coefficients = args[0]

        self.error = None # start of with no error

        # check for errors in the inputs a, b and c
        # possible error includes:
        # 1. a = zero
        # 2. a, b and c being non-numerics i.e.bad types
        # 3. Zero coefficient passed
        try:
            if len(coefficients) > 0 <= 3: # if 1 to 3 coeffs are passed, coeff 'a' is always there.
                self.a = float(coefficients[0])
                if self.a == 0.0:  # if a is zero raise an exception.Stop further execution
                    raise CoeffAError("Error: Coefficient 'a' can't be zero for a valid quadratic equation.")
            else:
                pass

            if len(coefficients) == 0: # no coeffs provided
                raise CoeffsError("Error: No coefficient passed. Atleast on be should be passed.")
            elif len(coefficients) == 1: # only coeff 'a' is provided.
                self.b = 0.0
                self.c = 0.0
            elif len(coefficients) == 2: # Coeffs 'a' and 'b' provided
                self.b = float(coefficients[1])
                self.c = 0.0
            elif len(coefficients) == 3: # all three coeffs provided i.e. 'a', 'b' and 'c'
                self.b = float(coefficients[1])
                self.c = float(coefficients[2])
            elif len(coefficients) > 3: # more than 3 coeffs provided
                raise CoeffsError(f"Error: More than necessary coefficient provided. {len(coefficients)} coeffs provided instead of between 1 to 3 coeffs.")

        except Exception as e:
            if isinstance(e, ValueError):
                self.error = "Error: One or more input is non-numeric."  # convert the error to a string for display later
            elif isinstance(e, CoeffsError):
                # print("Here")
                self.error = str(e)


    def is_quadratic(self):
        """
        Checks whether the quadratic equation is valid by checking coefficient a
        :return: True or False
        """
        if self.a == 0:  # if a = 0 then the quadratic equation is not valid. Therefore, return False.
            return False
        else:  # if a is not 0 then the quadratic equation is valid. Therefore, return True.
            return True

    def equation(self):
        """
        Form the quadratic equation
        :return: quadratic equation as a string
        """
        return "No equation generated for now."

    def discriminant(self):
        """
        Computes the discriminant which informs about the nature of the roots.
        :return: discriminant
        """
        if self.is_quadratic():
            discriminant = round(((self.b ** 2) - (4 * self.a * self.c)), 2)
            return discriminant
        else:
            return None

    def roots(self):
        """
        Compute the roots.
        :return: roots of the quadratic equation as a tuple object with two items.
        """
        discriminant = self.discriminant()
        if self.is_quadratic():
            if discriminant == 0:
                # if discriminant is equal to zero, there is only one root:
                root = round(((-self.b / (2 * self.a)) + ((math.sqrt(discriminant)) / (2 * self.a))), 4)
                return root
            elif discriminant > 0:
                # if discriminant is greater than zero, there are two real roots:
                root1 = round((((-self.b ) / (2 * self.a)) + ((math.sqrt(discriminant)) / (2 * self.a))), 4)
                root2 = round((((-self.b ) / (2 * self.a)) - ((math.sqrt(discriminant)) / (2 * self.a))), 4)
                return root1, root2
            else:
                # if the discriminant is less than zero then roots are not real i.e. a complex solution is obtained.
                root1 = complex((round(((-self.b ) / (2 * self.a)), 4)),
                                (round((-(math.sqrt(abs(discriminant))) / (2 * self.a)), 4)))
                root2 = complex((round(((-self.b ) / (2 * self.a)), 4)),
                                (round(((math.sqrt(abs(discriminant))) / (2 * self.a)), 4)))
                return root1, root2

    def __str__(self):
        if self.error:
            return self.error
        else:
            return "No error, solution available."

q = Quadratic(['w',8,9])
print(q.is_quadratic())

# if __name__ == "__main__":
#     # self test code
#     if len(sys.argv) > 1:
#         # obtain inputs through the command line
#         coeff_lst = []
#         try:
#             coeff_lst.append(sys.argv[1])
#             coeff_lst.append(sys.argv[2])
#             coeff_lst.append(sys.argv[3])
#             q = Quadratic(*coeff_lst)
#             w = q.working()
#             if q.error == None:
#                 print("\tSolution:")
#                 print("Coefficients.")
#                 print("a = " + str(w['coefficients']['a']))
#                 print("b = " + str(w['coefficients']['b']))
#                 print("c = " + str(w['coefficients']['c']))
#                 print("Discriminant = " + str(w['discriminant']))
#                 print(str(w['nature of roots']))
#                 print(str(w['roots']))
#             else:
#                 print(q.error)
#         except:
#             print(q.error)
#     else:
#         # Fetch input from user
#         def get_coeff():
#             """
#             Fectch all the coefficient a, b and c from the terminal
#             :return:
#             """
#             coeff_lst = []
#             for coeff in range(3):
#                 if coeff == 0:
#                     coeff = "a"
#                 elif coeff == 1:
#                     coeff = "b"
#                 else:
#                     coeff = "c"
#                 while True:
#                     try:
#                         coefficient = input("Enter coefficient " + coeff + ": ")
#                         coefficient = float(coefficient)
#                         coeff_lst.append(coefficient)
#                         if coeff_lst[0] == 0:
#                             print("Coefficient 'a' can't be zero")
#                             coeff_lst.clear()
#                         else:
#                             break
#                     except Exception as e:
#                         print(e)
#                         print("'" + str(coefficient) + "' is not a valid value for coefficient '" + str(
#                             coeff) + "' .Try again!")
#                         continue
#
#             return coeff_lst
#
#
#         while True:
#             print("-------------------------------------------------------------")
#             coeff_lst = get_coeff()
#             q = Quadratic(*coeff_lst)
#
#             if q.error:
#                 print(q.error)
#             else:
#                 w = q.working()
#                 print("\tSolution:")
#                 print("Coefficients.")
#                 print("a = " + str(w['coefficients']['a']))
#                 print("b = " + str(w['coefficients']['b']))
#                 print("c = " + str(w['coefficients']['c']))
#                 print("Discriminant = " + str(w['discriminant']))
#                 print(str(w['nature of roots']))
#                 print(str(w['roots']))
#
#             x = input("Type 'x' to quit or Enter to solve another equation --> ")
#             if x.lower() == 'x':
#                 exit()

# TODO
# Convert ErrorHandling block to a function.
# Only allow calculations if there no errors