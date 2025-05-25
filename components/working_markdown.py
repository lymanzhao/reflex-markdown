import reflex as rx

def WorkingMarkdown(content: str = "", **props) -> rx.Component:
    """
    Working markdown component that uses marked.js.
    This version avoids state variable complications.
    """
    import json
    
    # Escape content for JavaScript
    escaped_content = json.dumps(content)
    
    # Generate unique container ID
    container_id = f"markdown-{abs(hash(content))}"
    
    # JavaScript code for rendering
    js_code = f"""
    (async function() {{
        const container = document.getElementById('{container_id}');
        if (!container) return;
        
        // Add CSS if not already added
        if (!document.getElementById('markdown-styles')) {{
            const style = document.createElement('style');
            style.id = 'markdown-styles';
            style.textContent = `
                .markdown-content {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
                    line-height: 1.6;
                    color: #1a1a1a;
                }}
                .markdown-content h1 {{
                    font-size: 2rem;
                    font-weight: 700;
                    margin: 1.5rem 0 1rem 0;
                    border-bottom: 2px solid #e0e0e0;
                    padding-bottom: 0.5rem;
                }}
                .markdown-content h2 {{
                    font-size: 1.5rem;
                    font-weight: 600;
                    margin: 1.25rem 0 0.75rem 0;
                }}
                .markdown-content h3 {{
                    font-size: 1.25rem;
                    font-weight: 600;
                    margin: 1rem 0 0.5rem 0;
                }}
                .markdown-content p {{
                    margin: 0.75rem 0;
                    line-height: 1.7;
                }}
                .markdown-content ul, .markdown-content ol {{
                    margin: 0.75rem 0;
                    padding-left: 2rem;
                }}
                .markdown-content li {{
                    margin: 0.25rem 0;
                }}
                .markdown-content pre {{
                    background-color: #f5f5f5;
                    border: 1px solid #e0e0e0;
                    border-radius: 4px;
                    padding: 1rem;
                    overflow-x: auto;
                    margin: 1rem 0;
                }}
                .markdown-content code {{
                    background-color: #f5f5f5;
                    padding: 0.2rem 0.4rem;
                    border-radius: 2px;
                    font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
                    font-size: 0.9em;
                }}
                .markdown-content pre code {{
                    background-color: transparent;
                    padding: 0;
                }}
                .markdown-content blockquote {{
                    border-left: 4px solid #0066cc;
                    margin: 1rem 0;
                    padding: 0.5rem 1rem;
                    background-color: #f0f8ff;
                }}
                .markdown-content table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin: 1rem 0;
                }}
                .markdown-content th, .markdown-content td {{
                    border: 1px solid #e0e0e0;
                    padding: 0.5rem;
                    text-align: left;
                }}
                .markdown-content th {{
                    background-color: #f5f5f5;
                    font-weight: 600;
                }}
                .markdown-content hr {{
                    border: none;
                    height: 1px;
                    background-color: #e0e0e0;
                    margin: 2rem 0;
                }}
                .markdown-content a {{
                    color: #0066cc;
                    text-decoration: none;
                }}
                .markdown-content a:hover {{
                    text-decoration: underline;
                }}
                .markdown-content thinking {{
                    display: block;
                    background-color: #fff8e1;
                    border: 1px solid #ffcc02;
                    border-radius: 4px;
                    padding: 0.75rem;
                    margin: 1rem 0;
                    font-style: italic;
                    opacity: 0.8;
                }}
            `;
            document.head.appendChild(style);
        }}
        
        // Show loading
        container.innerHTML = '<div style="padding: 2rem; text-align: center; color: #666;">正在加载 Markdown...</div>';
        
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
            
            // Render markdown
            const content = {escaped_content};
            if (content && content.trim()) {{
                container.innerHTML = window.marked.parse(content);
            }} else {{
                container.innerHTML = '<p style="color: #999; font-style: italic;">暂无内容</p>';
            }}
            
        }} catch (error) {{
            console.error('Markdown rendering error:', error);
            container.innerHTML = `<div style="padding: 1rem; background-color: #ffe6e6; border: 1px solid #ff9999; border-radius: 4px; color: #cc0000;"><strong>渲染错误:</strong> ${{error.message}}</div>`;
        }}
    }})();
    """
    
    return rx.box(
        rx.script(js_code),
        rx.box(
            id=container_id,
            class_name="markdown-content",
            **props
        ),
        width="100%"
    )
