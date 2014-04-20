# The Recursive Directory Sorter

# All attempts have been made to make this script safe across all platforms
# However, mistakes happen. You should ALWAYS back up your files before sorting them.
# I accept NO responsibility for lost files, whether or not you took a backup.
# This software is provided AS IS with no expressed or implied warranties
# Including merchantability or fitness for any particular purpose

def softexit(secs): #You can't read error messages if the screen instantly closes...
        print 'Script will die in ', secs, ' seconds...'
        sleep(secs)
        exit()

import os
import sys
import shutil
from time import sleep

def typeproc(curfile, typelist, typedir):
    for ft in typelist:
        if curfile.lower().endswith('.' + ft):
            #if not os.access(thedir + '/' + typedir + '/', os.F_OK):
            if not os.access(os.path.join(thedir, typedir, ''), os.F_OK):    
                os.mkdir(os.path.join(thedir, typedir))
            print 'Putting ' + curfile + ' in the ' + typedir + ' folder...'
            #shutil.move(thedir + curfile, thedir + '/' + typedir + '/' + curfile)
            print os.path.join(thedir, typedir, curfile)
            os.rename(curfile, os.path.join(thedir, typedir, os.path.split(curfile)[-1]))
            break
            

def reclist(dirc, totallist=[]):
        basedir = dirc
        subdirlist = []
        for item in os.listdir(dirc):
                if os.path.isfile(os.path.join(basedir,item)):
                        totallist.append(os.path.join(basedir,item))
                else:
                        subdirlist.append(os.path.join(basedir, item))
        for subdir in subdirlist:
                totallist = reclist(subdir, totallist) #Some people WILL have problems with recursivity if they have a big folder tree.
        return totallist

def processdirectory(directory):
        for item in reclist(directory):
                    typeproc(item, ['jpg','jpeg','bmp','gif','png','tiff', 'webp', 'xcf','psd'], 'Images')
                    typeproc(item, ['avi','mp4','flv', 'mov', 'wmv', 'aff', 'fla', 'm4v', 'mpeg', 'mpg', 'mpe', 'swf', 'webm', 'dvd'], 'Videos')
                    typeproc(item, ['doc', 'docx', 'txt', 'rtf', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'fodt', 'odp', 'fodp', 'ods', 'fods', 'odg', 'fodg', 'pub', 'pdf'], 'Documents')
                    typeproc(item, ['mp3', 'm4a', 'flac', 'wav', 'au', 'la', 'mp2', 'speex', 'wma', 'aac', 'm4p', 'mid', 'midi','aif'], 'Audio')
                    typeproc(item, ['tar.gz','tar','tgz','rar','tar.bz','tbz','zip','7z','bz2','deb','rpm','lzma','tar.xz','txz','iso'], 'Archives')
                    typeproc(item, ['torrent','magnet'], 'Torrents')
                    typeproc(item, ['mdb', 'sql', 'sqlite', 'accdb', 'sas'], 'Databases')
                    typeproc(item, ['temp', 'tmp'], 'Temporary Files')




# Begining!

try:
        thedir = sys.argv[1]
except:
        print 'You didn\'t include a directory. That\'s okay, I\'ll let you specify one now.'
        #if os.name == 'nt':
        #        print 'DEAR WINDOWS USER: You\'ll need to use two slashes between directories, like so...'
        #        print 'EXAMPLE: C:\\Users\\Files\\To\\Be\\Sorted'
        #        print 'If you don\'t, you\'ll get some strange errors from Windows and risk file loss!'
        thedir = raw_input('What directory should I recursively sort? ')




print 'Sorting'

processdirectory(thedir)

raw_input('All done! Press enter to exit.')
