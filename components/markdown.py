import reflex as rx

def Markdown(content: str, **props) -> rx.Component:
    """Create a markdown component using marked.js with Radix Themes styling."""
    import json
    escaped_content = json.dumps(content)
    container_id = f"markdown-{hash(content)}"
    
    # CSS styles as a separate string
    css_styles = f"""
    #{container_id} thinking {{
        display: block;
        opacity: 0.7;
        padding: 0.5rem;
        margin: 0.5rem 0;
        border-radius: var(--radius-2);
        background-color: var(--accent-a3);
    }}
    #{container_id} pre {{
        opacity: 0.85;
        background-color: var(--accent-a2);
        padding: 0.75rem;
        border-radius: var(--radius-2);
        overflow-x: auto;
    }}
    #{container_id} ul {{
        list-style-type: disc;
        padding-left: 2em;
    }}
    #{container_id} code {{
        background-color: transparent;
        padding: 0.2rem 0.4rem;
        border-radius: var(--radius-1);
    }}
    #{container_id} h1 {{
        font-size: 1.8rem;
    }}
    #{container_id} h2 {{
        font-size: 1.5rem;
    }}
    #{container_id} h3 {{
        font-size: 1.2rem;
    }}
    #{container_id} h4 {{
        font-size: 1rem;
    }}
    #{container_id} hr {{
        border: none;
        height: 1px;
        background-color: var(--accent-a5);
        margin: 1rem 0;
    }}
    #{container_id} p {{
        margin: 0.5rem 0;
        line-height: 1.5;
    }}
    #{container_id} table {{
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
    }}
    #{container_id} th, #{container_id} td {{
        border: 1px solid var(--accent-a5);
        padding: 0.5rem;
        text-align: left;
    }}
    #{container_id} th {{
        background-color: var(--accent-a2);
    }}
    """
    
    return rx.box(
        rx.script(f"""
        const renderMarkdown = async () => {{
            try {{
                // Load marked.js
                const {{ marked }} = await import('https://esm.sh/marked@12.0.0');
                
                // Create and append styles
                const style = document.createElement('style');
                style.textContent = `{css_styles}`;
                document.head.appendChild(style);
                
                // Render markdown
                const container = document.getElementById('{container_id}');
                if (container) {{
                    container.innerHTML = marked.parse({escaped_content});
                }}
            }} catch (error) {{
                console.error('Markdown rendering error:', error);
            }}
        }};
        renderMarkdown();
        """),
        rx.box(
            id=container_id,
            opacity=0.95,
            padding="1rem",
            border_radius="0.5rem",
            **props
        ),
        width="100%"
    )
