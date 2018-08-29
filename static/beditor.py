import ace

class editor():
    """ace brython editor"""
    def __init__(self, script):
        self.script = script
    
    def prog(self, ev):
        Ace = ace.Editor(editor_id="kw_editor", console_id="kw_console", container_id="kw__container", storage_id="kw_py_src" )
        Ace.editor.setValue(self.script)
        Ace.editor.scrollToRow(0)
        Ace.editor.gotoLine(0)