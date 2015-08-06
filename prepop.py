def prepop_twitter(oldtweet):
    new_tweet = oldtweet.replace(" ", "+").replace("#", "%23")
    header = "http://twitter.com/intent/tweet?text="
    return header + new_tweet

def prepop_facebook(oldlink):
    newlink = oldlink.replace("/", "%2F")
    fbshare = 'http://www.facebook.com/sharer.php?u=newlink'
    newfb = fbshare.replace("newlink", newlink)
    return newfb
