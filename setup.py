from server import run
import os

if __name__ == '__main__':
    run(port=int(os.environ['PORT']))