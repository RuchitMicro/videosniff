from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from pytube import exceptions as e, YouTube
from django.core.validators import URLValidator

def validate_url(value):
    
    validate = URLValidator()
    try:
        validate(value)
        YouTube(value)
    except e.LiveStreamError:
        raise ValidationError(_('ARF ARF!!! The Requested video is been livestreamed.'))
    except e.RegexMatchError:
        raise ValidationError(_('ARF ARF!!! Bad URL'))
    except e.VideoUnavailable:
        raise ValidationError(_('ARF ARF!!! Video Unavailable'))
    except ValidationError:
        raise ValidationError(_('URL does not exists'))

    return value
    
