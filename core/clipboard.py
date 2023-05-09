import re
from tkinter import Tk


class ClipboardManager:
    """Class in charge of managing the content copied by the
    user to the clipboard of the operating system.
    """

    dummy_app = Tk()
    dummy_app.withdraw()
    vocab = dummy_app.clipboard_get()
    if vocab.strip().count(" ") > 1:
        # Search additional whitespaces in the text after removing them from the beginning and the end of the original string.
        vocab = re.sub("[\x00-\x1f]", " ", vocab)  # Removing control characters.
        sentence = list()
        sentence.append(vocab)
        sentence = tuple(sentence)

    else:
        vocab = vocab.split()
        for i in range(len(vocab)):
            word = (vocab[i],)
