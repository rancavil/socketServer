# socketServer

Socket server is a simple server that receives a message from a client, and sends back a response.

This is a server developed from scratch using multiprocessing and socket python libraries.

## how to use it

**Starting the server:**

     $ git clone https://github.com/rancavil/socketServer.git
     $ cd socketServer/
     $ ./server.py

**Using the cliente:**

     $ ./client.py <server-address>
     Enter message : 

You have to enter a message 

     Enter message : Hello

The server will respond.

     INFO:__main__:You will send <<Hello>> to server
     INFO:__main__:Server side says 2019-10-21 01:10:26.160460 Message Received <<Hello>> from 191.11x.13.171

At the server-side we will see the following messages:

     ubuntu@ip-172–31–16–4x:~/socketServer$ ./server.py
     DEBUG:__main__:Server started 2019–10–27 04:09:37.401182
     DEBUG:__main__:2019–10–21 01:10:40.457245 Received data from 191.11x.13.171
     DEBUG:__main__:2019–10–21 01:10:40.459447 Created process 1766
     DEBUG:__main__:2019–10–21 01:10:42.507844 Message Received <<Hello>> from 191.11x.13.171
     DEBUG:__main__:2019–10–21 01:11:24.356126 Received data from 191.11x.13.171
     DEBUG:__main__:2019–10–21 01:11:24.357009 Created process 1767
     DEBUG:__main__:2019–10–21 01:11:26.159615 Message Received <<Hello>> from 191.11x.13.171

To stop the server, you just have to press CRTL-C and it’s all.

     ^CDEBUG:__main__:Server stopped
