class AjustPolin:
    def __init__(self, allX:list, allY:list) -> None:
        if AjustPolin.validaPares(allX, allY):
            self.allX = allX
            self.allY = allY
            self.qtdPares = len(allX)
        else:
            raise Exception('Os pares passados como parâmetro estão incompletos')

    def validaPares(allX, allY):
        return len(allX) == len(allY)
    
    '''
    parse num
    '''
    def pNum(num):
        return f'{num:.5f}'