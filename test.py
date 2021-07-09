import datetime
import random
import pandas as pd

DATA_SOURCE = [
    [1, '台北市', '大安區', 9, 1000, '台北市大安區信義路四段189號9樓'],
    [2, '台北市', '中正區', 3, 1234, '台北市中正區鎮江街1巷3號'],
    [3, '台北市', '大安區', 4, 700,  '台北市大安區羅斯福路三段235號'],
    [4, '台中市', '豐原區', 1, 500,  '台中市豐原區長壽路北2巷7號'],
    [5, '基隆市', '安樂區', 3, 750,  '基隆市安樂區樂利三街84號']
]

NUM_ROW = 10000

def main():

    # preprocessing
    print('preparing...')

    data_proto = pd.DataFrame({
            'id'      : pd.Series([], dtype='int'   ),
            'city'    : pd.Series([], dtype='object'),
            'district': pd.Series([], dtype='object'),
            'floor'   : pd.Series([], dtype='int'   ),
            'price'   : pd.Series([], dtype='int'   ),
            'address' : pd.Series([], dtype='object'),
            'score'   : pd.Series([], dtype='int'   ),
    })

    df = data_proto.copy()

    dicts = [{
            'id'      : val[0],
            'city'    : val[1],
            'district': val[2],
            'floor'   : val[3],
            'price'   : val[4],
            'address' : val[5],
            'score'   : 0,
        }
        for val in DATA_SOURCE
    ]

    # start timing
    print('timing...')
    start_time = datetime.datetime.now()

    tmp = []
    for i in range(NUM_ROW):
        d = dict(dicts[i % len(DATA_SOURCE)])
        d['id'] = i
        d['price'] += random.randint(-100, 100)
        tmp.append(d)
        # data = data.append(d, ignore_index=True)
        # data.loc[i] = d
        # print(i, data.loc[i])
    df = pd.concat([df, pd.DataFrame(tmp)])
    print(len(df))

    # end timing
    end_time = datetime.datetime.now()
    execution_time = (end_time - start_time).total_seconds()
    print(f'time spent: {execution_time}sec')

    # save for further use
    df.to_csv('data_large.csv', index=False)

if __name__ == '__main__':
    main()
