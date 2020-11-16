from pywinauto.application import Application as WinApplication
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, cfg_target):
        self.application = WinApplication(backend="win32").start(cfg_target)
        self.main_window = self.application.window(title="Free Address Book")
        # Wait until the window is visible (opened)
        self.main_window.wait("visible")
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def destroy(self):
        self.main_window.close()