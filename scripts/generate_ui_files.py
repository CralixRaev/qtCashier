import os

os.chdir('..')
folder = []
for i in os.walk(os.getcwd()):
    folder.append(i)

for address, dirs, files in folder:
    for file in files:
        if file.split('.')[-1] == 'ui':
            if 'venv' not in address:
                print(f'Working on {address}/{file}')
                print(f'Output in: {address}/{".".join(file.split(".")[:-1])}.py')
                so = os.popen(
                    f'"C:\\Users\\Cralix\\Desktop\\qtCashier\\venv\\Scripts\\pyuic5.exe" {address}/{file} -o {address}/{".".join(file.split(".")[:-1])}.py').read()
                print(so)
