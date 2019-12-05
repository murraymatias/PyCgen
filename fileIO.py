class FileIO():

    @staticmethod
    def SaveText(path,filename,data):
        with open(path+filename,'w') as f:
            f.write(data)


