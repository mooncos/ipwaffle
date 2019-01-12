#! python2

import subprocess

def read_config():
    p = subprocess.Popen("iptables -t nat -v -L PREROUTING -n --line-number", stdout=subprocess.PIPE, shell=True)
    (output, err) = p.communicate() 
    p_status = p.wait()
    output = output.split("\n")[2:-1]
    rules_tokenized = []
    
    for line in output:
       entry = line.split()
       id_no = entry[0]
       srcproto = entry[4]
       srcip = entry[9]
       dproto = entry[10]
       srcport = entry[11].split(":")[1]
       _, dip, dport = entry[12].split(":")
       rules_tokenized.append((srcproto, srcip, srcport, dproto, dip, dport, id_no))

    return rules_tokenized