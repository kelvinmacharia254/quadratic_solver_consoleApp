class CoeffsError(Exception):
    """Exception raised when coeffs provide are zero or more than three"""

class CoeffAError(Exception):
    """Exception raised when coeffs provide are zero or more than three"""

# class CustomException(Exception):
#     def __init__(self, message, error_code):
#         self.message = message
#         self.error_code = error_code
#
# try:
#     raise CustomException("Something went wrong.", 500)
# except CustomException as e:
#     print(f"Error: {e.message}")
#     print(f"Error Code: {e.error_code}")