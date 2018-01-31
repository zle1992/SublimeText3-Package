#-*- encoding: utf-8 -*-
'''
Created on 2018-01-12 19:20:44

@author: zhangle

@note: 
'''



import sublime, sublime_plugin, datetime

class insertSignatureCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        date = datetime.datetime.now()
        dateStr = date.strftime("%Y-%m-%d %X")
        text_encode = """#-*- encoding: utf-8 -*-\n'''\n"""
        text_author = """\n\n@author: zhangle"""
        text_note = """\n\n@note: \n'''\n"""
        text = text_encode + 'Created on ' + dateStr + text_author +text_note#-*- encoding: utf-8 -*-



        #for region in the selection
        #一个region是一个选择块，一次可以选择多个块
        for r in self.view.sel():
            str_r = self.view.substr(r)#str_r是所选择块的文本内容
            if 'Created on ' in str_r:
                if 'Updated on ' in str_r:
                    text = str_r[0:str_r.find('Updated on ')] + 'Updated on ' + dateStr + text_author
                else:
                    text = str_r.replace(text_author, '\nUpdated on ' + dateStr + text_author)
            self.view.erase(edit, r)
            self.view.insert(edit, r.begin(), text)