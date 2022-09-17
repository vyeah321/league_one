import datetime

league_one = 'リーグワンD1'
team = '横浜キヤノンイーグルス'
is_team = True
file = team if is_team else league_one
csv_file = open(file + '.csv', 'w')
data_file = open('LEAGUE_ONE_DIVISION1.txt', 'r')

datalist = data_file.readlines()

csv_file.write('Start date,Subject,Location\n')
for data in datalist:
    if data[0].isdigit():
        game = data.split()
        if game[3] != team and game[5] != team and is_team:
            continue
        year = '2022年' if game[0][1] == '2' else '2023年'
        date_str = year + game[0]
        date_format = '%Y年%m⽉%d⽇'
        date_dt = datetime.datetime.strptime(date_str, date_format)
        date = date_dt.strftime('%x')
        schedule = '{},{} {} {},{}\n'.format(date, game[3], game[4], game[5], game[7])
        print(date_dt, schedule)
        csv_file.write(schedule)

data_file.close()
csv_file.close()