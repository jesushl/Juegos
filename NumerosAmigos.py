class NumerosAmigos:
    def __init__(self):
        self.numerosAmigos = {}

    def getNumerosAmigos(self, topNumerosAmigos):
        numerosAmigosA = []
        self.numerosAmigos.update({1:1})
        self.numerosAmigos.update({2:1})
        for i in range(3, topNumerosAmigos + 1):
            print('Generating  : {}'.format( i ), end = '\r', flush=True)
            currentSum = self.getDivisors(i)
            #print('CurrentSum : {}'.format(currentSum))
        print(self.numerosAmigos)
        for i in range(1, topNumerosAmigos):
            print('Scaning : {}'.format(i), end = '\r', flush=True)
            if i in self.numerosAmigos:
                probablyFriend = self.numerosAmigos[i]
                if probablyFriend in self.numerosAmigos:
                    if self.numerosAmigos[probablyFriend] == i:
                        numerosAmigosA.append((i, probablyFriend))
        return numerosAmigosA


    def getDivisors(self, number):
        currentSum = 0
        limit = int(number/2) + 1
        #print('Number : {}'.format(number))
        #print('limit : {}'.format(limit))
        for i in range( limit, 0 , -1):
            #print('index : {}'.format(i))
            if (number % i) == 0:
                #print('{0} % {1}'.format(number, i))
                if i in self.numerosAmigos:
                    currentSum = self.numerosAmigos[i]
                    if number > 2:
                        currentSum = currentSum + i
                    self.numerosAmigos.update({number : currentSum})
                    return currentSum
                else:
                    currentSum = currentSum + i
            #print(currentSum)
        self.numerosAmigos.update({ number : currentSum})
        #print('current sum : {}'.format(currentSum))
        return currentSum


if __name__ == "__main__":

    na = NumerosAmigos()
    topNumber = 285
    print(na.getNumerosAmigos(topNumber))
    import pdb; pdb.set_trace()
