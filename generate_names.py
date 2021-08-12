# target string: R.drawable.__seqw_000000
# R.drawable.__loop_000000
# 2_odebrane 1 minuta_000000

number_of_images = 59
default_string = "R.drawable.czas_3__"
string_to_copy = ""
end_name = "_,\n"

for i in range(number_of_images + 1):
    generated_string = default_string + str(i)
    string_to_copy += generated_string + end_name
    with open("string.txt", "w") as file:
        file.write(string_to_copy)
