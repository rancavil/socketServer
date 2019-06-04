import socket as sk
import multiprocessing as mp
from datetime import datetime as dt
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def handler(conn,address):
    with conn:
        data = conn.recv(1024)
        logger.debug('{} Message Received <<{}>> from {}'.format(dt.now(),data.decode(),address[0]))
        if len(data)>0:
            resp = '{} Message Received <<{}>> from {}'.format(dt.now(),data.decode(),address[0])
            conn.sendall(resp.encode())
            return

def kill_all_process():
    for p in mp.active_children():
        logger.debug('Pid : {} terminated'.format(p.pid))
        p.terminate()
        p.join()

if __name__ == '__main__':
    # a simple server
    logger.debug('Server started {}'.format(dt.now()))
    with sk.socket(sk.AF_INET,sk.SOCK_STREAM) as sd:
        try:
            sd.bind(('0.0.0.0',9990))
            sd.listen(1)
            while True:
                conn,address = sd.accept()
                with conn:
                    logger.debug('{} Received data from {}'.format(dt.now(),address[0]))
                    p = mp.Process(target=handler,args=(conn,address))
                    p.daemon=True
                    p.start()
                    logger.debug('{} Created process {}'.format(dt.now(),p.pid))
                    
        except Exception as e:
            logger.debug(e)
            kill_all_process()
            sd.close()
        except KeyboardInterrupt:
            logger.debug('Server stopped')
            kill_all_process()
            sd.close()
        finally:
            kill_all_process()

