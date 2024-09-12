#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = [
            "str is a data type in Python",
            "programming is hard, but it's worth it",
            "JavaScript async web request",
            "Python function call definition",
            "object-oriented teacher instance",
            "programming computers hacking learning terminal",
            "pipenv install pipenv shell",
            "pytest -x flag to fail fast",
        ]
    
    def teach(self):
        index = random.randint(0, len(self._knowledge) - 1)
        return self.knowledge[index]
    
    @property
    def knowledge(self):
        return self._knowledge
    
    @knowledge.setter
    def knowledge(self, new_knowledge):
        self._knowledge = new_knowledge