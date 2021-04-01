import arcade


class Director(arcade.Window):
    
    ON_DRAW = "ON_DRAW"
    ON_KEY_PRESS = "ON_KEY_PRESS"
    ON_KEY_RELEASE = "ON_KEY_RELEASE"
    ON_MOUSE_DRAG = "ON_MOUSE_DRAG"
    ON_MOUSE_MOTION = "ON_MOUSE_MOTION"
    ON_MOUSE_PRESS = "ON_MOUSE_PRESS"
    ON_MOUSE_RELEASE = "ON_MOUSE_RELEASE"
    ON_MOUSE_SCROLL = "ON_MOUSE_SCROLL"
    ON_UPDATE = "ON_UPDATE"

    def __init__(self, screen_width, screen_height):
        super().__init__(screen_width, screen_height)
        self._cast = None
        self._script = None

    def direct_scene(self, cast, script):
        self._cast = cast
        self._script = script
    
    def on_draw(self):
        arcade.start_render()
        self._cue_action(Director.ON_DRAW, None)
        
    def on_key_press(self, key, modifiers):
        args = { "key": key, "modifiers": modifiers }
        self._cue_action(Director.ON_KEY_PRESS, args)
            
    def on_key_release(self, key, modifiers):
        args = { "key": key, "modifiers": modifiers }
        self._cue_action(Director.ON_KEY_RELEASE, args)
        
    def on_mouse_drag(self, x, y, dx, dy, buttons, _):
        args = { "x": x, "y": y, "dx": dx, "dy": dy, "buttons": buttons }
        self._cue_action(Director.ON_MOUSE_DRAG, args)
        
    def on_mouse_motion(self, x, y, dx, dy):
        args = { "x": x, "y": y, "dx": dx, "dy": dy }
        self._cue_action(Director.ON_MOUSE_MOTION, args)
        
    def on_mouse_press(self, x, y, button, _):
        args = { "x": x, "y": y, "button": button }
        self._cue_action(Director.ON_MOUSE_PRESS, args)
        
    def on_mouse_release(self, x, y, button, _):
        args = { "x": x, "y": y, "button": button }
        self._cue_action(Director.ON_MOUSE_RELEASE, args)
        
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        args = { "x": x, "y": y, "scroll_x": scroll_x, "scroll_y": scroll_y }
        self._cue_action(Director.ON_MOUSE_SCROLL, args)
        
    def on_update(self, delta_time):
        args = { "delta_time": delta_time }
        self._cue_action(Director.ON_UPDATE, args)
        
    def _cue_action(self, cue, args):
        actions = self._script.get(cue, list())
        for action in actions:
            action.execute(self._cast, args, self)