# Not really the correct of way of implementing this
# Should have a separate functionality for lexing and parsing, but oh well...
class ExpressionProcessor:
    def __init__(self):
        self.variables = {}

    def calculate(self, expression):

        result = 0

        def get_next_value(subexpr):
            string_value = ''
            for j, subchar in enumerate(subexpr):
                if subchar not in ['+','-']:
                    string_value += subchar
                else:
                    break
            if string_value.isdigit():
                return int(string_value), j
            elif len(string_value) > 1:
                return 0, j
            return self.variables[string_value], j
            
        first_val, i = get_next_value(expression)
        result += first_val
        
        while i < len(expression):
            char = expression[i]
            if char == '+':
                next_val, j = get_next_value(expression[i+1:])
                i += j

                result += next_val
            elif char == '-':
                next_val, j = get_next_value(expression[i+1:])
                i += j
                result -= next_val
            i += 1
            
        return result

if __name__ == "__main__":
    e = ExpressionProcessor()
    e.variables['y'] = 1

    print(e.calculate('1+y+oa'))


                    

