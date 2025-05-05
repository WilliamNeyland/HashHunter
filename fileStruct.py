import stat
import hashlib

class fileStruct():

    def __init__(self, filePath, fileStat):

        self.attributes = {}

        self.path = filePath
        self.mode = stat.filemode(fileStat.st_mode)
        self.dev = fileStat.st_dev
        self.nlink = fileStat.st_nlink
        self.uid = fileStat.st_uid
        self.gid = fileStat.st_gid
        self.size = fileStat.st_size
        self.atime = fileStat.st_atime
        self.ctime = fileStat.st_ctime
        self.mtime = fileStat.st_mtime

        with open(self.path, 'rb') as file:
            digest = hashlib.file_digest(file, 'sha256').hexdigest()
            self.digest = digest

        # Creates a dictionary of the files attributes
        for attribute in dir(self):
            if not attribute.startswith("__") or attribute.startswith("stat") or attribute.startswith("hashlib"):
                value = getattr(self, attribute)
                self.attributes.update({attribute : value})
        self.attributes.pop('attributes')

    def __str__(self):

        return str(f'File={self.path},Mode={self.mode},Dev={self.dev},Nlinks={self.nlink},UID={self.uid},GID={self.gid},Size={self.size},Atime={self.atime},Ctime={self.ctime},Mtime={self.mtime},Digest={self.digest}')


#st_mode == File mode: file type and file mode bits (permissions).
#st_ino ==
#st_dev == Identifier of the device on which this file resides.
#st_nlinks == Number of hard links.
#st_uid == User identifier of the file owner.
#st_gid == Group identifier of the file owner.
#st_size == Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.
#st_atime == Time of most recent access expressed in seconds.
#st_ctime == Time of most recent content modification expressed in seconds.
#st_mtime == Time of most recent metadata change expressed in seconds.