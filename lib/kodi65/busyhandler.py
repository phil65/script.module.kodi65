import xbmc
from kodi65 import utils
import traceback
from functools import wraps


class BusyHandler(object):
    """
    Class to deal with busydialog handling
    """
    def __init__(self, *args, **kwargs):
        self.busy = 0

    def show_busy(self):
        """
        Increase busycounter and open busydialog if needed
        """
        if self.busy == 0:
            xbmc.executebuiltin("ActivateWindow(busydialog)")
        self.busy += 1

    def hide_busy(self):
        """
        Decrease busycounter and close busydialog if needed
        """
        self.busy = max(0, self.busy - 1)
        if self.busy == 0:
            xbmc.executebuiltin("Dialog.Close(busydialog)")


def set_busy(func):
    """
    Decorator to show busy dialog while function is running
    Only one of the decorated functions may run simultaniously
    """
    @wraps(func)
    def decorator(self, *args, **kwargs):
        busyhandler.show_busy()
        result = func(self, *args, **kwargs)
        try:
            result = func(self, *args, **kwargs)
        except Exception:
            result = None
            utils.log(traceback.format_exc())
            utils.notify("Error", "please contact add-on author")
        finally:
            busyhandler.hide_busy()
        return result

    return decorator

busyhandler = BusyHandler()
