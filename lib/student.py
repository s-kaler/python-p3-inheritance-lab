#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
    
    @property
    def knowledge(self):
        return self._knowledge
    
    @knowledge.setter
    def knowledge(self, new_knowledge):
        self._knowledge = new_knowledge

    def learn(self, new_knowledge):
        self._knowledge.append(new_knowledge)