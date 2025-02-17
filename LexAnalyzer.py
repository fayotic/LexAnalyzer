
import re
fileName1 = "SquareGame.jack"
fileName2 = "Main.jack"
file1 = open(fileName1)
file2 = open(fileName2)

 #Word banks
symbol = {'=', '(', ')', '[', ']', '{', '}', ',', ';', '.', '+', '-', '*', '/', '|',
             '~', '<', '>'}

keyword = {'class', 'constructor', 'method', 'function', 'int', 'boolean', 'char',
                  'void', 'var', 'static', 'field', 'let', 'do', 'if', 'else', 'while', 'return', 'true',
                  'false', 'null', 'this'}

identifier_e = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'

#Mapping 
keyword_map = {word: "<keyword>" for word in keyword}

symbol_map = {word: "<symbol>" for word in symbol}

iden_map = {word: "<identifier>" for word in identifier_e}

def remove_comments(fileName):
    with open(fileName, 'r') as data:
        content = data.read()
        content = re.sub(r'//.*', '', content)
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        content = re.sub(r'\s+', ' ', content)
        content = content.strip()
    return content

def test(fileName):
    content = remove_comments(fileName)
   
    for line in content.split():
        print(line)


def main():
    test(fileName1)
    test(fileName2)
    
if __name__ == "__main__":
    main()

