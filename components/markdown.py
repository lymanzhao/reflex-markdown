import reflex as rx

def markdown(content: str, **props) -> rx.Component:
    """Create a markdown component using react-markdown.
    
    Args:
        content: The markdown content to render
        **props: Additional props to pass to the component
        
    Returns:
        A reflex component rendering the markdown
    """
    import json
    escaped_content = json.dumps(content)
    
    return rx.box(
        rx.script(f"""
        window.MarkdownComponent = (props) => {{
            return React.createElement(
                ReactMarkdown,
                {{
                    children: props.content,
                    remarkPlugins: [remarkGfm]
                }}
            );
        }}
        """),
        rx.box(
            __props__={
                "as": "MarkdownComponent", 
                "content": escaped_content,
                **props
            }
        ),
        width="100%"
    )
