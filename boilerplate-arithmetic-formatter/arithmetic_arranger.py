# Create a function that receives a list of strings 
# that are arithmetic problems and returns the problems 
# arranged vertically and side-by-side.

def arithmetic_arranger(problems, solve=False):
    # se verifica si hay demasiados problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = []
    line1 = line2 = line3 = line4 = ""

    # se itera sobre cada cuenta
    for problem in problems:
        #se separa cada cuenta
        num1, operator, num2 = problem.split()

        # severifica si el operador es válido
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        # se verifica si contienen solo digitos
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        # se verifica si tienen mas de 4 dig
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # se calcula el ancho necesario para cada numero y operador
        width = max(len(num1), len(num2)) + 2
        # se construye las lineas del array
        line1 += num1.rjust(width) + "    "
        line2 += operator + " " + num2.rjust(width - 2) + "    "
        line3 += "-" * width + "    "

        # si solve es True se muestra los resultads
        if solve:
            if operator == "+":
                result = str(int(num1) + int(num2))
            else:
                result = str(int(num1) - int(num2))
            line4 += result.rjust(width) + "    "
    # se agrega lineas del arreglo a una lista
    arranged_problems.extend([line1.rstrip(), line2.rstrip(), line3.rstrip()])
    # se agrega las soluciones si solve es True
    if solve:
        arranged_problems.append(line4.rstrip())
    
    # se combina las líneas del arreglo en un solo string, separadas por saltos de línea
    return "\n".join(arranged_problems)