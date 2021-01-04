#!/usr/bin/env python3

from pdf2image import convert_from_path

import uuid
import threading


class ThreadSafeGenerator(object):
    """Wrapper around generator that protects concurrent access"""

    def __init__(self, gen):
        self.gen = gen
        self.lock = threading.Lock()

    def __iter__(self):
        return self

    def __next__(self):
        with self.lock:
            return next(self.gen)


def threadsafe(f):
    """Decorator to make generator threadsafe. Fix #125"""

    def g(*a, **kw):
        return ThreadSafeGenerator(f(*a, **kw))

    return g


@threadsafe
def uuid_generator():
    """Returns a UUID4"""
    while True:
        yield str(uuid.uuid4())


@threadsafe
def counter_generator(prefix="", suffix="", padding_goal=4):
    """Returns a joined prefix, iteration number, and suffix"""
    i = 0
    while True:
        i += 1
        yield str(prefix) + str(i).zfill(padding_goal) + str(suffix)



convert_from_path(
    './input.pdf',
    dpi=200,
    output_folder='./in',
    first_page=None,
    last_page=None,
    fmt="jpg",
    jpegopt=None,
    thread_count=4,
    userpw=None,
    use_cropbox=False,
    strict=False,
    transparent=False,
    single_file=False,
    output_file=uuid_generator(),
    poppler_path=None,
    grayscale=False,
    size=None
)
