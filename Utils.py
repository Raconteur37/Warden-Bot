


class Utils:
    
    # Convert from @
    def getIdFromMention(a:str):
        a = a.replace("<","")
        a = a.replace(">","")
        a = a.replace("@","")
        a = a.replace("!", "")
        return(a)

    # Cleans db table to get raw values as strings
    def cleanDbTable(a:str):
        a = str(a)
        a = a.replace("[","")
        a = a.replace("]","")
        a = a.replace("(","")
        a = a.replace(")","")
        a = a.replace(",","")
        a = a.replace("'","")
        return(a)

    def getInstanceInTuple(a:str, index):
        a = str(a)
        a = a.replace("[","")
        a = a.replace("]","")
        a = a.replace("(","")
        a = a.replace(")","")
        a = a.replace(",","")
        a = a.replace("'","")
        args = a.split(" ")
        ans = args[index]
        return ans