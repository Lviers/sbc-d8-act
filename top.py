"""files = open("sbc-d8-sample.txt", "w")
file = open("ni.txt", "r")
print(file.readlines())
var = file.read()
print(var[0:])
print(file.read())
 
lines = [line.strip() for line in open("ni.txt")]

print(lines[4])

lines = [line.strip() for line in open("sbc-d8-sample.txt")]
for line in lines:
    print(line)

file = open("sbc-d8-sample.txt", "w")
file.write("HEWWO")
file.write("\nHEWW")
file.write("\nHEO")
file.close()

ws = open("sbc-d8-sample.txt", "w")
print("HEWsWO",file=ws )
print("\nHEWW",file=ws)
print("\nHEO0",file=ws)
ws.close()

fname = "ligma"
lname = "barruso"
write = open("st.txt", "w")
print(fname, file = write)
print(lname, file = write)
write.close()
"""

while True:
    write = open("st.txt", "a")
    name = input("Name: ")
    print(name, file=write)
    write.close()

