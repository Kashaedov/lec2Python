#  Данные для запсии в файл 2 способа.
# Первый способ!
# with open('file.txt', 'a') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')
# Второй способ!
# colors = ['red', 'green', 'blue3123']
# data = open('file.txt', 'a')
# # data.writelines(colors) # разделителей не будет
# data.write('line 122\n')
# data.write('line 222\n')
# data.close()
#  Способ чтения файлов:
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()