class Dept:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.patients = {}

    def __str__(self):
        return "Department: {}, Location: {}, # of patients: {}".format(self.name, self.location, len(self.patients))

    class Patient:
        def __init__(self, name, dept, condition, treatment):
            self.name = name
            self.dept = dept
            self.condition = condition
            self.treatment = treatment
            dept.patients[self.name] = self

        def __str__(self):
            return 'Patient Name: {}, Department: {}, Condition: {}, Treatment Plan: {}'.format(self.name, self.dept.name,
                                                                                                self.condition,
                                                                                                self.treatment)

if __name__ == '__main__':
    gastro = Dept("Gastroenterology", "3rd Floor")
    som = Dept("Somnology", "2nd Floor")
    psych = Dept("Psychiatry", "5th Floor")

    leah = gastro.Patient("Leah", gastro, "GERD", "Stop eating so much ice cream, Jesus")
    shahroz = som.Patient("Shahroz", som, "Sleep Deprivation", "Stop going to sleep at 6 A.M.")
    gadget = psych.Patient("Gadget", psych, "5 A.M. Craziness", "Yeet him")

    print(gastro)
    print(som)
    print(psych)
    print("----------------------------------------------")
    print(leah)
    print(shahroz)
    print(gadget)
