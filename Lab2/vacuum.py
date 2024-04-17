class agent:

    def goal_test(self, state):
        if state[0] == "Clean" and state[1] == "Clean":
            return True
        else:
            return False
    
    def action(self, state):
        if(state[state[2]]=="Dirty"): 
            return "Suck"
        elif(state[0]=="Dirty"): 
            return "Left"
        else:
            return "Right"

    def update(self, act, state):
        if act == "Suck":
            state[state[2]] = "Clean"
        elif act == "Left":
            state[2] = 0
        else:
            state[2] = 1

    def run(self, state):
        actions = []
        while not self.goal_test(state):
            act = self.action(state)
            actions.append(act)
            self.update(act, state)
        return actions
    
def test1():
    a= agent()
    a.state = ["Dirty", "Dirty", 0]
    output = a.run(a.state);
    if output == ["Suck", "Right", "Suck"]:
        print("Test1 passed")

def test2():
    a= agent()
    a.state = ["Dirty", "Dirty", 1]
    output = a.run(a.state);
    if output == ["Suck", "Left", "Suck"]:
        print("Test2 passed")

def test3():
    a= agent()
    a.state = ["Clean", "Clean", 0]
    output = a.run(a.state);
    if output == []:
        print("Test3 passed")

def test4():
    a= agent()
    a.state = ["Clean", "Clean", 1]
    output = a.run(a.state);
    if output == []:
        print("Test4 passed")

def test5():
    a= agent()
    a.state = ["Dirty", "Clean", 0]
    output = a.run(a.state);
    if output == ["Suck"]:
        print("Test5 passed")

def test6():
    a= agent()
    a.state = ["Dirty", "Clean", 1]
    output = a.run(a.state);
    if output == ["Left", "Suck"]:
        print("Test6 passed")

def test7():
    a= agent()
    a.state = ["Clean", "Dirty", 0]
    output = a.run(a.state);
    if output == ["Right", "Suck"]:
        print("Test7 passed")

def test8():  
    a= agent()
    a.state = ["Clean", "Dirty", 1]
    output = a.run(a.state);
    if output == ["Suck"]:
        print("Test8 passed")

def main():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()

if __name__ == "__main__":
    main()