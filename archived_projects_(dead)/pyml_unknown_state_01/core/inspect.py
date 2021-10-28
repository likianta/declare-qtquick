from lk_utils.read_and_write import load_list


class Inspect:
    
    def __init__(self):
        self._source_dict = {}
        self._source = None
    
    def chfile(self, file):
        # from lk_logger import lk
        # lk.loga(file)
        if file not in self._source_dict:
            self._source_dict[file] = load_list(file)
        self._source = self._source_dict[file]
    
    def get_line(self, lineno) -> str:
        return self._source[lineno - 1]


inspect = Inspect()
