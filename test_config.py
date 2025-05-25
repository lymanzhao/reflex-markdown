import reflex as rx

config = rx.Config(
    app_name="markdown_test",
    frontend_packages=[
        "react-markdown@^8.0.7", 
        "remark-gfm@^3.0.1"
    ],
    # Point to the test app module
    app_module="test_app"
)
