import os
from redis import Redis
from rq import Queue
import story

queue = Queue(connection=Redis())

def queue_tasks():
    queued_job = queue.enqueue(story.write_story)
    for x in range(2):
        previous_job = queued_job
        queued_job = queue.enqueue(story.write_story, depends_on=previous_job)

def main():
    queue_tasks()

if __name__ == "__main__":
    main()
