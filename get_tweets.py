# https://gist.github.com/yanofsky/5436496


import tweepy
import csv

#twitter API credentials
consumer_key = "GO TO"
consumer_secret = "DEV.TWITTER.COM"
access_key = "TO REGISTER YOUR APP"
access_secret = "AND GET YOUR OWN"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users moster cent 3240 tweets with this method

	#authorize twitter. initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#initialioze a list to hold tweets
	alltweets = []

	#make initaial request for most recent tweets. 200 is the maxmim allowed count
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)

	#save most recent tweets
	alltweets.extend(new_tweets)

	#save the ID of the oldest tweet less one
	oldest = alltweets[-1].id - 1

	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)

		#all subsiquent requests use the max_id param to prevent dupes
		new_tweets = api.user_timeline(screen_name = screen_name, count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)

		#update the id of the oldest tweet again
		oldest = alltweets[-1].id - 1

		print "...%s tweets downloaded so far" % (len(alltweets))

	#transform the tweepy tweets into a 2d array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.in_reply_to_screen_name, tweet.retweet_count, tweet.favorite_count] for tweet in alltweets]

	#write the csv
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text", "in reply to", "retweet count", "favorite count"])
		writer.writerows(outtweets)

	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
	user_name = raw_input("Please enter the twitter screen name you want to scrape (no @ needed):")
	get_all_tweets(user_name)

