"""
I know this is like the worst solution
but im bad at coding and wanted to make
it myself and not take it from someone
else.
"""
import multitimer
import json

def jsonWrite(file, data):
    with open(f"{file}.json", "W") as output:
        json.dump(data, output, indent=2)

def txtWrite(file, data):
    with open(f"{file}.txt", "w") as output:
        output.write(data)

class Cache:
    def __init__(self, file:str, writeTime:int, type:str, data):
        if type == "json": pass
        else: pass