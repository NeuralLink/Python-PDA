##    The goal of this program is to simulate the top-down parsing as performed by a compiler when given an input
##    arithmetic expression to be checked for correct syntax. The logic implemented in this program is just a
##    starting point, as an actual compiler will use additional concepts so that it can do its job much faster. We
##    know the rules of a grammar are in the form: V → string, where V is a variable and string is a ﬁnite
##    sequence of variables and terminals. If we are given the rules of a grammar, the symbols on the left sides
##    of the arrows will be the variables. Any symbol which does not appear on the left side of a rule must be a
##    terminal.




class Rule:
    def __init__(self , variable , productions):
        self.variable   = variable
        self.productions = [productions]

def read_rules(): #Read rules from 'rules.cfg' into a list called rules_input
    rules_file = open("rules.cfg", "rt")
    data = rules_file.read()
    lines = data.split("\n")
    for line in lines:
        rules_input.append(line)
        print(line)

def read_exp():  #Expression is read from 'expression.cfg' into list exp in reverse order, removing whitespace.
    i = 0
    exp_file = open("expression.cfg", "rt")
    data = exp_file.read()
    chars = data.split(" ")
    for char in chars[::-1]:
        i = i + 1
        exp.append(char)
    return i

def divide_rules():  # split productions into the rules class by variable
    results = []
    for rule in rules_input:
        found = False
        var = rule.split(" -> ")
        for result in results:
            if result.variable == var[0]:
                result.productions.append(var[1])
                found = True
        if not found:
            results.append(Rule(var[0] , var[1]))
    return results

def print_reject():  #Prints Reject and exits program.
    print("\n\n")
    print("************************************")
    print("*             REJECT               *")
    print("************************************")
    exit()


def operation():  #Performs the operations of a PDA.  Recursive.
    #added x,y counting variables to count up and allow different variables and productions to be tested.
    global x
    global y
    global var
    global kill
    global match

    print("At the beginning of operation, stack = ", stack)
    var = stack.pop()
    test()
    if match == True:
        match = False
        operation()

    print("var =", var)
    if var == rules[x].variable:
        if len(rules[x].productions) <= y:
            string = rules[x].productions[y].split(" ")
        else:
            string = rules[x].productions[y].split(" ")
        for s in string[::-1]:
            stack.append(s)
        print("Stack after rules applied( Marker 1)", stack) # MARKER ONE
        if kill == True:
            kill = False
            for op in stack:
                del op
            stack.append(rules[0].variable)

            if y <= len(rules[x].productions):
                y = y + 1
            elif x < len(rules):
                y = 0
                x = x + 1
            else:
                print_reject()
            operation()
        operation()
    elif x <= len(rules):
        y = 0
        x = x + 1
    else:
        print_reject()

    print("End of Operation (MARKER TWO", stack) # MARKER TWO




def test():
    global i
    global var
    global exp
    global match
    global length
    #test if
    if var == exp[i]:
        exp.pop()
        match = True

    if len(stack) == 0 and len(exp) == 0:
        print("\n\n")
        print("************************************")
        print("*             ACCEPT               *")
        print("************************************")
        exit()
        #accept program

    if len(stack) > length: #Kills stack if length of stack is greater than length of original expression
        global kill
        print("\n\n")
        print("************************************")
        print("* Stack has exceeded String length *")
        print("************************************")
        kill = True

def main():
    global length
    global rules
    print("Rules:")
    read_rules()

    print("Expression:")
    length = read_exp()
    print(exp)
    print("Expression length:", length)
    rules = divide_rules()

    #print("\n\nThis should be E:")
    #print(rules[0].variable)
    stack.append(rules[0].variable)

    operation()

exp = []
test_exp = []
rules_input = []
stack = []
i = int(0)
x = int(0)
y = int(0)
z = int(0)
kill = False
match = False

main()
