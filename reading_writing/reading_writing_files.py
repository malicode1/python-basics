open("example.txt","a").close()

with open("example.txt","w") as f:
    f.write("Hello World")

with open("example.txt","a") as f:
    f.write("\nNew line added.\n")

with open("example.txt","r") as f:
    print(f.read())