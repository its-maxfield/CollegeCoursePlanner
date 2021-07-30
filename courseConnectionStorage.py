'''
Stores all course objects based on current major in hashmap to easily assemble the tree.

i.e.
{
    BIO123 : corresponding base or nonbase course,
    ...,
    ...,
    MATH23 : base or nonbase course
}
'''

import courseInfoStorage as CIS

class courseConnections():
    '''
    Created 07/21/2021 by MFF
    '''

    def __init__(self, courses):
        self.courses = courses
        self.courseMap = {}

    def coursesToMap(self):
        #Take the list of courses and then using access paramters store in the hashmap

        for course in self.courses:
            courseKey = course.getKey()

            if courseKey not in self.courseMap:
                self.courseMap[courseKey] = course

        return

    # Return the prereq classes for a give course key
    def returnPrereqs(self, courseKey):
        if courseKey in self.courseMap:
            try:
                return self.courseMap[courseKey].getPrereqs()
            except TypeError as err:
                print(err)
                print("Requested course has no prereqs")

        return

    def returnCourse(self, courseKey):
        if courseKey in self.courseMap:
            return self.courseMap[courseKey]

        return

##END##
