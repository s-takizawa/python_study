
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    
    def public_method(self):
        # can use by client
        pass

    def _unsafe_method(self):
        # can not use by client
        pass