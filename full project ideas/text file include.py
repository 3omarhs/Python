open("C:\\Users\\omarh\\Desktop\\pass.txt", "w").close()
file1 = open("C:\\Users\\omarh\\Desktop\\pass.txt", "a")
counter = 0
with open('D:\\backup\\python projects\\python try hack insta\\rockyou.txt', errors="ignore") as f:
    for line in f:
        lin = line
        if "ibrahim" in lin.upper().lower():
            if len(line) >= 8 and len(line) <= 16:
                ln = line.strip() + "\n"
                file1.write(ln)
                counter = counter + 1
                print(f"line: {counter}")