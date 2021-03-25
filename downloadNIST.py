import pandas as pd
import lib #pip3 install lib-elem-isotopes

loop=1
while loop==1:
    print("Type the element: ")
    elem=input()
    try:
        lib.ElementZ(elem)
        loop=0
    except:
        print("Something went wrong. Did you use the proper notation? H for hydrogren, Tb for terbium etc.")

print("Collecting table.....")
url = "https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z"+str(lib.ElementZ(elem))+".html"

dfs=pd.read_html(url)
table=dfs[1].loc[5:, [2, 4, 6]]
table.rename(columns={2: "Energy (MeV)", 4: "μ/ρ cm²/g", 6:"μ_{en}/ρ cm²/g"}, inplace=True)
print(table)
loop=1
while loop==1:
    print("Do you want to save this table? (y/n)")
    answer=input()
    if answer=="y":
        try:
            table.to_csv("XrayMassCoef"+elem+".csv")
            print("Saved as XrayMassCoef"+elem+".csv")
            loop=0
        except:
            print("Couldn't save for some reason. Do you have the rights to write in this folder?")
    elif answer=="n":
        loop=0
    else:
        print("Input not accepted. Only type y or n.")
