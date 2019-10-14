#_*_ coding:utf-8 _*_

lock_file = "lock.txt"

with open(lock_file,"a+",encoding="utf-8") as lockFile:
    print("123113132312313")
    for lines in lockFile:
        print(lines)



