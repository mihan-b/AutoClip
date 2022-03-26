class StorageReader:
    def __init__(self, targetfile, key):
        self.dataname = targetfile
        reader = open(targetfile,"r", encoding="utf-8")
        self.datalist = {}
        output = self.hash_v(reader.read(), key)
    #    print(output)
        self.key = key
        for line in output.split("\n"):
         #   print(f'LN: {line}')
            split_list = line.split(" ",1)
            self.datalist[tuple(split_list[0].strip("[]").split("+"))] = split_list[1].strip("][\n")
        reader.close()
      #  self.output_to_text()
    def modify_list(self, key, value):
        if key in self.datalist.keys(): #if key exists 
            if value in self.datalist.values(): #if value exists, thus, we are changing it's key
                self.datalist.pop(key) #remove existing key
            self.datalist[key] = value #if new key, new set of terms, if old key, update value
    def output_to_text(self):
        reader = open(self.dataname, "w")
        sumoutput = ""
        for key in self.datalist.keys():
            keyterm = "["
            for term in key:
                keyterm += term + "+"
            keyterm = keyterm.rstrip("+") + "]"
            valueterm = "[" + self.datalist[key] + "]"
            sumoutput+= keyterm + " " + valueterm + "\n"
        reader.write(self.hash_v(sumoutput.rstrip("\n"), self.key))
        reader.close()
    #basic xor hashing
    def hash_v(self, input_line, key) :
        masksz = len(key)
        bytekey = key.encode()
       # print(input_line)
        maskiter = 0
        output = ""
        for char in input_line.encode() :
            #print(chr(bytekey[maskiter]))
           # print(char)
           # print(f'{chr(char ^ bytekey[maskiter])} {char ^ bytekey[maskiter]}')
            output += chr(char ^ bytekey[maskiter])
            maskiter+=1
            if(masksz == maskiter):
                maskiter = 0
        return output