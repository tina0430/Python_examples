from sklearn import datasets
iris = datasets.load_iris()

print(type(iris))

print(len(iris.data))

print(len(iris.target))

print(len(iris.data[0]))
#꽃받침 길이,  꽃받침 너비, 꽃잎 길이
print(set(iris.target))