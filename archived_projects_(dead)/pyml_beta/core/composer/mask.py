"""
@Author   : likianta (likianta@foxmail.com)
@FileName : mask.py
@Version  : 0.2.3
@Created  : 2020-11-02
@Updated  : 2020-11-06
@Desc     : 
"""
import re
from contextlib import contextmanager

from lk_logger import lk

from pyml_rc.declare_pyml.core._typing_hints import MaskHint as Hint


class Mask:
    
    def __init__(self, pyml_text: str):
        self._keyx = 0  # keyx: mask holder key index
        self._mask = {}  # type: Hint.MaskHolder
        
        self._conflicts = re.compile(
            r'{mask_holder_\d+}|{mask_holder_conflict}'
        ).findall(pyml_text)
        if self._conflicts:
            lk.loga('Found {} conflicts'.format(len(self._conflicts)))
        
        self._holder_pattern = re.compile(r'{mask_holder_\d+}')
        self._text = self._holder_pattern.sub(
            '{mask_holder_conflict}', pyml_text
        )
    
    @contextmanager
    def temp_mask(self, pattern: Hint.RegexPattern, restore=''):
        """
        NOTE: 您需要保证 pattern 的形式足够简单, 它应该只匹配到 "一个" 特定的字
            符串, 例如:
                # wrong
                pattern = re.compile(r'\d\d')
                pattern = re.compile(r'\w+')
                ...

                # right (仅使用准确的描述, 可以加上前瞻, 后顾的条件)
                pattern = re.compile(r'11')
                pattern = re.compile(r'(?<=0x)001A')
                pattern = re.compile(r'32(?!\w)')
                ...
            restore 一般来说和 pattern 要匹配的目标字符串是一致的. 比如
            `pattern = re.compile(r'11')` 对应的 restore 就是 '11',
            `pattern = re.compile(r'(?<=0x)001A')` 对应的 restore 是 '001A'.

        :param pattern:
        :param restore:
        :return:
        """
        restore = restore or pattern.pattern
        try:
            holder = self._create_mask_holder(restore)
            self._text = pattern.sub(holder, self._text)
            yield self
        finally:
            # noinspection PyUnboundLocalVariable
            restore_pattern = re.compile(r'(?<!{)' + holder + r'(?!})')
            self._text = restore_pattern.sub(restore, self._text)
    
    def main(self, pattern: Hint.RegexPattern, cmd=''):
        """
        E.g.
            self._text = '\'He didn\\\'t tell you,\' she says, "and me, too."'
                          |        ^--^            |           ^------------^
                          ^------------------------^
            -> self._mask = {
                'mask1': '\'He didn\\\'t tell you,\'',
                          |        ^--^            |
                          ^------------------------^
                'mask2': '"and me, too."',
                          ^------------^
            }
            -> self._text = '{mask1} she says, {mask2}'

            So we can use `self._text.format(**self._mask)` to restore the
            origin text in the future (see `self.plain_text()`).

        :param pattern:
        :param cmd: <str 'strip_linebreaks', 'abandon', 'recurse'>
            strip_linebreaks: replace '\n' to ' '
            abandon: repalce matched string to ' '
            circle: 针对这种情况:
                    (A, (B), (C), D)
                    |   ^-^  ^-^   |
                    ^--------------^
                我们希望捕获到三个, 但只通过一次正则表达式似乎没法做到 (目前能想
                到的写法最多匹配到两个).
                所以增加一个此命令, 用于循环检测是否全部匹配到.
            circle+strip_linebreaks: 复合指令, 见上述描述
            
        :return:
        """
        
        def _generator1():
            text = self._text
            for match in pattern.finditer(text):
                yield match
        
        def _generator2():
            while match := pattern.search(self._text):
                yield match
        
        if cmd != 'circle' and cmd != 'circle+strip_linebreaks':
            gen = _generator1
        else:
            gen = _generator2
        
        # ----------------------------------------------------------------------
        
        for match in gen():
            match_str = match.group(0)
            
            if cmd == '' or \
                    cmd == 'circle' or \
                    cmd == 'circle+strip_linebreaks':
                mask_to = match_str
            elif cmd == 'abandon':
                mask_to = ''
            elif cmd == 'strip_linebreaks':
                mask_to = match_str.replace('\n', ' ')
            else:
                raise Exception('Unknown command', cmd, match_str)
            
            holder = self._create_mask_holder(mask_to)
            self._text = self._text.replace(match_str, holder, 1)
            """ FIXME: 隐患
                假如有:
                    text = 'ABCDD'
                    pattern = re.compile(r'(?<=D)D')
                那么正则表达式匹配的是后一个 'D', 但是我们使用 `replace()` 方法
                来替换:
                    text = text.replace('D', '{mask1}', 1)
                就会导致前一个 'D' 被替换成 'mask1'!

                后续我会使用 `self._safely_replace()` (目前还不稳定) 替换
                `replace()` 方法.
            """
            #   # noinspection PyTypeChecker
            #   self._safely_replace(*match.span(0), holder)
    
    def _safely_replace(self, start: int, end: int, mask_holder: str):
        """ 安全地替换目标片段为 mask_holder.

        FIXME: 此方法未被调用过, 且未通过用例测试 (需要检视和修复).

        E.g.
            from: 'a = "x, y"'
                  |    ^----^|
                  ^----------^
            to: 'a = {mask1}'
                |    ^-----^|
                ^-----------^
            #   self._mask = {'mask1': '"x, y"'}
        E.g.
            from: 'a = "\'\'\'x, \'y\\\'\'\'\'"'
                  |    ||        ^-----^     |||
                  |    |^1-2-3-----------4-5-6||
                  |    ^----------------------^|
                  ^----------------------------^
            to: 'a = "{mask1}"'
                |    |^-----^||
                |    ^-------^|
                ^-------------^
            #   self._mask = {'mask1': '\'\'\'x, \'y\\\'\'\'\''}
                                       ||        ^-----^     ||
                                       |^--------------------^|
                                       ^----------------------^
        """
        self._text = '{0}{{{1}}}{2}'.format(
            self._text[:start], mask_holder, self._text[end:]
        )
    
    def _create_mask_holder(self, s: str):
        self._keyx += 1
        key, val = f'mask_holder_{self._keyx}', s
        self._mask[key] = val
        return '{' + key + '}'
    
    @property
    def masked_text(self):
        return self._text
    
    @property
    def plain_text(self):
        """
        E.g.
            # origin_text = 'a = "x and y" \\ \n    "and z"'
            self._text = 'a = {mask2}'
            self._mask = {
                'mask1': '\\ \n',
                'mask2': '"x and y" {mask1}    "and z"',
            }
            ->
                result = 'a = "x and y" \\ \n    "and z"'
                # assert result == origin_text
        """
        pattern = self._holder_pattern
        text = self._text
        _error_stack = []
        
        while pattern.search(text):
            _error_stack.append('---------------- ERROR STACK ----------------')
            _error_stack.append(text)
            
            try:
                for holder in set(pattern.findall(text)):
                    text = text.replace(
                        holder, self._mask[holder[1:-1]]
                        #   `holder[1:-1]` means `holder.strip("{}")`
                    )
            except Exception as e:
                from lk_utils import read_and_write
                read_and_write.dumps(
                    _error_stack, f1 := './pyml_composer_error.txt'
                )
                read_and_write.dumps(
                    self._mask, f2 := './pyml_composer_error.json'
                )
                raise Exception(
                    e, f'Plese check dumped info from [{f1}] and [{f2}] for '
                       f'more infomation.'
                )
        
        else:
            if text == self._text:
                lk.loga('No mask node found')
        
        for holder in self._conflicts:
            text = text.replace('{mask_holder_conflict}', holder, 1)
        
        del _error_stack
        return text
