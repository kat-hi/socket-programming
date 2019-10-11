list=['192.168.0.20','192.168.0.21','192.168.0.22','192.168.0.23']
for ip in list
	do
		ssh -c pi@$ip shutdown -h 0
		echo shutdown $ip 
	done

