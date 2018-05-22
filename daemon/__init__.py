__project__ = 'OSADOL.'
__author__ = 'Jeys_Ozzius.'
__descript__ = "Copyright (c) 2017 Anirban Ghosh(Anirban83314) & Debashis Biswas(deb991)."
__URL__ = 'https://github.com/Anirban83314/OutLook-Automation-All-scopes-with-APP-utility.'
__NB__ = 'For more information, please see github page & all commit details.'
__CipherSig__ = 'This project & all associate files are encrypted under PBEncryption cryptography. Another details will be available at the end of this pgogram.'

import os
import sys
import math

class DaemonOTF():
    def __init__(self, umask, wdir, maxfd):
        self.umask = 0
        self.wdir = '/'
        self.maxfd = 1024
        return self

#Initiating Operation for Daemon.

    if (hasattr(os, "devnull")):
        redirect_to = os.devnull
    else:
        redirect_to = '/dev/null'

    def creatingDaemon(self):

        try:
            pid = os.fork ( )
        except OSError as e:
            raise Exception ( "%s [%d]" % (e.strerror , e.errno) )

        if (pid == 0):
            os.setsid()

            try:
                pid = os.fork ( )  # Fork a second child.
            except OSError as e:
                raise Exception ( "%s [%d]" % (e.strerror , e.errno) )

            if (pid == 0):
                os.chdir(self.wdir)
                os.umask(self.umask)

            else:
                os._exit(0)

        else:
            os._exit(0)

        import resource  # Resource usage information.
        maxfd = resource.getrlimit ( resource.RLIMIT_NOFILE )[1]
        if (maxfd == resource.RLIM_INFINITY):
            maxfd = self.maxfd

        for fd in range ( 0 , maxfd ):
            try:
                os.close ( fd )
            except OSError:  # ERROR, fd wasn't open to begin with (ignored)
                pass

        os.dup2 ( 0 , 1 )  # standard output (1)
        os.dup2 ( 0 , 2 )

        return(0)

if __name__ == '__main__':
    retCode = DaemonOTF

    procParams = """
       return code = %s
       process ID = %s
       parent process ID = %s
       process group ID = %s
       session ID = %s
       user ID = %s
       effective user ID = %s
       real group ID = %s
       effective group ID = %s
       """ % (retCode , os.getpid ( ) , os.getppid ( ) , os.getpgrp (0), os.getuid ( ) , os.geteuid ( ) , os.getgid ( ) , os.getegid ( ))

    open ( "createDaemon.log" , "w" ).write ( procParams + "\n" )

    sys.exit ( retCode )

os.getsid ( 0 )
