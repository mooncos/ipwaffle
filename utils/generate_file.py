#! python2

import os

cwd = os.getcwd()
ip_sh = os.path.join(cwd, "iptables.sh")


def bashfile(routes, rejects=[111, 932, 3128]):
    # Delete existing iptables.sh
    try:
        os.remove(ip_sh)
    except Exception, e:
        print "Cannot delete file, moving on...", e
    else:
        print "Deleted", ip_sh

    # Generating new file from port routes
    with open("iptables.sh", "w+") as f:
        # Header and shebang
        f.write("#!/bin/bash\n\n")

        # Write port rejections
        for port in rejects:
            f.write(("iptables -I INPUT -p udp  --dport {port} -j REJECT \niptables -I INPUT -p tcp  --dport {port} -j REJECT\n").format(port=port))
        f.write("\n")
        
        # Write port mappings
        for row in routes:
            f.write(("iptables -A FORWARD -p {srcproto} -d {srcip} --dport {srcport} -j ACCEPT\r\niptables -t nat -A PREROUTING -p {dproto} -d {srcip} --dport {srcport} -j DNAT --to {dip}:{dport}\n").format(srcproto=row[0], srcip=row[1], 
                srcport=row[2], dproto=row[3], dip=row[4], dport=row[5]))

        # Append last line
        f.write("iptables -t nat -L -n")

        return (True, ip_sh, routes, rejects)