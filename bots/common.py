from random import randint
import re

class common_bot(object):
    def __init__(self, filename):
        self.filename = filename

    def create_response(self, args):
        with open(self.filename, "r", encoding = "UTF-8") as f:
            lines = f.readlines()
        return self.formatString(lines[randint(0, len(lines) - 1)]).replace("$1", " ".join(args))

    def formatString(self, s):
        if s.find("{") != -1:
            result = re.findall('{(.+?)}', s)
            s = s.replace("{", "")
            s = s.replace("}", "")
            arguments = result
            for a in arguments:
                choices = a.split("|")
                s = s.replace(a, choices[randint(0, len(choices) - 1)].strip())
        return (s)

    def add(self, args):
        new_line = " ".join(args)

        if new_line:
            with open (self.filename, "r") as f:
                lines = [line for line in f if line.strip()]
            with open (self.filename, "w") as f:
                for line in lines:
                    f.write(line)
                if line[-1].find("\n") == -1:
                    f.write("\n")
                f.write(new_line)

            return "Added " + new_line + " to " + self.filename
        else:
            return "Õpi kirjutama, loll. Tühja asja ma ei söö."