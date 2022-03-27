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
        V_in_list = value in self.datalist.values()
        if V_in_list and not key in self.datalist.keys(): #if value exists, thus, we are changing it's key
            for k, v in self.full_list.items():
                if value == v:
                    self.datalist.pop(k) #if same value, remove 
                    break
        self.datalist[key] = value #if existing key, update it, if new key, assign new entry
        #note: changing the key with the same value may cause entry misallignment with the VFrame entry order.
        #Changes should only lead to different positions of entries between program restarts, though it might cause problems
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