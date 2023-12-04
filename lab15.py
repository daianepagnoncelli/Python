#você usará os.system()o comando Bash para executar ls, que mostra o conteúdo do diretório
import os
os.system("ls")

#o subprocessmódulo para gerar novos processos, conectar-se a canais de entrada/saída/erro e obter códigos de erro
import subprocess
subprocess.run(["ls"])

#os colchetes são tipos de dados de lista, o que significa que run()podem receber uma lista de argumentos
subprocess.run(["ls","-l"])

#subprocess.run()com três argumentos, o terceiro argumento será um nome de diretório
subprocess.run(["ls","-l","README.md"])

#chamará o "uname" comando para obter informações do sistema
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

#subprocess.run()permite executar qualquer comando, você executará o comando df para obter informações do disco
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])