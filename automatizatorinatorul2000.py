table_name = input("TABLE = ")
query = ""
no_values = int(input("NO. OF VALUES = "))
print("Int positions [enter if empty]: ")
int_positions = [int(x) for x in input().split()]
for i in range(no_values):
	row = input()
	values = row.split(",")
	for j in range(len(values)):
		if j not in int_positions:
			values[j] = f"'{values[j]}'"

	final = f"({','.join(values)});"
	query += f"INSERT INTO {table_name}\nVALUES\n{final}\n\n"

print(f"\nQUERY FINAL:\n\n{query}")
