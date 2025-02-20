
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

def tokenizer(fileName):
    content = remove_comments(fileName)
    content = re.sub(r'([;,.\(\)\{\}\[\]=\+\-\*/|~<>])', r' \1 ', content) 
    array = content.split()
    
    outputFiledata = ""

    
    for i in range(len(array)):     
        if array[i] in keyword_map:
            outputFiledata += "<keyword> " + array[i] + " </keyword>\n"
        elif array[i] in symbol_map:
           outputFiledata += "<symbol> " + array[i] + " </symbol>\n"
        elif re.search(identifier_e, array[i]):
            outputFiledata += "<identifier> " + array[i] + " </identifier>\n"
        else:
            outputFiledata += "N/A\n"
    
    return outputFiledata

def createFile(outputData, outFile):
    with open(outFile, "w") as out_file:
        out_file.write(f"<tokens>\n{outputData}</tokens>\n")
    

                 
        
        


def main():
    data1 = tokenizer(fileName1)
    data2= tokenizer(fileName2)
    createFile(data1, "SquareGame.xml")
    createFile(data2, "Main.xml")
    
if __name__ == "__main__":
    main()

