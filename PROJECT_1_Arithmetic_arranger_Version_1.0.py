def arithmetic_arranger(*parameters):
    problems = parameters[0] #extracting problems from the supplied parameters
    operands = ["+","-"] #operands which we consider valid
    lst=[]

#checking all of the criteria (5 problem limit, only sum/sub, only integers, less then 5 digits per equation)
    if len(problems)>5 :
        print("Error: Too many problems.")
        quit()
  
    for n in problems:
        words = n.split()
        if words[1] not in operands:
            print("Error: Operator must be '+' or '-'")
            quit()            
        
        if words[0].isnumeric() == False or words[-1].isnumeric() == False:
            print("Error: Numbers must only contain digits.")
            quit()  

        if len(words[0])>4 or len(words[-1])>4:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        
        #splitting problems into individual 'words' and combining them back into a list of lists
        lst.append(words)

    #preparing variables: flag which would change the iteration cycle and lines of text to display
    i = 0
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    #a, b, c, represent the text that will be displayed for each individual equation
    while i<len(lst):
        if  len(lst[i][0]) > len(lst[i][2]): #if A parameter is longer then B
            a=(2*' '+ lst[i][0])
            b=(lst[i][1] + (len(lst[i][0]) - len(lst[i][2])+1)*" " + lst[i][2])
            c=((len(lst[i][0])+2)*'-')

        if len(lst[i][2]) > len(lst[i][0]): #if A parameter is shorter then B
            a=(((2 + len(lst[i][2]) - len(lst[i][0]))*" " + lst[i][0]))
            b=(lst[i][1] + " "+ lst[i][2])
            c=((len(lst[i][2])+2)*'-')

        if len(lst[i][0]) == len(lst[i][2]): #if A parameter is equal to B
            a=((2*" " + lst[i][0]))
            b=(lst[i][1] + " "+ lst[i][2])
            c=((len(lst[i][2])+2)*'-')

        #getting the result and adding whitespaces to it to match the rest of the lines
        result = str(eval(lst[i][0] + lst[i][1] + lst[i][2]))
        result = (((len(c)-len(result))*" "+ result))
        
        #combining results from individual equations to form lines which will be displayed
        line1 = line1 + a + "    "
        line2 = line2 + b + "    "
        line3 = line3 + c + "    "
        line4 = line4 + result  + "    "
        i = i + 1
    
    #displaying the equations
    print(line1)
    print(line2)
    print(line3)

    #displaying the solutions if true is added
    try:
        if parameters[1] == True:
            print(line4)
    except:
        quit()

#test run command below:
#arithmetic_arranger(["2501 + 242", "12 - 121", "4 + 1", "12 - 0", "10 - 2322"], True)