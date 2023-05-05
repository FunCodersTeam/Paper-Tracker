import json
from os import environ
from wxpusher import WxPusher

class Tracker:
    def __init__(self, path: str = "config.json") -> None:
        self.__path = path
        with open(self.__path, 'r', encoding = 'utf-8') as f:
            self.config = json.load(f)
        self.__fetch().__analyze().__update()

    def __fetch(self):
        from arxiv import Search, SortCriterion
        self.__new = dict()
        for k, v in self.config["keywords"].items():
            temp = list()
            res = Search(
                query = v,
                max_results = self.config["max_results"],
                sort_by = SortCriterion.SubmittedDate
            )

            for r in res.results():
                temp.append({
                    "id": r.get_short_id()[:-2],
                    "title": r.title,
                    "url": r.entry_id[:-2].replace('/abs/', '/pdf/') + '.pdf',
                    "time": r.updated.date().strftime("%Y-%m-%d"),
                    "context": [r.summary.replace("\n"," "), ]
                })
            self.__new[k] = temp
        return self

    def __analyze(self):
        cache = self.config["cache"]

        for i in self.__new:
            if i in cache:
                temp = list()
                for j in self.__new[i]:
                    if j['id'] == cache[i]:
                        break
                    else:
                        temp.append(j)
                self.__new[i] = temp

            if self.__new[i]:
                cache[i] = self.__new[i][0]["id"]

        def ChatGPT():
            import time
            from re import search
            from poe import Client
            from random import randrange
            bot = Client(environ["TOKEN"])
            for _ in bot.send_message("capybara", self.config["prompt"], with_chat_break = True):
                pass
            for i in self.__new:
                for j in self.__new[i]:
                    for chunk in bot.send_message("capybara", j["context"][0]):
                        pass
                    
                    j["context"] = [search(r"'en':\s*'(.+?)',", chunk["text"]).group(1), \
                                    search(r"'zh':\s*'(.+?)',", chunk["text"]).group(1)]

                    timer = randrange(100, 120)
                    time.sleep(timer)
        
        if all(value == [] for value in self.__new.values()):
            return self

        ChatGPT()

        with open(self.__path, 'w', encoding = self.config["encoding"]) as f:
            json.dump(self.config, f)

        return self

    def __update(self):
        import shutil
        import tempfile
        from datetime import datetime, timezone, timedelta

        def update(file, zh = False) -> None:
            with open(file, "r", encoding = self.config["encoding"]) as file:
                with tempfile.NamedTemporaryFile(mode = "w+", encoding = self.config["encoding"], delete = False) as temp_file:
                    i, keys, key, msgs = 0, list(self.__new.keys()), 0, ""

                    for line in file:
                        if i == 20:
                            temp_file.write(("> ### `更新时间：" if zh else "> ### `Update(BJT)：") + now + "`\n")
                        elif line == "|:-:|:-:|:-:|\n":
                            temp_file.write(line)
                            if key >= len(keys): continue

                            if self.__new[keys[key]] and zh: 
                                msgs += f'## **{keys[key]}**\r\n| 发布时间 | 标题 | 总结 |\r\n|:-:|:-:|:-:|\r\n'

                            for p in self.__new[keys[key]]:
                                new_line = "|{}|[{}]({})|{}|\n".format(p["time"], p["title"], p["url"], \
                                                                       p["context"][1] if zh else p["context"][0])
                                temp_file.write(new_line)
                                if zh:
                                    msgs += new_line
                            key += 1
                        else:
                            temp_file.write(line)
                        i += 1
                    temp_file.flush()
                    shutil.copy(temp_file.name, file.name)
            self.__wechat(msgs)

        tz = timezone(timedelta(hours = 8))
        now = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        update(self.config["en_md"])
        update(self.config["zh_md"], True)

    def __wechat(self, msg: str):
        if not msg: return
        msg = f"<center>\n\r{msg}</center>"
        WxPusher.send_message(msg, content_type = 3 ,topic_ids = ["9888"], token = environ["WX"], \
                              url = "https://github.com/FunCodersTeam/AI-Paper-Tracker")

    def __clean(self):
        pass

if __name__ == "__main__":
    Tracker()