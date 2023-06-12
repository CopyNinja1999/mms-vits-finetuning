'''
Author: zhangzheyu zheyuzhang527@gmail.com
Date: 2023-06-06 15:10:30
LastEditors: zhangzheyu zheyuzhang527@gmail.com
LastEditTime: 2023-06-12 15:28:36
FilePath: /mms/efficient-vits-finetuning/text/__init__.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
""" from https://github.com/keithito/tacotron """
from text import cleaners
from text.symbols import TextMapper


# Mappings from symbol to numeric ID and vice versa:
_symbol_to_id = {}
_id_to_symbol = {}


def text_to_sequence(text, cleaner_names, vocab_path):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
      cleaner_names: names of the cleaner functions to run the text through
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = []
  text_mapper=TextMapper(vocab_path)
  _symbol_to_id=text_mapper._symbol_to_id
  _id_to_symbol=text_mapper._id_to_symbol
  text=text.lower()
  text=text_mapper.filter_oov(text)
  clean_text = _clean_text(text, cleaner_names)
  for symbol in clean_text:
    symbol_id = _symbol_to_id[symbol]
    sequence += [symbol_id]
  return sequence


def cleaned_text_to_sequence(cleaned_text):
  '''Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
  '''
  sequence = [_symbol_to_id[symbol] for symbol in cleaned_text]
  return sequence


def sequence_to_text(sequence):
  '''Converts a sequence of IDs back to a string'''
  result = ''
  for symbol_id in sequence:
    s = _id_to_symbol[symbol_id]
    result += s
  return result


def _clean_text(text, cleaner_names):
  for name in cleaner_names:
    cleaner = getattr(cleaners, name)
    if not cleaner:
      raise Exception('Unknown cleaner: %s' % name)
    text = cleaner(text)
  return text
