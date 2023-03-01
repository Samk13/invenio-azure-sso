"""Additional views."""

from flask import Blueprint

#
# Registration
#
def create_blueprint(app):
    """Register blueprint routes on app."""
    blueprint = Blueprint(
        "instance_test_2",
        __name__,
        template_folder="./templates",
    )

    # Add URL rules
    return blueprint
