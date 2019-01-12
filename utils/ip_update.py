#! python2

import subprocess

def update_config(new_bashfile):
	p = subprocess.Popen("iptables -t nat -v -L PREROUTING -n --line-number", stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate() 
	p_status = p.wait()
	lines = len(output.split('\n'))-3
	print "Erasing a total of : ", lines
	i=0

	while i < lines:
		p = subprocess.Popen("iptables -t nat -D PREROUTING 1", stdout=subprocess.PIPE, shell=True)
		(output, err) = p.communicate()
		p_status = p.wait()
		i = i + 1

	p = subprocess.Popen("sh " + new_bashfile, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate() 
	p_status = p.wait()
	if err:
		return (False, err)
	else:
		return (True, None)

