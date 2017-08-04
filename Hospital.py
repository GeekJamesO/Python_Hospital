class Patient:
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def display(self):
        print "  Patient: ID:{0}  Name:'{1}' Allergic to:'{2}' Bed#:{3}".format(self.id, self.name, self.allergies, self.bed_number)
        return self
    def assignBed(self, bedNum):
        self.bed_number = bedNum

class Hospital:
    def __init__(self, name, capacity):
        self.name = name
        self.Patients = []
        self.EmptyBeds = range(capacity)

    # Admit: add a patient to the list of patients.
    # Assign the patient a bed number.
    # If the length of the list is >= the capacity do not admit the patient.
    # Return a message either confirming that admission is complete or saying the hospital is full.
    def Admit(self, aPatient):
        if (len(self.EmptyBeds) <= 0):
            #we are full
            print "I am sorry {0}, but we are full.  Try St. Mongos down the street".format(aPatient.name)
        else:
            #we have room
            anEmptyBed = self.EmptyBeds.pop()
            aPatient.assignBed(anEmptyBed)
            self.Patients.append(aPatient)
            print "Welcome {0} to {1}, you are in bed# {2}".format(aPatient.name, self.name, aPatient.bed_number)
        return self
         # Discharge: look up and remove a patient from the list of patients.
         # Change bed number for that patient back to none.
    def Discharge(self, aPatientName):
        thisPatient = None
        #need an index here..
        for a in self.Patients:
            if aPatientName == a.name:
                thisPatient = a
                break;
        if (thisPatient == None):
            print "There is no patient with the name of '{0}' to discharge.  ERROR".format(aPatientName)
        else:
            anEmptyBed = thisPatient.bed_number
            thisPatient.assignBed(None)
            self.EmptyBeds.append(anEmptyBed) #add bed to array of empty beds.
            self.Patients.remove(thisPatient)
        return self
    def PatientList(self):
        print "Patient List: "
        for x in self.Patients:
            x.display()
        print "Empty Beds: "
        for y in self.EmptyBeds:
            print "  ", y
        return self
    def Status(self):
        print "Here at '{0}' we have {1} Empty beds".format(self.name, len(self.EmptyBeds))
        PatientList()
        return self

alpha = Patient(000, "alpha", "Annice")
bravo = Patient(11, "bravo", "Bad Puns")
charlie = Patient(222, "charlie", "Crepes")
delta = Patient(3, "Delta", "Dogs")
echo = Patient(44, "Echo", "Electralights")
foxtrot = Patient(555, "Foxtrot", "Fur")




foo = Hospital("St. Josephs of Nebraska", 5)

foo.PatientList()
foo.Admit(alpha)
foo.Admit(bravo)
foo.Admit(charlie)
foo.Admit(delta)
foo.Admit(echo)
foo.PatientList()
foo.Admit(foxtrot) # we are full
foo.Discharge(delta.name)
foo.PatientList()
foo.Admit(foxtrot) # we are full
foo.PatientList()
