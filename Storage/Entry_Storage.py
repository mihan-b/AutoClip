class StorageReader:
    def __init__(self, targetfile):
        self.dataname = targetfile
        reader = open(targetfile,"r")
        self.datalist = {}
        i = 0
        for line in reader:
            split_list = line.split(" ",1)
            self.datalist[tuple(split_list[0].strip("[]").split("+"))] = split_list[1].strip("][\n")
        reader.close()
    def modify_list(self, key, value):
        if key in self.datalist.keys(): #if key exists 
            if value in self.datalist.values(): #if value exists, thus, we are changing it's key
                self.datalist.pop(key) #remove existing key
            self.datalist[key] = value #if new key, new set of terms, if old key, update value
    def output_to_text(self):
        reader = open(self.dataname, "w")
        for key in self.datalist.keys():
            keyterm = "["
            for term in key:
                keyterm += term + "+"
            keyterm = keyterm.rstrip("+") + "]"
            valueterm = "[" + self.datalist[key] + "]"
            reader.write(keyterm + " " + valueterm + "\n")
        reader.close()