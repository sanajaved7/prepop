while True:
    content = raw_input("Would you like to prepopulate content for Twitter or Facebook? Reply 'Twitter' or 'Facebook' ")

    if content.lower() == "twitter":
        oldtweet = raw_input("Great. Enter the tweet you would like prepopulated: ")
        if len(oldtweet) > 140:
            print "Heads up! That tweet is more than 140 characters!"
        new_tweet = oldtweet.replace(" ", "+").replace("#", "%23")
        header = "http://twitter.com/intent/tweet?text="
        print "Here is your prepopulated Tweet! " + header + new_tweet


    if content.lower() == "facebook":
        oldlink = raw_input("Awesome. Please enter what URL you want to share: ")
        newlink = oldlink.replace("/", "%2F")
        fbshare = 'http://www.facebook.com/sharer.php?u=newlink'
        newfb = fbshare.replace("newlink", newlink)
        print "Here is your prepopulated Facebook share! " + newfb

    x = raw_input("Do you want to prepopulate more content? Reply 'yes' or 'no' ")

    if x.lower() == "no":
        break