
def wordBreak(self, s, wordDict):
        dict={}
        
        return sorted(self.words(s,wordDict,dict))
       
def words(self,s,wordDict,dic):
    res=[]
    if s in dic:
        return dic[s]
    if(len(s)==0):
        res.append("")
        return res
    for i in range(len(s),-1,-1):
        temp=s[i:]
        if(s[i:] in wordDict):
            l=self.words(s[:i],wordDict,dic)
            for x in l:
                if(x==""):
                    res.append(temp)
                else:
                    res.append(x+" "+temp)
            
    dic[s]=res
    return res