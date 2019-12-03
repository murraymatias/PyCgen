class FileIO:
    @staticmethod
    def SaveText(path,file,stream):
        try:
            output_file = open(path+file,'w')
            output_file.write(stream)
        finally:
            output_file.close()


