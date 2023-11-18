import pytest
from television import Television

def test_initialization():
    tv = Television()
    assert tv.status is False
    assert tv.muted is False
    assert tv.volume == tv.MIN_VOLUME
    assert tv.channel == tv.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv.status is True

def test_mute_unmute():
    tv = Television()
    tv.volume_up()
    tv.mute()
    assert tv.muted is True
    assert tv.volume == tv.MIN_VOLUME

    tv.mute()
    assert tv.muted is False
    # Assuming the TV should revert to the previous volume upon unmuting
    assert tv.volume == tv.MIN_VOLUME + 1  # Adjust this assertion according to your logic

# Add more test functions for other methods following a similar pattern

# Run the tests if this script is executed directly
if __name__ == "__main__":
    pytest.main()