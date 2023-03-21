import re
from tkinter import Tk


def clipboard_manager():
    """The function classifies the content selected and copied 
    by the user in the OS clipboard.
    """
    dummy_app = Tk() 
    dummy_app.withdraw()
    vocab = dummy_app.clipboard_get()
    if vocab.strip().count(" ") > 1: 
    # Search additional whitespaces in the text after removing them from the beginning and the end of the original string. 
        vocab = re.sub("[\x00-\x1f]", " ", vocab) # Removing control characters.
        sentence = list()
        sentence.append(vocab)
        sentence = tuple(sentence)
        return sentence
    else:
        vocab = vocab.split()
        for i in range(len(vocab)):
            word = (vocab[i],)
            return word 
    
