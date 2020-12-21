from queue import LifoQueue
import os

way = "c:\\Users\\user\Desktop\Html"
class Html():
    def __init__(self, code):
        self.code = code
        self.tags = ""
        self.closetag = LifoQueue()
        self.pars()
    def pars(self):
        for i in range(len(self.code)):
            if self.code[i] == "[":
                g = i + 1
                if self.code[g: len("head") + g] == "head":
                    self.tags += "<head>\r\n"
                    self.closetag.put("</head>\r\n")
                if self.code[g: len("body") + g] == "body":
                    self.tags += "<body>\r\n"
                    self.closetag.put("</body>\r\n")
                elif self.code[g: len("p") + g] == "p":
                    self.tags += "<p>\r\n"
                    self.closetag.put("</p>\r\n")
                elif self.code[g: len("div") + g] == "div":
                    self.tags += "<div>\r\n"
                    self.closetag.put("</div>\r\n")
                elif self.code[g: len("h3") + g] == "h3":
                    self.tags += "<h3>\r\n"
                    self.closetag.put("</h3>\r\n")
                elif self.code[g: len("h2") + g] == "h2":
                    self.tags += "<h2>\r\n"
                    self.closetag.put("</h2>\r\n")
                elif self.code[g: len("h1") + g] == "h1":
                    self.tags += "<h1>\r\n"
                    self.closetag.put("</h1>\r\n")
                elif self.code[g: len("footer") + g] == "footer":
                    self.tags += "<footer>\r\n"
                    self.closetag.put("</footer>\r\n")
                elif self.code[g: len("b") + g] == "b":
                    self.tags += "<b>\r\n"
                    self.closetag.put("</b>\r\n")
                elif self.code[g: len("title") + g] == "title":
                    self.tags += "<title>\r\n"
                    self.closetag.put("</title>\r\n")
            if self.code[i] == "]":
                self.tags += self.closetag.get()
            if self.code[i] == "(":
                end = self.code.find(")", i+1)
                self.tags += self.code[i+1:end] + "\r\n"

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


page = Html("[head[title(Заголовок)]], [body [p[b(Параграф)]] "
             "[div[h1(h1)][h2(h2)][h3(h3)]]"
             "[footer]]")
page.generate()


