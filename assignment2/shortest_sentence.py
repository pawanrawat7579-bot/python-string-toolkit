
import re

def shortest_sentence(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    if not text.strip():
        return ""

    shortest = min(sentences, key=lambda s: len(s.split()))

    return shortest

