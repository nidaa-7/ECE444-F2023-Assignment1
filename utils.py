# Create a class named utils that includes the functions reversed and formatter

class Utils:
      
    # The reversed function that takes in a number and returns the number reversed:
    @staticmethod
    def reversed(number):
        if not isinstance(number, int):
            raise ValueError("The input is not an integer")
        else:
            if number < 0:
                number = str(number)
                number = number.replace(number[0], "", 1)
                return int(str(number)[::-1]) * -1
            else:
                return int(str(number)[::-1])

        
    # The formatter function that takes in a number and returns it in base 2 and base 8 format:
    @staticmethod
    def formatter(number):
        if not isinstance(number, int):
            raise ValueError("The input is not an integer")
        else:
            binary = bin(number)
            octal = oct(number)
            return binary, octal