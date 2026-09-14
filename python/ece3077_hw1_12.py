

class Link:
    def __init__(self, capacity, avail):
        self.capacity = capacity
        self.avail = avail
        pass

link1 = Link(10, 0.95)
link2 = Link(10, 0.90)
link3 = Link(5, 0.92)
link4 = Link(5, 0.88)
link5 = Link(2.5, 0.97)
link6 = Link(2.5, 0.94)

count = 1
for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):
                for m in range(2):
                    for n in range(2):
                        sum = ((0 if i % 2 == 0 else link1.capacity) + (0 if j % 2 == 0 else link2.capacity) + (0 if k % 2 == 0 else link3.capacity) + (0 if l % 2 == 0 else link4.capacity) + (0 if m % 2 == 0 else link5.capacity) + (0 if n % 2 == 0 else link6.capacity))
                        print(str(count) + " " + (str(i) + str(j) + str(k) + str(l) + str(m) + str(n)) + " " + str(sum) + (" TRUE" if sum>20 else " FALSE"))
                        count+=1

print("CONTIRUBTUIONSFFOSEFJOISFJEO")
print("HELO")