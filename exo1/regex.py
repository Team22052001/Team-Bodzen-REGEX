#!/usr/bin/env python3
import re

from pathlib import Path
contents = Path("exo1.txt").read_text()


informations = re.sub("[^A-Z ]", "", contents)
print(informations)