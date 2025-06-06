class ComposerDetection:

    def __init__(self,
                 x1: int,
                 y1: int,
                 x2: int,
                 y2: int,
                 tag: str,
                 command_name: str
                 ):

        self.x1: int = x1
        self.y1: int = y1

        self.x2: int = x2
        self.y2: int = y2

        self.tag: str = tag

        self.on_p1: bool = False
        self.on_p2: bool = False

        self.anchored_p1 = False
        self.anchored_p2 = False

        self.corner_amplitude = 10

        self.command_name: str = command_name

        pass
