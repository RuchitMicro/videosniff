from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import redirect
from pytube import YouTube
from django.views.generic import TemplateView
from downloader.forms import HomeForm
from django.utils.encoding import smart_str
import os
import youtube_dl
from django.views.static import serve

class indexView(TemplateView):
        template_name = 'downloader/index.html'
        form = HomeForm()
        def get(self, request):
                return render(request,self.template_name, {'form':self.form})

        def post(self, request):
                form = HomeForm(request.POST)
                if form.is_valid() and 'video' in request.POST:
                        formUrl = form.cleaned_data['URL']
                        yt = YouTube(formUrl)
                        url = yt.streams.all()[0].url
                        title = 'title='+yt.title
                        url += '&'+title
                        response = HttpResponse()
                        response = redirect(url)
                        response['content_type'] = 'application/mp4'
                        response['User-Agent'] = 'None'
                        response['Content-Disposition'] = 'attachment/mp4'
                        return response
                elif form.is_valid() and 'audio' in request.POST:
                        formUrl = form.cleaned_data['URL']
                        '''
                        options = {
                                'format': 'bestaudio/best',
                                'extractaudio' : True,
                                'audioformat' : "mp3",
                                'outtmpl': '%(id)s.%(ext)s',
                                'noplaylist' : True,
                                'postprocessors': [{
                                        'key': 'FFmpegExtractAudio',
                                        'preferredcodec': 'mp3',
                                        'preferredquality': '192',
                                }],
                        }
                        with youtube_dl.YoutubeDL(options) as ydl:
                                audio = ydl.download([formUrl])
                        '''
                        file_name = 'o.mp4'
                        path = 'C:/Users/mr/VideoSniff/o.mp4'
                        response = HttpResponse()
                        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
                        response['X-Sendfile'] = smart_str(path)
#                       return serve(request, os.path.basename(path), os.path.dirname(path))
                        return response
                return render(request,self.template_name, {'form':form})
       

    #https://redirector.googlevideo.com/videoplayback?ei=YNuAXIPZDcjJgAepo6bgAQ&mt=1551948518&ratebypass=yes&requiressl=yes&lmt=1472094651656856&ip=136.243.71.29&fvip=4&ipbits=0&expire=1551970240&id=o-AHDnKnDTEBeci2Nax3fBHP1wuqmvNncaCMp-1kxKoZOw&mime=video%2Fmp4&mm=31%2C26&itag=22&c=WEB&mn=sn-4g5e6ney%2Csn-5hnekn7d&signature=C79222DED4D376F88E50CE5E56DD01843F09E4AC.76B2D0D644B4E1C552A20534E790BB7D080D5E6D&key=yt6&ms=au%2Conr&mv=m&initcwndbps=891250&source=youtube&sparams=dur%2Cei%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&pl=23&dur=122.949&title=A Swarm of One Thousand Robots
    #https://redirector.googlevideo.com/videoplayback?&requiressl=yes&ip=136.243.71.29&mv=m&source=youtube&ratebypass=yes&ms=au%2Conr&mn=sn-4g5e6ney%2Csn-5hnekn7d&mm=31%2C26&pl=23&id=o-AHDnKnDTEBeci2Nax3fBHP1wuqmvNncaCMp-1kxKoZOw&mime=video%2Fmp4&expire=1551970240&sparams=dur%2Cei%2Cid%2Cinitcwndbps%2Cip%2Cipbits%2Citag%2Clmt%2Cmime%2Cmm%2Cmn%2Cms%2Cmv%2Cpl%2Cratebypass%2Crequiressl%2Csource%2Cexpire&ipbits=0&lmt=1472094651656856&key=yt6&itag=22&fvip=4&signature=C79222DED4D376F88E50CE5E56DD01843F09E4AC.76B2D0D644B4E1C552A20534E790BB7D080D5E6D&dur=122.949&initcwndbps=891250&c=WEB&mt=1551948518&ei=YNuAXIPZDcjJgAepo6bgAQ&title=A Swarm of One Thousand Robots