# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 15:31:59 2023

@author: Juan Brasdefer 225936, Fabian Pawelczyk 226921
"""


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the first element of the queue."""
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO)."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
