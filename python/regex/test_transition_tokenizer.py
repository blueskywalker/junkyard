
from transition_tokenizer import expansion
import pytest

def test_basic():
    assert 'abc' == expansion('abc')

def test_one_stack():
    assert 'abcabc' == expansion('2[abc]')

def test_two_stacks():
    assert 'abcccdabcccd' == expansion('2[ab3[c]d]')

def test_two_stacks_suffix():
    assert 'abcabcdededefgabcdededefghij' == expansion('abc2[abc3[de]fg]hij')

def test_two_expansions():
    assert 'abcddfghiii' == expansion('abc2[d]fgh3[i]')

def test_complex():
    assert 'abciaaaazzzzziaaaazzzzziaaaazzzzziaaaazzzzziaaaazzzzzfffabyxzzziyxzzziabyxzzziyxzzziabyxzzziyxzzzi' == expansion('abc5[i2[aa]5[z]]fff3[ab2[yx3[z]i]]')