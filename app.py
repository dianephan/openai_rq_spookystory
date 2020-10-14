from datetime import datetime, timedelta
import time
import os
from redis import Redis
from rq import Queue
import story

queue = Queue(connection=Redis())

def queue_tasks():
    for x in range(12):
        queue.enqueue_in(timedelta(seconds=5), story.write_story)

def main():
    queue_tasks()

if __name__ == "__main__":
    main()
