import reflex as rx

config = rx.Config(
    app_name="samply",
    frontend_packages=[
        "react-markdown@^8.0.7", 
        "remark-gfm@^3.0.1"
    ],
    # Point to the samply package module
    app_module="samply.samply"
)
