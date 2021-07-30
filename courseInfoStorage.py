'''
Creates all class found for a specific degree/major at X school
'''

class baseCourse():
    # This class is the base design for all courses with or without prereqs
    """
    Created 07/20/2021 by MFF
    """

    def __init__(self, courseName, courseID, courseType, courseInfo, courseCredits):
        #Strings
        self.name = courseName
        self.type = courseType
        self.info = courseInfo

        #Int
        self.id = courseID
        self.credits = courseCredits

        #String concat with int
        self.key = self.setKey()

    # Set the key for the current course
    def setKey(self):
        return self.getType() + str(self.getID())

    '''
    Default lookup operations for the baseCourse class
    '''
    def getName(self):
        return self.name

    def getID(self):
        return self.id

    def getType(self):
        return self.type

    def getInfo(self):
        return self.info

    def getCredits(self):
        return self.credits

    def getKey(self):
        return self.key

class nonBaseCourse(baseCourse):
    # This class is a baseCourse but also has prereqs
    """
    Created 07/20/2021 by MFF
    """

    #Call super and define extra var for nonBaseCourse
    def __init__(self, courseName, courseID, courseType, courseInfo, courseCredits, *args):
        self.prereqs = []

        baseCourse.__init__(self, courseName, courseID, courseType, courseInfo, courseCredits)

        for x in args:
            try:
                if isinstance(x, baseCourse) or isinstance(x, nonBaseCourse):
                    self.prereqs.append(x)
            except TypeError as err:
                print(err)
                print("Not of type course. Wrong data.")

    # Returns the list form of the prereq classes for this current course.
    def getPrereqs(self):
        return self.prereqs

##END##
