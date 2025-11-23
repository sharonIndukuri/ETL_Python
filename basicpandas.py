import pandas as pd 

a = pd.read_csv("TestData.csv")
b = pd.read_csv("TestDataTar.csv")

'''
#No of rows
print(pd.options.display.max_rows) 

#First n rows
print(a.head(7))

#replace nulls with
print(a.fillna(444, inplace=True))
print(a.head(7))

#check if duplicates
print(a.duplicated())

#drop duplicates
print(a.drop_duplicates(inplace=True))
print(pd.options.display.max_rows)
print(a.tail(10))


modelyear = a[a["Model Year"]<2015]
print(modelyear)

if len(a) == len(b):
    print("same")
else:
    print("idk")

nulls = a.isnull().sum()
print(nulls)


#check if duplicates
isdupli = a.duplicated()
print(isdupli)
show = a[a.duplicated()]
print(show)


print(a.isnull().sum())

'''
print(a.count())
print(b.count())




'''
assert len(a) == len(b) , "not same"

a = [12, 23, 34, 45, 56]
print(pd.Series(a))


data = {
  "calories": [1, 2, 3],
  "duration": [4, 5, 6]
}
pf = pd.DataFrame(data)
print(pf)
print()
print(pd.DataFrame(data).loc[0])
print()
print(pd.DataFrame(data).loc[[0,2]])'''


