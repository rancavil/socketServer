#!/usr/bin/python3
import socket
import logging
import sys

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    try:
        if len(sys.argv) >= 2:
            server_address = sys.argv[1]
        else:
            logger.info('Usage : ./client.py <server address>')
            sys.exit(0)

        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sd:
            sd.connect((server_address,9990))
            msg = input('Enter message : ')
            if len(msg.strip()) > 0:
                logger.info('You will send <<{}>> to server'.format(msg))
                sd.sendall(msg.encode())
                response = sd.recv(1024)
            else:
                logger.info('You must enter a message!!! Try again')
                sys.exit(1)

        logger.info(response.decode())
    except Exception as e:
        logger.info(e)

