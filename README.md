### Instructions
This python3 program downloads X-ray Mass Attenuation Coefficients from the NIST database and saves them in a nice readable .csv file.

downloadNIST.py is more user friendly while adownloadNIST.py is more suitable for a larger amount of tables.

## downloadNIST.py
- Execute using "python3 downloadNIST.py" / "chmod +x downloadNIST.py && ./downloadNIST.py"
- Follow instructions
- Table will be saved in the same folder as you are in.

## adownloadNIST.py
- Execute "python3 adownloadNIST.py X" / "chmod +x adownloadNIST.py && ./adownloadNIST.py X" where X is the element name.
- Csv data will be printed to the terminal.
- Optionally you can pipe the data into a file or pipe it into other programs like sed (example: "python3 adownloadNIST.py Tb > path/to/file.csv"
