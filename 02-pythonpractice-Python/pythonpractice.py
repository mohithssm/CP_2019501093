"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""

class Classy(object):
    def __init__(self):
        self.items = []

    def addItem(self, str):
        self.items.append(str)
    
    def classiness(self):
        sum = 0
        for elem in self.items:
            if (elem == "tophat"):
                sum = sum + 2
            elif (elem == "bowtie"):
                sum = sum + 4
            elif (elem == "monocle"):
                sum = sum + 5
        return sum