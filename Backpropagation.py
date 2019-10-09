import numpy as np

class NeuralNetwork():
    def __init__(self,input_numbers):
        self.learning_constant = 0.16
        self.input_numbers = input_numbers
        self.layers_numbers = 7
        self.ouput_layers = 4 
        self.w1 = np.random.rand(input_numbers, self.layers_numbers)
        self.w2 = np.random.rand(self.layers_numbers,self.ouput_layers)

    def train(self,inputs,ex_output):
        salidas = []
        for inputone,outputstone in zip(inputs,ex_output):

            #Calculating layers and outputs            
            layers,output = self.spread(inputone)

            #Calculating errors
            errores_outputs = np.asarray(self.calculate_mistakes_outputs(outputstone,output)) #Errores de la capa salidA
            errores_layers = np.asarray(self.calculate_mistakes_layers(layers,errores_outputs)) #Errores de la capa ENTRADA

            
            #Modifico los pesos W2
            for j in range(self.ouput_layers):                
                for i in range(self.layers_numbers):
                    self.w2[i][j] = self.w2[i][j] + self.calculate_delta(errores_outputs[j],layers[i])
            
            #Modifico los peros w1
            for j in range(self.layers_numbers):
                for i in range(self.input_numbers):
                    self.w1[i][j] = self.w1[i][j] + self.calculate_delta(errores_layers[j],inputone[i])
            
            salidas.append(output)
        
        #print(np.asarray(salidas))
        #print("")
        #print("-------------------------")

            
            
    
    def calculate_delta(self,error,capa):                
        delta = self.learning_constant * error * capa
        return delta
            
    def calculate_mistakes_outputs(self,outputstone,output):          
        error = output*(1-output)*(outputstone-output)
        return error
    
    def calculate_mistakes_layers(self,layers,errores_outputs):
        errores = []
        for j in range(self.layers_numbers):

            error = layers[j]*(1-layers[j])*sum(errores_outputs*self.w2[j])
            errores.append(error)
        
        return np.asarray(errores)
             
    def spread(self,inputs):
        #------------------------------------------
        list_layers = []        
        for h in range(self.layers_numbers):
            hi = self.sigmoid(sum(inputs*self.w1[:,h]))
            list_layers.append(hi)
        layers = np.asarray(list_layers)
        #------------------------------------------print(hi)
        list_ouputs = []            
        for o in range(self.ouput_layers):
            oi = self.sigmoid(sum(layers*self.w2[:,o]))
            list_ouputs.append(oi)
        outputs = np.asarray(list_ouputs)
        #------------------------------------------
        return layers,outputs        


    def sigmoid(self,x):
        return 1.0/(1+ np.exp(-x))  