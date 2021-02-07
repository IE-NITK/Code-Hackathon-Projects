from summarizer import Summarizer

body="""Greetings from ISTE NITK!

This week with our More You Know series, we bring to you a partially open-source network on nearly all formal research going on around the world.

 The Microsoft Academic Knowledge Graph is one of the largest databases containing over 8 Billion triplets of data on researchers,research articles and conferences. It is available for public use through a SparQL endpoint.

Go through our post and see if it excites the Data Analytics enthusiast within you. 

https://www.instagram.com/p/CK9JENRA2Fd/"""
model = Summarizer()
result = model(body, min_length=60)
full = ''.join(result)
print(full)