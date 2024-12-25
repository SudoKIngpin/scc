from pytube import YouTube


'''
{       URL OBJECT DATA
        "title":Video title,
        "views":Video views,
        "length":Video length,
        "videos": Progressive mp4 streams,
        "audios": All audio streams 
        
    }
'''
def yt(url):
    ytob=YouTube(url)
    videos=ytob.streams.filter(progressive=True,file_extension='mp4') 

    ytdict={
        'url':url,
        'thumb':ytob.thumbnail_url,
        'title':ytob.title,
        'views':ytob.views,
        'length':ytob.length,
        'videos':videos, # vid in videos vid.url(360,720) contain download link
        "audios":ytob.streams.filter(type="audio")

    }

    return ytdict