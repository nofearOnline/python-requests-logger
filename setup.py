from server import run
import os

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=os.environ['PORT'])
    else:
        run()