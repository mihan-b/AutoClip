class StorageReader:
    def __init__(self, targetfile):
        self.file = open(targetfile,"r")
        self.datalist = {}
        lastkey = ""
        for line in self.file:
            if line[0] == '~':
                lastkey = line.strip("\n~")
                self.datalist[lastkey] = []
            else:
                self.datalist[lastkey].append(line.split())
