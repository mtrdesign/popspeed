popspeed
==========
Popspeed is a small Python script, which will try to download each message found in your mailbox, and will report the speed. It will never change the maiblox contents though - no massages will be deleted from the server as a result of a popspeed test.

Sample usage
------------
```
$ python popspeed.py example.com myuser mypass
Trying to connect to myuser@example.com via POP3
Found 8 messages, starting download...
Message 1: DL time: 0.10s, size:3.79 KB, AVG Speed: 36.38 KB/s
Message 2: DL time: 0.04s, size:1.30 KB, AVG Speed: 33.59 KB/s
Message 3: DL time: 0.01s, size:13.07 KB, AVG Speed: 1044.40 KB/s
Message 4: DL time: 0.01s, size:8.33 KB, AVG Speed: 584.06 KB/s
Message 5: DL time: 0.04s, size:50.99 KB, AVG Speed: 1222.89 KB/s
Message 6: DL time: 0.13s, size:35.38 KB, AVG Speed: 277.52 KB/s
Message 7: DL time: 0.03s, size:2.14 KB, AVG Speed: 75.02 KB/s
Message 8: DL time: 0.02s, size:11.43 KB, AVG Speed: 643.09 KB/s
Done.
```
