import src


print("Processing data...")
_, measure = src.fetch_and_process()
print("Creating graph...")
g = src.make(measure)
g.show()
print("<PRESS RETURN TO EXIT>")



