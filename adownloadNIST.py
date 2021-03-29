#!/usr/bin/env python3
import pandas as pd
import lib #pip3 install lib-elem-isotopes
import sys

elem=sys.argv[1]

try:
    lib.ElementZ(elem)
except:
    print("Something went wrong. Did you use the proper notation? H for hydrogren, Tb for terbium etc.\nTo run this program use: 'python3 filename.py element [> savefile.csv]'")
    exit()

url = "https://physics.nist.gov/PhysRefData/XrayMassCoef/ElemTab/z"+str(lib.ElementZ(elem))+".html"

dfs=pd.read_html(url)
table=dfs[1].loc[5:, [2, 4, 6]]
table.rename(columns={2: "Energy (MeV)", 4: "μ/ρ cm²/g", 6:"μ_{en}/ρ cm²/g"}, inplace=True)
print(table.to_csv(index=False))
