import pytest
import sys

sys.path.append("../src")

from utils import stringUtil

def test_isArabic():
    assert stringUtil.isArabic('مرحبا') is not None
    assert stringUtil.isArabic('hello') is None

def test_reverseWordWiseForArabic():
    assert stringUtil.reverseWordWiseForArabic('hello world') == 'world hello'
    assert stringUtil.reverseWordWiseForArabic('123 456') == '456 123'

def test_replace_substring():
    assert stringUtil.replace_substring('hello world', 0, 5, 'goodbye') == 'goodbye world'
    assert stringUtil.replace_substring('123 456', 4, 7, '789') == '123 789'

def test_fixOrder():
    assert stringUtil.fixOrder('hello world', 'hello', 5) == 'hello world'
    assert stringUtil.fixOrder('123 456', '123', 3) == '123 456'

def test_fixArabic():
    assert stringUtil.fixArabic('hello world') == 'hello world'
    assert stringUtil.fixArabic('123 456') == '123 456'
    assert stringUtil.fixArabic('محل 1-11 - ملك مؤسسة دبي العقارية - الطي 13-23') == 'محل 11-1 - ملك مؤسسة دبي العقارية - الطي 23-13'
    assert stringUtil.fixArabic("محل 1-31-10 - ملك مؤسسة دبي العقارية - الطي") == "محل 10-31-1 - ملك مؤسسة دبي العقارية - الطي"
    assert stringUtil.fixArabic("مكتب رقم 43 - 44 ملك بلدية دبي - بردبي - الفهيدي .") == "مكتب رقم 44 - 43 ملك بلدية دبي - بردبي - الفهيدي ."
    assert stringUtil.fixArabic('محل 11,1 - ملك مؤسسة دبي العقارية - الطي 23,13') == 'محل 11,1 - ملك مؤسسة دبي العقارية - الطي 23,13'
