#显示物品列表
def read_dict():
    fr = open('dic.txt', 'r',encoding='utf-8')
    dic = {}
    keys = []
    for line in fr:
        v = line.strip().split(':')
        if v[0] == '':
            print("暂未收到任何物品，请您添加！")
            return
        dic[v[0]] = int(v[1])
        keys.append(v[0])
    fr.close()
    print("物品列表：")
    for i in dic:
        print(i + "："+ str(dic[i]))
    print(" ")

#添加物品信息
def add(article, quantity):
    fr = open('dic.txt', 'r',encoding='utf-8')
    dic = {}
    keys = []
    for line in fr:
        v = line.strip().split(':')
        if v[0] == '':
            fw = open('dic.txt', 'a',encoding='utf-8')
            fw.write(article + ':' + str(quantity) +'\n')
            fw.close()
            return
        dic[v[0]] = int(v[1])
        keys.append(v[0])
    tmp = dic.get(article, 0)
    fr.close()
    if tmp == 0 :
        fw = open('dic.txt', 'a',encoding='utf-8')
        fw.write(article + ':' + str(quantity) +'\n')
        fw.close()
    else:
        with open('dic.txt','r',encoding='utf-8') as fr:
                lines=fr.readlines()
        with open('dic.txt','w',encoding='utf-8') as fw:
                for line in lines:
                    v=line.strip().split(':')
                    if article == v[0]:
                        fw.write(article + ':' +str(dic[article]+quantity)+ '\n')
                    else:
                        fw.write(line)
        fr.close()
        fw.close()

            
#查找物品信息
def search(article):
        fr = open('dic.txt','r',encoding='utf-8')
        for line in fr:
            v = line.strip().split(':')
            tmp = 0
            if article in v[0]:
                print(v[0]+"："+v[1])
                tmp = 1
                break
        
        if tmp ==0 : print("清单中没有您要查找的物品")
        fr.close()

#删除物品信息
def delete(article,number):
        tmp = 0
        with open('dic.txt','r',encoding='utf-8') as fr:
            lines = fr.readlines()
        with open('dic.txt','w',encoding='utf-8') as fw:
            for line in lines:
                v = line.strip().split(':')
                
                if article == v[0]:
                    if number == int(v[1]):
                        tmp = 1
                        continue
                    elif number > int(v[1]):
                        tmp = 1
                        print("个数输入错误！")
                        fw.write(line)
                    else:
                        fw.write(article + ':' +str(int(v[1])-number)+ '\n')
                elif v[0] != '':
                    fw.write(line)
        if tmp == 0 :
            print("清单中没有该项物品！")    
        fr.close()
        fw.close()



def main():
    while True:
        print("请选择您需要的操作：1.添加物品信息；2.删除物品信息；3.显示物品列表；4.查找物品信息；5.退出程序")
        choice = int(input())
        if choice ==1:
            print("请输入物品名称：")
            article = input()
            print("请输入数目：")
            quantity = int(input())
            add(article, quantity)
        if choice ==2:
            print("请输入物品名称：")
            article = input()
            print("请输入要删除的个数：")
            number = int(input())
            delete(article,number)
        if choice ==3:
            read_dict()
        if choice ==4:
            print("请输入要查找的物品")
            article = input()
            search(article)
        if choice == 5:
            break


main()
