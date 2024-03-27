from . import classes


# THIS FILE IS RESPONSABLE FOR THE CONSTRUCTION OF MANY OBJECTS



def get_available_markets(data):
    """Returns available markets from data or None if not present."""
    return data.get('available_markets')


def base_arguments(data):
    """Returns base arguments for all classes."""
    arguments = {
        'data': data,
        'type': data.get('type'),
        'name': data.get('name'),
        'url': data.get('external_urls', {}).get('spotify'),
        'id': data.get('id')
    }
    return arguments


def track_base_arguments(data):
    """Returns base arguments for track-like classes."""
    arguments = {
        'explicit': data.get('explicit'),
        'duration_ms': data.get('duration_ms')
    }
    return arguments


def artist(data):
    """Returns an Artist object."""
    return classes.Artist(**base_arguments(data))


def track(data):
    """Returns a Track object."""
    base = base_arguments(data)
    track_base = track_base_arguments(data)

    arguments = {
        'preview': data.get('preview_url'),
        'artists': [artist(artist_data) for artist_data in data.get('artists', [])],
        'album': album(data.get('album')),
        'available_markets': get_available_markets(data),
        'disc_number': data.get('disc_number'),
        'popularity': data.get('popularity')
    }
    return classes.Track(**{**base, **track_base, **arguments})


def album(data):
    """Returns an Album object."""
    base = base_arguments(data)

    arguments = {
        'images': [classes.AlbumCover(image.get('width'), image.get('height'), image.get('url')) for image in data.get('images', [])],
        'artists': [artist(artist_data) for artist_data in data.get('artists', [])],
        'available_markets': get_available_markets(data),
        'release_date': data.get('release_date'),
        'total_tracks': data.get('total_tracks')
    }
    return classes.Album(**{**base, **arguments})


def episode(data):
    """Returns an Episode object."""
    base = base_arguments(data)
    track_base = track_base_arguments(data)

    arguments = {
        'preview': data.get('audio_preview_url'),
        'description': data.get('description'),
        'html_description': data.get('html_description'),
        'images': data.get('images'),
        'language': data.get('language'),
        'languages': data.get('languages'),
        'release_date': data.get('release_date')
    }
    return classes.Episode(**{**base, **track_base, **arguments})
