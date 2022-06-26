class Mapmanager():
    def __init__(self):
        self.model = 'block.egg' # модель кубика в файле block.egg
        self.texture = 'block.png'# текстура кубика           
        self.colors = [
                  (0.5, 0.3, 0.0, 1),
                  (0.2, 0.2, 0.3, 1),
                  (0.5, 0.5, 0.2, 1),
                  (0.0, 0.6, 0.0, 1)]
        self.startNew() # ШАГ 4 | даём понять, что мы создали карту
        
    

        
        # создаём строитель
    def startNew(self): # ШАГ 1 | создаем *карту*
        self.land = render.attachNewNode("Land")


    def getColor(self, z):
        if z < len(self.colors):
            return self.colors[z]
        else:
            return self.colors[len(self.colors) - 1]
            

    def addBlock(self, position): # ШАГ 2 | описываем создание 1 блоканые блоки 
        self.block = loader.loadModel(self.model) # модель блока
        self.block.setTexture(loader.loadTexture(self.texture)) # текстура
        self.block.setPos(position) # позиция, её мы получаем когда вызываем этот метод
        self.color = self.getColor(int(position[2]))
        self.block.setColor(self.color) # цвет блока
        self.block.reparentTo(self.land) # ШАГ 3 | связываем блок в узел с картой land
    

    
    def loadLand(self, filename):
        with open(filename) as file:
            y = 0
            for line in file:
                x = 0
                line = line.split(' ')
                for z in line:
                    if z == '':
                        x += 1
                    else:
                        for z0 in range(int(z)+1):
                            block = self.addBlock((x, y, z0))
                    x += 1
                y += 1