from abc import ABC , abstractmethod

class BaseExtractor(ABC):
    @abstractmethod
    def extract(self): pass

class csv(BaseExtractor):
    def extract(self):
        print("csv...")

class api(BaseExtractor):
    def extract(self):
        print("api..")

class basetransformer(ABC):
    @abstractmethod
    def transformer(self): pass

class clean(basetransformer):
    def transformer(self):
        print("clean....")

class basline(ABC):
    @abstractmethod
    def run(self):
        pass

class pipeline(basline):

    def __init__(self,extactor,transformer):
        self.extractor=extactor
        self.transformer=transformer
        
    def run(self):
        self.extractor.extract()
        self.transformer.transformer()

p = pipeline(csv(),clean())
p.run()
        

