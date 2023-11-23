answer = ""
while True:
    answer = input("Enter line length: ")
    if answer.strip().isnumeric() and int(answer) > 1:
        break


LINE_LENGTH = int(answer.strip())

input_read = open("input.txt", "r")
output_write = open("output.txt", "w")
output_write.write("")
output_write.close()
output_append = open("output.txt", "a")

for l in input_read:
    string = l

    while len(string) > LINE_LENGTH:
        cur_pos = LINE_LENGTH

        while string[cur_pos - 1] != " " and cur_pos != 0:
            cur_pos -= 1

        if cur_pos <= 0:
            space = string.find(" ")
            if space != -1:
                cur_pos = space
            else:
                cur_pos = len(string)

        if string.strip() != "":
            output_append.write(string[:cur_pos].strip() + "\n")
        string = string[cur_pos:]

    if string.strip() != "":
        output_append.write(string.strip() + "\n")


output_append.close()

output_read = open("output.txt", "r")

result = ""
for line in output_read:
    if line.strip(): 
        result += line

output_read.close()

output_write2 = open("output.txt", "w")
output_write2.write(result)

output_write2.close()
input_read.close()