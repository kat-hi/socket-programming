list=[192.168.0.20 192.168.0.21 192.168.0.22 192.168.0.23]

for ip in $list
	do ssh pi@$ip
		sudo apt-get update 
		echo update $ip done
	       	sudo apt-get upgrade
		echo upgrade $ip done	
	done

