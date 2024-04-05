# functions go here


# main routine goes here

while True:
    want_instructions = input("Do you want to read the "
                              "instructions? ").lower()


    if want_instructions == "yes":
        print("Blah Blah Blah")
    elif want_instructions == "no":
        pass
    else:
        print("please answer yes / no")

    print("we are done")
