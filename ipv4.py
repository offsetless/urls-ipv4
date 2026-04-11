import socket

def ipv4(inputf,output):
    try:
        #read urls
        with open(inputf, 'r') as file:
            urls = file.read().splitlines()
        
        ips = []
        for url in urls:
            try:
                #convert urls->ipv4
                ip = socket.gethostbyname(url)
                ips.append(ip)
            except socket.gaierror:
                print(f"error conecting to->{url}")
        
        #write->file
        with open(output, 'w') as file:
            for ip in ips:
                file.write(ip + '\n')
        
        print(f"IPs have been saved to-> {output}")
    except FileNotFoundError:
        print(f"file not found {intputf}")
#example
if __name__ == "__main__":
    inputf = input("Enter file name: ")
    output = "iplist.txt" # output file name
    ipv4(intputf, output)
