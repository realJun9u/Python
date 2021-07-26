import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.Series(data)
print(myvar)
myvar = pd.DataFrame(data)
print(myvar)
