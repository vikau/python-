class animal:
    def __init__(self,animal_name,animal_type):
        print("construtor callld")
        self.name=animal_name
        self.type=animal_type

    def display(self):
        print("{0} {1}".format(self.name,self.type))

zerman=animal("zerman_sefald","DOG")
zerman.display()


ca=animal("micky","CAT")
ca.display()

