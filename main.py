import requests

""" Special thank to @Zigoo0 - http://www.Sec-Down.com/ """

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; rv:30.0) Gecko/20100101 Firefox/33.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
}


class URLHandler:

    def __init__(self, url):
        self.url = url
        self.file_name = self.url.split('/')[-1]  # Getting the file name from the url
        self.file_ext = self.file_name.split('.')[1]  # This parameter contains the file extension only.
        self.file_noext = self.file_name.split('.')[0]  # This parameter contains the file name without extension

    def is_reachable(self) -> bool:
        '''
        Test the connection between local machine and dest url by sending a request to the url
        :param url: str "http://www.google.com/"
        :return: boolean
        '''
        try:
            r = requests.get(self.url)
            if r.status_code == 200:
                return True
        except:
            pass
        return False

    def generate_filenames(self):
        """ This function will handle the file extension manipulation """
        """ Like adding .tar, .zip etc to the file name """
        # Below is a list of extensions to be used for the filename brute-forcing.
        files = [self.file_name, "%s.tar" % (self.file_noext), "%s.rar" % (self.file_noext),
                 "%s.zip" % (self.file_noext),
                 "%s.txt" % (self.file_noext)]
        files += ["%s.old" % (self.file_name), "%s~" % (self.file_name), "%s.bak" % (self.file_name),
                  "%s.tar.gz" % (self.file_noext)]
        files += ["%s-backup.%s" % (self.file_noext, self.file_ext), "%s-bkp.%s" % (self.file_noext, self.file_ext),
                  "backup-%s.%s" % (self.file_noext, self.file_ext)]
        files += [".%s.%s.swp" % (self.file_noext, self.file_ext), "%s.%s" % (self.file_noext, self.file_ext) + "s",
                  "_%s.%s" % (self.file_noext, self.file_ext)]
        files += ["%s2.%s" % (self.file_noext, self.file_ext), "%s.%s_" % (self.file_noext, self.file_ext),
                  "%s.%s.gz" % (self.file_noext, self.file_ext)]
        files += ["%s_old.%s" % (self.file_noext, self.file_ext)]
        return files  # returning the list of created files.


class Files_Hunter:

    def __init__(self, url, headers):
        count = 0
        self.files = list()
        link_main = url.split('/')[-1]  # will replace the file name with the new list of file names.
        files = URLHandler(url).generate_filenames()
        for filename in files:
            try:
                count += 1
                new_url = url.replace(link_main, filename)  # This will replace the filename in the original url
                print("  [*] Testing %s" % new_url, end="")
                request = requests.get(new_url, headers=headers, verify=False, timeout=3)
                if request:
                    self.files.append(new_url)
                print(" ... ", request.status_code)

            except Exception as e:
                # print e
                print(e)

                continue
        self.print_result()

    def print_result(self):
        print("--------------result-------------------")
        for url in self.files:
            print("  [*] Seems I Hunted below url: %s" % url)


if __name__ == '__main__':
    print("""Special thank to @Zigoo0 - http://www.Sec-Down.com/""")
    print("Welcome to backup file sniffer!!!")
    print("Author: Rui; \nGitHub: https://github.com/lrlrlrlr")

    url = input("Please input the URL:  ").strip()
    # url = "http://challenge01.root-me.org/web-serveur/ch11/index.php"
    urlhandler = URLHandler(url)
    if not urlhandler.is_reachable():
        f"Not able to connect to the url:{url}, please have a check of the url and your connection."
        exit()
    Files_Hunter(url, headers)
