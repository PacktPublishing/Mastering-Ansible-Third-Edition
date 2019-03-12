from ansible.plugins.callback import default
class CallbackModule(default.CallbackModule):
  CALLBACK_VERSION = 2.0
  CALLBACK_TYPE = 'stdout'
  CALLBACK_NAME = 'shrug'
  def v2_on_any(self, *args, **kwargs):
    msg = '\xc2\xaf\\_(\xe3\x83\x84)_/\xc2\xaf'
    self._display.display(msg.decode('utf-8') * 8)

