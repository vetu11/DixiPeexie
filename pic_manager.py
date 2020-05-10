from json import load, dump
from os import listdir
from uuid import uuid4


class _PicManager:

    def __init__(self):
        with open("pic_info.json", "r") as f:
            self.pic_info = load(f)
        listed_pic_file_names = [pic["file_name"] for pic in self.pic_info.values()]

        pic_files = listdir("pics/")
        for file_name in pic_files:
            if file_name not in listed_pic_file_names:
                new_uuid = str(uuid4())
                self.pic_info.update({new_uuid:{"pic_id": new_uuid, "file_name": file_name, "file_id": None}})

        with open("pic_info.json", "w") as f:
            dump(self.pic_info, f)

    def get_pic(self, pic_id):
        pic = self.pic_info[pic_id]
        if pic["file_id"] is None:
            return open("pics/%s" % pic["file_name"], "rb")
        else:
            return pic["file_id"]

    def get_pic_id_list(self):
        return list(self.pic_info.keys())

    def update_pic_info(self, pic_id, new_file_id):
        self.pic_info[pic_id]["file_id"] = new_file_id
        with open("pic_info.json", "w") as f:
            dump(self.pic_info, f)


pic_manager = _PicManager()
