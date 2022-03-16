class color():
    def __init__(self, color):
        self.color = ""
        if color == "TEST":
            self.color = "test"
        if color == "BLUE":
            self.color = '\033[94m'
        if color == "YELLOW":
            self.color = '\033[93m'
        if color == "GREEN":
            self.color = '\033[92m'
        if color == "RED":
            self.color = '\033[91m'
        if color == "END":
            self.color = '\033[0m'
        # PURPLE = '\033[95m'
        # CYAN = '\033[96m'
        # DARKCYAN = '\033[36m'
        # BOLD = '\033[1m'
        # UNDERLINE = '\033[4m'
