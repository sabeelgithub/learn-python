class VersioControl:
    def __init__(self):
        self.version_value = ['']
        self.version_number = 0

    def version_value_find(self,version_number):
        if 0 <= version_number < len(self.version_value):
            return print(self.version_value[version_number])
        else:
            return print("version not found")
        
    def add_version(self,value):
        splitted_value = value.split('-')
        current_version_value = self.version_value[self.version_number]
        if 'A' in splitted_value:
            version_value_to_add = current_version_value + splitted_value[1]
            self.version_value.append(version_value_to_add)
            self.version_number += 1
        if 'D' in splitted_value:
            if 0 <= int(splitted_value[1]) < len(current_version_value):
                version_value_to_add = current_version_value[:int(splitted_value[1])] + current_version_value[int(splitted_value[1])+1:]
                self.version_value.append(version_value_to_add)
                self.version_number -= 1
            else:
                return print("there is no specified index for value")


    def all_version(self):
        return print(self.version_value)
        

vc = VersioControl()
vc.version_value_find(0)
vc.all_version()
vc.add_version('A-h')
vc.add_version('A-i')
vc.add_version('A-kooi')
vc.all_version()
vc.version_value_find(3)
vc.add_version('D-10')
vc.all_version()

