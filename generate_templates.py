
number_of_templates = int(input("How many templates? ")) + 1
which_date = str(input("Which date (ex. 20210113)? "))
text_list = ["/*  */\n", "#include <stdio.h>\n\n", "int main(void) {\n\t", "\n\n\treturn 0;", "\n}"]

for i in range(1, number_of_templates):
    name = which_date + "_" + str(i) + ".c"
    try:
        with open(name, "w") as f:
            f.writelines(text_list)
    except Exception as e:
        print(e)
