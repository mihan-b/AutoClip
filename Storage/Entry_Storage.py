class StorageReader:
    def __init__(self, targetfile):
        self.file = open(targetfile,"r")
        self.datalist = [[]]
        for line in self.file:
            print(line)
            if line.strip("\n") == '!!!NL!!!':
                self.datalist.append([])
            else:
                self.datalist[len(self.datalist)-1].append(line.split())

g = StorageReader("test_entry.txt")
print(g.datalist)
