print("Welcome to your life decider")
print("***********")

progress_count = 0
trailer_count = 0
retreiver_count = 0
excluded_count = 0

# creating cells
def create_cells(count_type):
    print("   ", end=" ")
    if row<(count_type):
        print("*", end=" ")
    else:
        print(" ", end=" ")
    print("  ",end = " ")







# arguements to take the inputs

done=False      # The boolean flag that indicates if we are finished with the work. This will help us loop the program till we are finished with the work.
try:
    while done==False:

        Pass = int(input("Please enter your credit at pass: "))
        while Pass not in [0, 20, 40, 60, 80, 100, 120]:
            # https://stackoverflow.com/questions/12553609/how-to-test-that-variable-is-not-equal-to-multiple-things - this is how I created this code.
            print("Out of range!")
            Pass = int(input("RETRY! It should be in 0,20,40,60,80,100,120 range.\nPlease enter your credit at pass: "))

        Defer = int(input("Please enter your credit at defer: "))
        while Defer not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range!")
            Defer = int(input("RETRY! It should be in 0,20,40,60,80,100,120 range.\nPlease enter your credit at defer: "))

        Fail = int(input("Please enter your credit at fail: "))
        while Fail not in [0, 20, 40, 60, 80, 100, 120]:
            print("Out of range!")
            Fail = int(input("RETRY! It should be in 0,20,40,60,80,100,120 range.\nPlease enter your credit at fail: "))

        total_marks = Pass + Defer + Fail
        if total_marks != 120:
            print("Total incorrect! Please try again.")

        else:    #logics to sort out the progression outcome.
            if Fail + Defer <= 20:
                if Fail + Defer == 0:
                    print("Progress")
                    progress_count=progress_count+1
                else:
                    print("Progress(module trailer)")
                    trailer_count=trailer_count+1
            elif Fail >= 80:
                print("Exclude")
                excluded_count=excluded_count+1
            else:
                print("Do not progress - module retriever")
                retreiver_count=retreiver_count+1


        runAgain =input("Enter y to continue. Enter q to quit and view results: ")
        while runAgain!="y" or runAgain!="q":
            if runAgain == "y":
                done=False
                break
            elif runAgain=="q":
                done=True
                print("Thank you for using the program")
                break
            else:
                print("Wrong input. check again.")
                runAgain = input("Enter y to continue. Enter q to quit and view results: ")


except ValueError:
    print("integer rquired! Please try again.")

print("_____________________________________________")
print("")


print("_____________________________________________")
print("")


h = max(progress_count, excluded_count, retreiver_count, trailer_count)
total_count=progress_count+trailer_count+retreiver_count+excluded_count

print("Progress",progress_count,"Trailer",trailer_count,"Retreiver",trailer_count,"Excluded",trailer_count)


#looping row by row
for row in range(h):
        #printing a cells in a row
    create_cells(progress_count)
    create_cells(trailer_count)
    create_cells(retreiver_count)
    create_cells(excluded_count)
    print("",end="\n")  #breaking the line so the loop can start in a new row.




print("Total count is ",total_count)
