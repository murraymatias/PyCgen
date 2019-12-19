class FileIO():

    @staticmethod
    def SaveText(filename,data):
        with open(filename,'w') as f:
            f.write(data)


