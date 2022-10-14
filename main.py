import sys
if 4 == len(sys.argv):
    match sys.argv[2]:
        case "+":
            result = float(sys.argv[1]) + float(sys.argv[3])
        case "-":
            result = float(sys.argv[1]) - float(sys.argv[3])
        case "x":
            result = float(sys.argv[1]) * float(sys.argv[3])
        case "/":
            result = float(sys.argv[1]) / float(sys.argv[3])
    print(sys.argv[1], sys.argv[2], sys.argv[3], "=", result)
else:
    print("Usage: python main.py [first number] [+,-,x,/] [second number]")