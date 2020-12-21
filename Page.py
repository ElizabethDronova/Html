from queue import LifoQueue
import os

way = "c:\\Users\\user\Desktop\Html"
class Html():
    def __init__(self, code):
        self.code = code
        self.tags = ""
        self.pars()
    def pars(self):
        for i in range(len(self.code)):
            if self.code[i] == "[":
                i = i+1
                if self.code[i: len("head") + i] == "head":
                    self.tags += "<head>"
                elif self.code[i: len("body") + i] == "body":
                    self.tags += "<body>"
                elif self.code[i: len("p") + i] == "p":
                    self.tags += "<p>"
                elif self.code[i: len("div") + i] == "div":
                    self.tags += "<div>"
                elif self.code[i: len("h3") + i] == "h3":
                    self.tags += "<h3>"
                elif self.code[i: len("h2") + i] == "h2":
                    self.tags += "<h2>"
                elif self.code[i: len("h1") + i] == "h1":
                    self.tags += "<h1>"
                elif self.code[i: len("footer") + i] == "footer":
                    self.tags += "<footer>"
                elif self.code[i: len("ul") + i] == "ul":
                    self.tags += "<ul>"
            if self.code[i] == "(":
                i = i + 1
                if self.code[i: len("title") + i] == "title":
                    self.tags += "<title>"
            if self.code[i] == "]":
                i = i + 1
    def generate(self, path = way):
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
            fileHtml = open(path + '\index.html', 'w', encoding='utf-8')
            fileHtml.write(self.tags)
            fileHtml.close()

        print(self.code)
        print(self.tags)


page = Html("[head(title='Заголовок')], [body [p('Параграф')] "
             "[div[h1('h1')][h2('h2')][h3('h3')]]"
             "[footer[ul('Cat', 'Dog')]]]")
page.generate()


