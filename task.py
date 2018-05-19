import schedule
from tools.fetch import multi_fetch


def job():
    try:
        result = multi_fetch()
        print(result[0])
    except Exception as e:
        print(e)


if __name__ == '__main__':
    schedule.every(10).seconds.do(job)
    while True:
        schedule.run_pending()