import reflex as rx

def SimpleMarkdown(content: str = "", **props) -> rx.Component:
    """
    Simple markdown component that works with both static content and state variables.
    Uses marked.js with proper Reflex integration.
    """
    
    # Generate unique container ID based on content hash or use dynamic for state vars
    if isinstance(content, str):
        container_id = f"markdown-{abs(hash(content))}"
    else:
        # For state variables, use a fixed ID
        container_id = "markdown-dynamic"
    
    # CSS styles
    css_styles = """
    .markdown-container {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
        color: #1a1a1a;
    }
    .markdown-container .loading {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
        color: #666;
        font-style: italic;
    }
    .markdown-container .error {
        padding: 1rem;
        background-color: #ffe6e6;
        border: 1px solid #ff9999;
        border-radius: 4px;
        color: #cc0000;
    }
    .markdown-container h1 {
        font-size: 2rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 0.5rem;
    }
    .markdown-container h2 {
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1.25rem 0 0.75rem 0;
    }
    .markdown-container h3 {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 1rem 0 0.5rem 0;
    }
    .markdown-container h4 {
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0.75rem 0 0.5rem 0;
    }
    .markdown-container p {
        margin: 0.75rem 0;
        line-height: 1.7;
    }
    .markdown-container ul, .markdown-container ol {
        margin: 0.75rem 0;
        padding-left: 2rem;
    }
    .markdown-container li {
        margin: 0.25rem 0;
    }
    .markdown-container pre {
        background-color: #f5f5f5;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        padding: 1rem;
        overflow-x: auto;
        margin: 1rem 0;
    }
    .markdown-container code {
        background-color: #f5f5f5;
        padding: 0.2rem 0.4rem;
        border-radius: 2px;
        font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
        font-size: 0.9em;
    }
    .markdown-container pre code {
        background-color: transparent;
        padding: 0;
    }
    .markdown-container blockquote {
        border-left: 4px solid #0066cc;
        margin: 1rem 0;
        padding: 0.5rem 1rem;
        background-color: #f0f8ff;
    }
    .markdown-container table {
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
    }
    .markdown-container th, .markdown-container td {
        border: 1px solid #e0e0e0;
        padding: 0.5rem;
        text-align: left;
    }
    .markdown-container th {
        background-color: #f5f5f5;
        font-weight: 600;
    }
    .markdown-container hr {
        border: none;
        height: 1px;
        background-color: #e0e0e0;
        margin: 2rem 0;
    }
    .markdown-container a {
        color: #0066cc;
        text-decoration: none;
    }
    .markdown-container a:hover {
        text-decoration: underline;
    }
    .markdown-container thinking {
        display: block;
        background-color: #fff8e1;
        border: 1px solid #ffcc02;
        border-radius: 4px;
        padding: 0.75rem;
        margin: 1rem 0;
        font-style: italic;
        opacity: 0.8;
    }
    """
    
    # Add global CSS if not already added
    css_script = f"""
    if (!document.getElementById('markdown-global-styles')) {{
        const style = document.createElement('style');
        style.id = 'markdown-global-styles';
        style.textContent = `{css_styles}`;
        document.head.appendChild(style);
    }}
    """
    
    # Main rendering script
    render_script = f"""
    (async function() {{
        const container = document.getElementById('{container_id}');
        if (!container) return;
        
        // Show loading
        container.innerHTML = '<div class="loading">正在加载 Markdown...</div>';
        
        try {{
            // Load marked if not already loaded
            if (!window.marked) {{
                const markedModule = await import('https://esm.sh/marked@12.0.0');
                window.marked = markedModule.marked;
                
                // Configure marked
                window.marked.setOptions({{
                    breaks: true,
                    gfm: true,
                    sanitize: false
                }});
            }}
            
            // Get content - handle both static strings and dynamic content
            let markdownContent = '';
            if (typeof window.getMarkdownContent_{container_id.replace('-', '_')} === 'function') {{
                markdownContent = window.getMarkdownContent_{container_id.replace('-', '_')}();
            }} else {{
                markdownContent = `{content if isinstance(content, str) else ''}`;
            }}
            
            // Render
            if (markdownContent && markdownContent.trim()) {{
                container.innerHTML = window.marked.parse(markdownContent);
            }} else {{
                container.innerHTML = '<p style="color: #999; font-style: italic;">暂无内容</p>';
            }}
            
        }} catch (error) {{
            console.error('Markdown rendering error:', error);
            container.innerHTML = `<div class="error"><strong>渲染错误:</strong> ${{error.message}}</div>`;
        }}
    }})();
    """
    
    # For state variables, we need a different approach
    if not isinstance(content, str):
        # This is a state variable - use rx.script with proper state handling
        return rx.box(
            rx.script(css_script),
            rx.script(render_script),
            rx.box(
                id=container_id,
                class_name="markdown-container",
                **props
            ),
            width="100%"
        )
    else:
        # Static content
        return rx.box(
            rx.script(css_script),
            rx.script(render_script),
            rx.box(
                id=container_id,
                class_name="markdown-container",
                **props
            ),
            width="100%"
        )
