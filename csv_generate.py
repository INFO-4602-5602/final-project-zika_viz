import random
import json, csv

def main():

    oppoList = []
    f = open('./data/collect_zika.json')
    x = 0; y = 0
    for line in f:
        l = []
        data = json.loads(line)
        l.append(str(x))
        x += 1
        l.append(str(y))
        l.append(data['text'])
        if x%31 == 0:
            x = 0
            y += 1
        oppoList.append(l)
    f.close()

    topicList = []
    f = open('./data/topic.csv')
    for line in f:
        l = line.strip().split(',')
        if l[0] != 'index':
            topicList.append(l[1])
    f.close()

    dateList = []
    f = open('./data/time_series.csv')
    for line in f:
        l = line.strip().split(',')
        if l[0] != 'created_at':
            dateList.append(l[0])
    f.close()

    sentiList = []
    f = open('./data/sentiment.csv')
    for line in f:
        l = line.strip().split(',')
        if l[0] != 'x':
            sentiList.append(l[2])
    f.close()

    for i in range(len(oppoList)):
        oppoList[i].append(topicList[i])
        oppoList[i].append(dateList[i])
        oppoList[i].append(sentiList[i])

    with open('./data/tst.csv','w') as csvfile:
        fieldnames = ['x','y','senti','text','topic','created_at']
        writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
        writer.writeheader()
        for i in oppoList:
            x = random.uniform(0,1)
            if i[3] == '0':
                d = {'x':i[0],'y':i[1],'senti':i[5],'text':i[2], 'topic':'cost', 'created_at':i[4]}
            if i[3] == '1':
                d = {'x':i[0],'y':i[1],'senti':i[5],'text':i[2], 'topic':'Infection source', 'created_at':i[4]}
            if i[3] == '2':
                d = {'x':i[0],'y':i[1],'senti':i[5],'text':i[2], 'topic':'travel', 'created_at':i[4]}
            if i[3] == '3':
                d = {'x':i[0],'y':i[1],'senti':i[5],'text':i[2], 'topic':'research', 'created_at':i[4]}
            if i[3] == '4':
                d = {'x':i[0],'y':i[1],'senti':i[5],'text':i[2], 'topic':'children', 'created_at':i[4]}
            if i[3] == '5':
                d = {'x':i[0],'y':i[1],'senti':i[5],'text':i[2], 'topic':'social media', 'created_at':i[4]}
            if i[3] == '6':
                d = {'x':i[0],'y':i[1],'senti':i[5],'text':i[2], 'topic':'others', 'created_at':i[4]}

            writer.writerow(d)
        csvfile.close()
if __name__ == '__main__':
    main()
