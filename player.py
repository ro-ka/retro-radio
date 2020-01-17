import vlc

instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
player = instance.media_player_new()

def playUrl(url):
  media=instance.media_new(url)
  media.get_mrl()
  player.set_media(media)
  player.play()
