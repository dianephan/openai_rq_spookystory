import os
from redis import Redis
from rq import Queue
import story

queue = Queue(connection=Redis())

def queue_tasks():
    for x in range(2):
        first_queued_job = queue.enqueue(story.write_story)
        queue.enqueue(story.write_story, depends_on=first_queued_job)

def main():
    queue_tasks()

if __name__ == "__main__":
    main()
