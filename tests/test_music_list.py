from lib.music_list import *
import pytest

def test_music_list_add() :
    music_list = Music_list()
    music_list.add('an artist', 'a track')
    assert music_list.listened_to == ['an artist: a track']

def test_music_list_empty_string() :
    with pytest.raises(Exception) as e:
        music_list = Music_list()
        music_list.add('', '')
    assert str(e.value) == 'No text given'

def test_music_list_add_twice() :
    music_list = Music_list()
    music_list.add('an artist', 'a track')
    music_list.add('second artist', 'second track')
    assert music_list.list() == ['an artist: a track','second artist: second track']

def test_music_list_non_string() :
    with pytest.raises(Exception) as e :
        music_list = Music_list()
        music_list.add(123, 123)
    assert str(e.value) == 'Not text format'

def test_music_list_list_empty() :
    with pytest.raises(Exception) as e:
        music_list = Music_list()
        music_list.list() 
    assert str(e.value) == 'List empty!'
    





