import tweepy
import os
import gtk
import sys
class tweetBox:
    def __init__(self, api):
        self.api = api
        self.me = api.me()
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(300,120)
        self.window.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(0xF000,0xEC00,0xF500))
        self.window.connect("destroy", self.close_application)
        self.window.set_title("tweetBox")
        
        self.box = gtk.VBox(False,2)
        self.window.add(self.box)
        self.box.show()
        
        self.tbox = gtk.HBox(False,2)
        self.tbox.set_size_request(200,85)
        self.box.pack_start(self.tbox,False,False,3)
        
        self.pbox = gtk.VBox(False,2)
        self.pbox.set_size_request(75,75)
        self.tbox.pack_start(self.pbox,False,False,3)
        
        self.tweetText = gtk.TextView()
        self.tweetText.set_wrap_mode(gtk.WRAP_WORD)
        self.tweetText.modify_base(gtk.STATE_NORMAL,gtk.gdk.Color(0xF000,0xEC00,0xF500))
        self.tweetText.set_editable(True)
        self.tweetText.set_cursor_visible(False)
        self.tweetText.connect("key_release_event",self.count_char)
        self.tbox.pack_end(self.tweetText)
        
        pixbuf = gtk.gdk.pixbuf_new_from_file(self.get_dp())
        small_pixbuf = pixbuf.scale_simple(75,75,gtk.gdk.INTERP_HYPER)
        self.dp = gtk.Image()
        self.dp.set_from_pixbuf(small_pixbuf)
        self.dp.set_pixel_size(125)
        self.pbox.pack_start(self.dp,False,False,0)
        
        self.butbox = gtk.HBox(False,2)
        self.butbox.set_size_request(300,30)
        self.box.pack_end(self.butbox,False,False,3)
        self.button = gtk.Button("tweet")
        self.button.set_size_request(100,30)
        self.button.connect('clicked', self.tweet)
        self.butlabel = self.button.get_children()[0]
        #self.button.modify_bg(gtk.STATE_NORMAL,gtk.gdk.Color(0xDD00,0x4800,0x1400))
        #self.butlabel.modify_fg(gtk.STATE_NORMAL,gtk.gdk.Color(0xF000,0xEC00,0xF500))
        self.butbox.pack_end(self.button,False,False,2)
        self.button.show()
        
        self.but1 = gtk.Button("cancel")
        self.but1.set_size_request(100,30)
        self.but1.connect('clicked', self.cleartext)
        self.butbox.pack_start(self.but1,False,False,2)
        self.but1.show()
        
        self.count_char_label = gtk.Label()
        self.count_char_label.set_text("140")
        self.butbox.pack_end(self.count_char_label,False,False,5)
        #self.butbox.pack_end(self.dp,False,False,3)
        self.window.show_all()
    
    def cleartext(self, widget, data=None):
        buf = self.tweetText.get_buffer()
        buf.set_text("")
        self.tweetText.set_buffer(buf)
        self.count_char_label.set_text("140")
        self.count_char_label.show()
    
    def count_char(self,widget,data=None):
        char_buffer = self.tweetText.get_buffer()
        num_char = char_buffer.get_char_count()
        text = char_buffer.get_text(char_buffer.get_start_iter(),char_buffer.get_end_iter())
        self.count_char_label.set_text(str(140-num_char))
        self.count_char_label.show()
    
    def tweet(self, widget, data=None):
        tweet_buffer = self.tweetText.get_buffer()
        text = tweet_buffer.get_text(tweet_buffer.get_start_iter(),tweet_buffer.get_end_iter())
        if text:
            status = self.api.update_status(text)
            if status:
                self.tweet_buffer.set_text('')
                self.tweetText.set_buffer(tweet_buffer)
        self.window.show_all()
        return
        
    def close_application(self, widget):
        gtk.main_quit()
        
    def get_dp(self):
        files = os.listdir(os.getcwd())
        if "display_pic.jpg" in files:
            pass
        else:
            import urllib
            url = "_".join(self.me.profile_image_url.split("_")[0:-1])+"."+self.me.profile_image_url.split("_")[-1].split(".")[-1]
            urllib.urlretrieve(url,"display_pic.jpg")
            print "pic downloaded"
        return os.path.join(os.getcwd(),"display_pic.jpg")
        
def tweet():
    CONSUMER_KEY = "" # your consumer key here
    CONSUMER_SECRET = "" # your consumer secret here
    ACCESS_KEY = "" # your access key here
    ACCESS_SECRET = "" # your access token here
    if CONSUMER_KEY and CONSUMER_SECRET and ACCESS_KEY and ACCESS_SECRET:
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
        try:
            api=tweepy.API(auth)
        except tweepy.error.TweepError:
            print "Please check consumer key/consumer secret/access key/access secret and re-install"
            sys.exit()
        tweetBox(api)
        gtk.main()
    else:
        print "Please add consumer key/consumer secret/access key/access secret and re-install"
        sys.exit()
        
    
