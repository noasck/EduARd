from wsgi import start_app  # noqa


def test_create_app():
    """App class Factory method."""
    assert start_app()
