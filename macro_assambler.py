import fileinput
import json
import re
import sys

#--------------------------------------------------------
mnt = []
mnt_dis = {"m_name":"","m_argc":0,"m_start":0,"m_end":0,"mcc":0} 
mdt = []
#--------------------------------------------------------

m_code = []  #modifide code
s_code = []  #source code
l = 0        #for line number

#--------------------------------------------------------

def find_macro(macro_name):
    for i in mnt:
        if macro_name == i["m_name"]:
            return i
    return None

def find_replace(d,c_line):
    d["mcc"] +=1
    lne = c_line.split()
    lne = lne[1].split(',')
    if d["m_argc"] == len(lne):
        s = d["m_start"]
        e = d["m_end"]
        for i in range(s,(e+1)):
            m_line = mdt[i]
            if "%%" in m_line:
                m_line = m_line.split("%%")
                if len(m_line) == 1:
                    m_code.append(".."+str(d["mcc"])+"."+str(d["m_name"])+"."+m_line[0])
                elif len(m_line) == 2:
                    m_code.append(m_line[0]+" .."+str(d["mcc"])+"."+str(d["m_name"])+"."+m_line[1])
            else:                      
                for j in range(1,((len(lne)) +1)):
                    k = ('%'+str(j))
                    if k in m_line:
                        m_line = m_line.replace(k,lne[j-1])
                if '%' in m_line:
                    x = list(map(int,re.findall('\d+',m_line)))
                    for j in x:
                        if ('%'+str(j)) in m_line:
                            m_line = m_line.replace(('%'+str(j)),' ')
                m_code.append(str(m_line))
    else:
        m_code.append(c_line)

def remove_internal_macro(l):
    while (not("%endmacro" in s_code[l])):
        if "%macro" in s_code[l]:
            l +=1
            remove_internal_macro()
        else:
            l +=1
    l +=1
    return l
                        
if __name__ == "__main__":
    with open("macro_intro.asm") as f:
        for line in f:
            s_code.append(line)
    
    while l < (len(s_code)):
        if "%macro" in s_code[l]:
            code_l = (s_code[l]).split()
            #if macro than remove and re-enter
            d = find_macro(code_l[1])
            if d :
                d["m_name"] = code_l[1]
                d["m_argc"] = int(code_l[2])
                d["m_start"] = len(mdt)
            else:
                mnt_dis["m_name"] = code_l[1]
                mnt_dis["m_argc"] = int(code_l[2])
                mnt_dis["m_start"] = len(mdt)
            l +=1
            while (not("%endmacro" in s_code[l])):
                if "%macro" in s_code[l]:
                    l +=1
                    l = remove_internal_macro(l)
                else:
                    mdt.append(s_code[l])
                    l +=1
            if d:
                d["m_end"] = (len(mdt)-1)
            else:
                mnt_dis["m_end"] = (len(mdt)-1)
                mnt.append(mnt_dis.copy())
            l +=1

        else:
            code_l = s_code[l].split()
            if len(code_l) > 0:
                d = find_macro(code_l[0])
                if d:
                    find_replace(d,s_code[l])  
                else:
                    m_code.append(s_code[l])
                l +=1
            else:
                m_code.append("\n")
                l +=1
                
    new_fp = open('macro_output.asm','w+')
    for i in m_code:
        new_fp.write(i)
    new_fp1 = open('macro_name_table','w+')
    new_fp1.write("macro_name | macro_argc | macro_start |  macro_end  | macro_call_count\n")
    for i in mnt:
        new_fp1.write(str(i["m_name"])+"\t\t"+str(i["m_argc"])+"\t\t"+str(i["m_start"])+"\t\t"+str(i["m_end"])+"\t\t"+str(i["mcc"])+"\n")
    new_fp2 = open('macro_defination_table','w+')
    for i in mdt:
        new_fp2.write(i)
