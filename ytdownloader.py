#!/usr/bin/env python3

from pytube import YouTube as yt
from time import sleep
from halo import Halo
import sys, pytube, os, halo, ffmpeg


def banner():
	print (""" _     _      _____                    _                 _             
| |   | |_   (____ \                  | |               | |            
| |___| | |_  _   \ \ ___  _ _ _ ____ | | ___   ____  _ | | ____  ____ 
 \_____/|  _)| |   | / _ \| | | |  _ \| |/ _ \ / _  |/ || |/ _  )/ ___)
   ___  | |__| |__/ / |_| | | | | | | | | |_| ( ( | ( (_| ( (/ /| |    
  (___)  \___)_____/ \___/ \____|_| |_|_|\___/ \_||_|\____|\____)_|    
                                                                       """)
	sleep(0.5)
	print ("Author		:Kr0nuzz")
	sleep(0.5)
	print ("Purpose		:YouTube Video Downloader")
	sleep(0.5)

def inti():
	link = input('Masukkan Link>> ')
	while(True):
		quality = input('Masukkan Kualitas Video>> ')
		if quality in ('144', '240', '360', '480', '720', '1080'):
			quality= quality+"p"
			break
		elif quality in ('144p', '240p', '360p', '480p', '720p', '1080p') :
			print (" ")
			break
		else:
			print("Salah Input")
	while(True):
		frame = int(input('Masukkan FPS>> '))
		if frame in (30, 60):
			break
		else:
			print(" Salah Input")
	spinner = Halo(text='Sedang Mengambil Data!', spinner='dots')
	spinner.start()
	if os.name == 'posix':
		lokasi = os.getcwd()+ '/'
	else:
		print ("maaf platform anda tidak support")
	suk = yt(link)
	spinner.stop()
	print ('\n'+'Berhasil Mengambil Data	:'+ suk.title)
	gug = Halo(text='Sedang Mendownload', text_color='red', spinner='line', animation='bounce')
	gug.start()
	kontol = suk.streams.filter(fps=frame, res=quality).first()
	if  kontol == None:
		print("Kualitas Yang Diinput Tidak Tersedia")
		exit()
	tuturuu = suk.title
	video = ('video.mp4')
	videom = ('video')
	suara = ('audio.mp4')
	suaram = ('audio')
	audio = suk.streams.filter(only_audio=True).first().download(filename=suaram)
	video = suk.streams.filter(fps=frame, res=quality).first().download(filename=videom)
	audio_stream = ffmpeg.input(suara)
	video_stream = ffmpeg.input(video)
	ffmpeg.output(audio_stream, video_stream, tuturuu+'.mp4').run()
	gug.stop()
	print ("Berhasil Mendownload!!")

if __name__=='__main__':
	os.system("clear")
	banner()
	inti()
