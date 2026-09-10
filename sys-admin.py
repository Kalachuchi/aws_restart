import os
import subprocess
#os.system("ls")
subprocess.run(["ls","-l","README.md"])
command="uname"
commandArgument="-a"
print(f'Gathering system information with command:{command} {commandArgument}')
subprocess.run([command, commandArgument])

command="ps"
commandArgument="-x"
print(f'Gathering active process information:{command} {commandArgument}')
subprocess.run([command,commandArgument])