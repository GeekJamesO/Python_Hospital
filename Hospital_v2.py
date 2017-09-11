# Assignment: Hospital
class Patient(object):
    def __init__(self, id, name, allergies, bedNumber = None):
        self.id = id
        self.name=name
        self.allergies = allergies
        self.bedNumber = bedNumber
    def __str__(self):
        return "  Patient Id:{}  Name:{}  Allergies:{}  Bed Number:{}".format(self.id, self.name, self.allergies, self.bedNumber)

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity
        self.beds = []
        for i in range(0, capacity):
            self.beds.append("{}".format(i))
    def __str__(self):
        print "-" * 10, "Hospital", self.name, "-" * 10
        print "Bed capacity: {}   Patient Count: {}".format(self.capacity, len(self.patients) )
        for pat in self.patients:
            print pat.__str__()
        print "-" * 10, "End Hospital report" , self.name, "-" * 10
    def Admit(self, aPatient):
        if len(self.beds) < 1:
            print "I am sorry {}, the hospital is too full to take you today..".format(aPatient.name), "**" * 10
        else:
            freebed = self.beds.pop()
            aPatient.bedNumber = freebed
            self.patients.append(aPatient)
            print "Welcome patient {}, you will be in bed {}".format(aPatient.name, freebed)
        return self

    def Discharge(self, patientId):
        thisPatient = None
        for pat in self.patients:
            if pat.id == patientId:
                thisPatient = pat
                break
        if thisPatient == None:
            print "Patient with id of '{}' is not currently in the hospital.".format(patientId), "**" * 10
        else:
            self.beds.append(thisPatient.bedNumber)
            thisPatient.bedNumber = None
            self.patients.remove(thisPatient)
            print "Thank you. Patient {}, you will be missed.  Take care".format(thisPatient.name)
        return self


Wiskey = Patient(id="101", name="Wilson Wiskey", allergies=[])
Xray   = Patient(id="987", name="Xander XRay", allergies=['lead'])
Yankee = Patient(id="876", name="Yonkers Yankee", allergies=['Peanuts'])
ZooLoo = Patient(id="999", name="Zed ZooLoo", allergies=['Zircons'])

capacity = 3
h = Hospital("St. Luckies", capacity)

h.Admit(Wiskey)
h.Admit(Xray)
h.Admit(Yankee)
print h.__str__()
h.Admit(ZooLoo)

h.Discharge('987')
print h.__str__()
h.Admit(ZooLoo)

h.Discharge('BadIdNumber')
h.Discharge("101")
h.Discharge("876")
h.Discharge("999")
print h.__str__()
