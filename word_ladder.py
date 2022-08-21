from queue import Queue
from stack import Stack


class WordLadder:
    """A class providing functionality to create word ladders"""
    def __init__(self, w1, w2, wordlist):
        """
        Initialize w1, w2, wordlist(word that is same length)
        Initialize a queue containing a single stack with w1.
        Initialize the alphabets and set with w1
        """
        self.w1 = w1
        self.w2 = w2
        self.wordlist = wordlist
        self.alphabet = ['a', 'b', 'c', 'd',
                         'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'l',
                         'm', 'n', 'o', 'p',
                         'q', 'r', 's', 't',
                         'u', 'v', 'w', 'x',
                         'y', 'z']
        self.check_word = {w1}
        self.stack = Stack()
        # Push the first word in the word ladder which is w1
        self.stack.push(self.w1)
        self.queue = Queue()
        # A queue eqnueueing a single stack
        self.queue.enqueue(self.stack)

    def make_ladder(self):
        # If queue is empty, return none
        if self.queue.isEmpty():
            return None
        else:
            # If not, repeat the same steps
            while not self.queue.isEmpty():
                # Dequeue the element which is stack
                stack = self.queue.dequeue()
                # Peek at its top item which is a word
                word = stack.peek()
                # For each position in the word
                for position in range(len(word)):
                    # For each alphabet in alphabet list
                    for alpha in self.alphabet:
                        # Replace the character with each alphabet to generate
                        # a candidate new word.
                        new_word = word[:position] + alpha + word[position+1:]
                        # Method to o reduce the running time
                        # If new_word is not in self.set, add new_word to set
                        # when only new word appears
                        # Don't need to recheck the word that appeared before
                        if new_word not in self.check_word:
                            self.check_word.add(new_word)
                            # If the new_word in the wordlist
                            if new_word in self.wordlist:
                                # Make a duplicate of the stack
                                new_stack = stack.copy()
                                # Push the new_word onto the new_stack
                                new_stack.push(new_word)
                                # If the last word in new_stack equal to w2
                                # return new stack.
                                if new_stack.peek() == self.w2:
                                    return new_stack
                                # If not, enqueue the new stack onto
                                # the end of the queue.
                                else:
                                    self.queue.enqueue(new_stack)
