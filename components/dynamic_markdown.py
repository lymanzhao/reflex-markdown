import reflex as rx

def DynamicMarkdown(content, **props) -> rx.Component:
    """
    Dynamic markdown component that works with Reflex state variables.
    Uses a different approach to handle state updates.
    """
    
    # Generate unique container ID
    container_id = "dynamic-markdown-container"
    
    # CSS styles
    css_styles = """
    .dynamic-markdown {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
        color: #1a1a1a;
    }
    .dynamic-markdown .loading {
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
        color: #666;
        font-style: italic;
    }
    .dynamic-markdown .error {
        padding: 1rem;
        background-color: #ffe6e6;
        border: 1px solid #ff9999;
        border-radius: 4px;
        color: #cc0000;
    }
    .dynamic-markdown h1 {
        font-size: 2rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 0.5rem;
    }
    .dynamic-markdown h2 {
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1.25rem 0 0.75rem 0;
    }
    .dynamic-markdown h3 {
        font-size: 1.25rem;
        font-weight: 600;
        margin: 1rem 0 0.5rem 0;
    }
    .dynamic-markdown h4 {
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0.75rem 0 0.5rem 0;
    }
    .dynamic-markdown p {
        margin: 0.75rem 0;
        line-height: 1.7;
    }
    .dynamic-markdown ul, .dynamic-markdown ol {
        margin: 0.75rem 0;
        padding-left: 2rem;
    }
    .dynamic-markdown li {
        margin: 0.25rem 0;
    }
    .dynamic-markdown pre {
        background-color: #f5f5f5;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        padding: 1rem;
        overflow-x: auto;
        margin: 1rem 0;
    }
    .dynamic-markdown code {
        background-color: #f5f5f5;
        padding: 0.2rem 0.4rem;
        border-radius: 2px;
        font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
        font-size: 0.9em;
    }
    .dynamic-markdown pre code {
        background-color: transparent;
        padding: 0;
    }
    .dynamic-markdown blockquote {
        border-left: 4px solid #0066cc;
        margin: 1rem 0;
        padding: 0.5rem 1rem;
        background-color: #f0f8ff;
    }
    .dynamic-markdown table {
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
    }
    .dynamic-markdown th, .dynamic-markdown td {
        border: 1px solid #e0e0e0;
        padding: 0.5rem;
        text-align: left;
    }
    .dynamic-markdown th {
        background-color: #f5f5f5;
        font-weight: 600;
    }
    .dynamic-markdown hr {
        border: none;
        height: 1px;
        background-color: #e0e0e0;
        margin: 2rem 0;
    }
    .dynamic-markdown a {
        color: #0066cc;
        text-decoration: none;
    }
    .dynamic-markdown a:hover {
        text-decoration: underline;
    }
    .dynamic-markdown thinking {
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
    
    # JavaScript for rendering
    render_script = f"""
    // Add CSS if not already added
    if (!document.getElementById('dynamic-markdown-styles')) {{
        const style = document.createElement('style');
        style.id = 'dynamic-markdown-styles';
        style.textContent = `{css_styles}`;
        document.head.appendChild(style);
    }}
    
    // Function to render markdown
    async function renderDynamicMarkdown(content) {{
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
            
            // Render
            if (content && content.trim()) {{
                container.innerHTML = window.marked.parse(content);
            }} else {{
                container.innerHTML = '<p style="color: #999; font-style: italic;">暂无内容</p>';
            }}
            
        }} catch (error) {{
            console.error('Markdown rendering error:', error);
            container.innerHTML = `<div class="error"><strong>渲染错误:</strong> ${{error.message}}</div>`;
        }}
    }}
    
    // Make function globally available
    window.renderDynamicMarkdown = renderDynamicMarkdown;
    """
    
    return rx.fragment(
        rx.script(render_script),
        rx.box(
            id=container_id,
            class_name="dynamic-markdown",
            **props
        ),
        # Use rx.script with content to trigger rendering
        rx.script(f"window.renderDynamicMarkdown(`{content}`);")
    )
