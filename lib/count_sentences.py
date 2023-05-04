#!/usr/bin/env python3
import ipdb

class MyString:
  
    def __init__(self, value = ''):
        self._value = value

    def get_value(self):
        print('Inside the getter')
        return self._value
    
    def set_value(self, value):
        if type(value) == str:
            print('Inside the setter')
            self._value = value
        else: 
            print("The value must be a string.")

    def is_sentence(self):
        if self.value.endswith('.'):
            return True
        else: 
            return False
        
    def is_question(self):
        if self.value.endswith('?'):
            return True
        else: 
            return False
        
    def is_exclamation(self):
        if self.value.endswith('!'):
            return True
        else: 
            return False

    def count_sentences(self):
        for end in ['?','!']:
            self.value = self.value.replace(end, '.')
        
        sentences = self.value.split('.')

        good_sentences = [sentence for sentence in sentences if len(sentence) > 0]
        
        return len(good_sentences)
        
        
    value = property(get_value, set_value)
                
# ipdb.set_trace()