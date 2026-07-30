#This code shows how to get rid of whitemarks
first_name = "\n\tsamantha\t"
last_name = "\theet\t"
full_name = f"{first_name.title()} {last_name.title()}"
print(full_name)
print(full_name.lstrip())
print(full_name.rstrip())
print(full_name.strip())
print(first_name.strip(),last_name.strip())
