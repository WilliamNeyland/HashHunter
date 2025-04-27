import stat

class fileStruct():

    def __init__(self, filePath, fileStat):
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

    def __str__(self):
        return str(f'File={self.path},Mode={self.mode},Dev={self.dev},Nlinks={self.nlink},UID={self.uid},GID={self.gid},Size={self.size},Atime={self.atime},Ctime={self.ctime},Mtime={self.mtime}')
    