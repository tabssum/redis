
import sys
import redis
if __name__ == '__main__':
    channel = sys.argv[1]
    r=redis.StrictRedis(host='localhost',port=6379,db=0)
    pubsub = r.pubsub()
    pubsub.subscribe(channel)

    print 'Listening to {channel}'.format(**locals())

    while True:
        for item in pubsub.listen():
            print item['data']
