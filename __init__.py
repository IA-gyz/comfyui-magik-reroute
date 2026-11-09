"""Magik Reroute: an unrestricted, single-value passthrough for ComfyUI."""


class AnyType(str):
    """Allow ComfyUI's legacy type comparison to accept any socket type."""

    def __ne__(self, other):
        return False


ANY = AnyType("*")


class MagikReroute:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"value": (ANY, {"forceInput": True})}}

    RETURN_TYPES = (ANY,)
    RETURN_NAMES = ("value",)
    FUNCTION = "passthrough"
    CATEGORY = "Magik/Utils"
    DESCRIPTION = "Passes any connected value through unchanged."

    @classmethod
    def VALIDATE_INPUTS(cls, input_types):
        # This node deliberately accepts every incoming socket type.
        return True

    def passthrough(self, value):
        return (value,)


NODE_CLASS_MAPPINGS = {"MagikReroute": MagikReroute}
NODE_DISPLAY_NAME_MAPPINGS = {"MagikReroute": "Magik Reroute"}
