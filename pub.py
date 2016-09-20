import sys
import redis

if __name__ == '__main__':
    name = sys.argv[1]
    channel = sys.argv[2]

    print 'Welcome to new {channel}'.format(**locals())

    while True:
        message = raw_input('Enter a message: ')

        if message.lower() == 'exit':
            break

        message = '{name} says: {message}'.format(**locals())
        r=redis.StrictRedis(host='localhost',port=6379,db=0)
        r.publish(channel, message)
