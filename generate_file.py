#! python2

import os

cwd = os.getcwd()
ip_sh = os.path.join(cwd, "iptables.sh")


def gen_sh(routes, rejects):
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
        f.write("#!/bin/bash\n")

        # Write port rejections
        for port in rejects:
            f.write(("iptables -I INPUT -p udp --dport {port} -j REJECT\r\niptables -I INPUT -p tcp --dport {port} -j REJECT\n").format(port=port))

        # Write port mappings
        for row in routes:
            f.write(("iptables -A FORWARD -p {srcproto} -d {srcip} --dport {srcport} -j ACCEPT\r\niptables -t nat -A PREROUTING -p {dproto} -d {srcip} --dport {srcport} -j DNAT --to {dip}:{dport}\n").format(srcproto=row[0], srcip=row[1], 
                srcport=row[2], dproto=row[3], dip=row[4], dport=row[5]))

        # Append last line
        f.write("iptables -t nat -L -n")

        return (True, ip_sh, routes, rejects)

# print gen_sh([('tcp', '5.9.100.11', '587', 'tcp', '192.168.1.4', '587'), ('tcp', '5.9.100.11', '80', 'tcp', '192.168.1.4', '80'), ('tcp', '5.9.100.11', '3389', 'tcp', '192.168.1.4', '22'), ('tcp', '5.9.100.11', '8080', 'tcp', '192.168.1.4', '8080'), ('tcp', '5.9.100.11', '8663', 'tcp', '192.168.1.4', '8663'), ('tcp', '5.9.100.11', '8443', 'tcp', '192.168.1.4', '8443'), ('tcp', '5.9.100.11', '8000', 'tcp', '192.168.1.4', '8000'), ('tcp', '5.9.100.11', '6998', 'tcp', '192.168.1.4', '6998'), ('tcp', '5.9.100.11', '443', 'tcp', '192.168.1.4', '443'), ('tcp', '5.9.100.11', '1337', 'tcp', '192.168.1.4', '1337'), ('tcp', '5.9.100.11', '7331', 'tcp', '192.168.1.4', '7331'), ('tcp', '5.9.100.11', '25', 'tcp', '192.168.1.4', '25'), ('tcp', '5.9.100.11', '465', 'tcp', '192.168.1.4', '465'), ('tcp', '5.9.100.11', '143', 'tcp', '192.168.1.4', '143'), ('tcp', '5.9.100.11', '993', 'tcp', '192.168.1.4', '993'), ('tcp', '5.9.100.11', '110', 'tcp', '192.168.1.4', '110'), ('tcp', '5.9.100.11', '995', 'tcp', '192.168.1.4', '995'), ('tcp', '5.9.100.11', '4190', 'tcp', '192.168.1.4', '4190'), ('tcp', '5.9.100.11', '5555', 'tcp', '192.168.1.1', '5555'), ('tcp', '5.9.100.11', '3390', 'tcp', '192.168.1.2', '22'), ('tcp', '5.9.100.11', '222', 'tcp', '192.168.1.2', '22'), ('tcp', '5.9.100.11', '280', 'tcp', '192.168.1.2', '80'), ('tcp', '5.9.100.11', '28080', 'tcp', '192.168.1.2', '8080'), ('tcp', '5.9.100.11','2443', 'tcp', '192.168.1.2', '443')], [111, 932, 3128])