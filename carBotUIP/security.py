class Security:
    list = [116708028]
    def validar(self, id):
        return self.list[id]
    def add(self, id):
        self.list.append(id)
    def remove(self, id):
        self.list.remove(id)
    def getUser(self):
        print(self.list)
