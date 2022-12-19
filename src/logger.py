import logging
from datetime import datetime
from main import *

class DataLogs:

    def __init__(self):

        self.error = None

        self.filename = 'logs.txt'

        try:
            main()
        except:
            self.error = logging.error('Data Export Not Succesfull')

    def showLogs(self):
        if self.error:
            return self.error
        else:
            return 'Data Export Succesfull'

    def writeLogs(self):

        if self.error:
            time = datetime.now().strftime("%d-%m-%Y %H-%M-%S")
            with open(self.filename, 'a') as f:
                f.write(f'Logs - {time}')
                f.write('\n')
            try:
                logging.basicConfig(filename=self.filename,
                                filemode='a',
                                format="%(asctime)s, %(msecs)d %(name)s %(levelname)s [ %(filename)s-%(module)s-%(lineno)d ]  : %(message)s",
                                datefmt="%H:%M:%S",
                                level=logging.DEBUG)
            except:
                return 'Error: Error creating logging file'



if __name__ == '__main__':

    Logs = DataLogs()

    Logs.showLogs()

    Logs.writeLogs()