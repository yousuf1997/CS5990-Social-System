from Model import Matrix

matrix = Matrix()

matrix.put("A", "B")
matrix.put("A", "E")
matrix.put("A", "D")
matrix.put("B", "A")
matrix.put("B", "C")
matrix.put("C", "B")
matrix.put("C", "E")
matrix.put("C", "F")
matrix.put("D", "A")
matrix.put("D", "E")
matrix.put("E", "D")
matrix.put("E", "A")
matrix.put("E", "C")
matrix.put("E", "F")
matrix.put("F", "C")
matrix.put("F", "E")

print(matrix.getEdges("C"))