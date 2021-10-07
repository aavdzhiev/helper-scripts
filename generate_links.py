which_date = str(input("Which date (ex. 20210113)? "))
tasks = input("How many tasks? ")


url = "https://github.com/aavdzhiev/Code-Academy/tree/main/" + which_date + "/" + which_date + "_"
filename = which_date + "_links.txt"

try:
    with open(filename, "w") as f:
        for i in range(1, int(tasks) + 1):
            f.write(url + str(i) + ".c" + "\n")
except Exception as e:
    print(e)
