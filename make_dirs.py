import pathlib

YEAR = (2017, 2015)

for i in range(YEAR[0], YEAR[1]-1, -1):
    print(i)
    pathlib.Path(f'data/{str(i)}').mkdir(parents=True)
