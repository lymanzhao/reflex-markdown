import reflex as rx

config = rx.Config(
    app_name="static_test",
    frontend_packages=[
        "react-markdown@^8.0.7", 
        "remark-gfm@^3.0.1"
    ],
    # Point to the static_test package module
    app_module="dynamic_test.dynamic_test"
)
