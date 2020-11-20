from paramiko.client import SSHClient,AutoAddPolicy
from getpass import getpass
paswd = getpass()

client = SSHClient()
client2 = SSHClient()

client.set_missing_host_key_policy(AutoAddPolicy())
client.connect("192.168.100.38",22,"09011281924049",paswd)

client2.set_missing_host_key_policy(AutoAddPolicy())
client2.connect("192.168.100.39",22,"username",paswd)

def node1():
    while(True):
        stdin, stdout, stderr = client.exec_command('python3 MonitoringComp.py')
        lines = stdout.readlines()
        lines_err = stderr.readlines()

        for i in lines_err:
            print(i)
        for i in lines:
            print(i)

    client.close()

def node2():
    while(True):
        stdin2, stdout2, stderr2 = client2.exec_command('python3 MonitoringComp.py')
        lines2 = stdout2.readlines()
        lines_err2 = stderr2.readlines()

        for i2 in lines_err2:
            print(i2)
        for i2 in lines2:
            print(i2)

    client2.close()


pilihan = input("\n1. Node1 \n2. Node2\nMasukkan Node yang ingin di check :")
if pilihan == "1" :
    node1()
else:
    node2()
