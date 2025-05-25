import reflex as rx
from typing import Optional

class MarkdownState(rx.State):
    """State for markdown component"""
    content: str = ""
    is_loading: bool = False
    error_message: str = ""
    
    def set_content(self, content: str):
        """Set markdown content"""
        self.content = content
        self.is_loading = True
        self.error_message = ""
        
    def on_render_complete(self):
        """Called when markdown rendering is complete"""
        self.is_loading = False
        
    def on_render_error(self, error: str):
        """Called when markdown rendering fails"""
        self.is_loading = False
        self.error_message = error

def ImprovedMarkdown(content, **props) -> rx.Component:
    """
    Improved markdown component with better error handling and loading states.
    Uses marked.js with proper async handling.
    """
    import json
    
    # Handle both string content and Var content
    # For Reflex Vars, we need to handle them differently
    if hasattr(content, '_var_name'):
        # This is a Reflex Var (state variable)
        escaped_content = f"String({content._var_name})"
        container_id = f"markdown-dynamic"
    else:
        # This is a regular string
        escaped_content = json.dumps(content or "")
        container_id = f"markdown-{abs(hash(str(content)))}"
    
    # CSS styles
    css_styles = f"""
    #{container_id} {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        line-height: 1.6;
        color: var(--gray-12, #1a1a1a);
    }}
    #{container_id} .loading {{
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 2rem;
        color: var(--gray-11, #666);
    }}
    #{container_id} .error {{
        padding: 1rem;
        background-color: var(--red-3, #ffe6e6);
        border: 1px solid var(--red-6, #ff9999);
        border-radius: var(--radius-2, 4px);
        color: var(--red-11, #cc0000);
    }}
    #{container_id} h1 {{
        font-size: 2rem;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        border-bottom: 2px solid var(--gray-6, #e0e0e0);
        padding-bottom: 0.5rem;
    }}
    #{container_id} h2 {{
        font-size: 1.5rem;
        font-weight: 600;
        margin: 1.25rem 0 0.75rem 0;
    }}
    #{container_id} h3 {{
        font-size: 1.25rem;
        font-weight: 600;
        margin: 1rem 0 0.5rem 0;
    }}
    #{container_id} h4 {{
        font-size: 1.1rem;
        font-weight: 600;
        margin: 0.75rem 0 0.5rem 0;
    }}
    #{container_id} p {{
        margin: 0.75rem 0;
        line-height: 1.7;
    }}
    #{container_id} ul, #{container_id} ol {{
        margin: 0.75rem 0;
        padding-left: 2rem;
    }}
    #{container_id} li {{
        margin: 0.25rem 0;
    }}
    #{container_id} pre {{
        background-color: var(--gray-3, #f5f5f5);
        border: 1px solid var(--gray-6, #e0e0e0);
        border-radius: var(--radius-2, 4px);
        padding: 1rem;
        overflow-x: auto;
        margin: 1rem 0;
    }}
    #{container_id} code {{
        background-color: var(--gray-3, #f5f5f5);
        padding: 0.2rem 0.4rem;
        border-radius: var(--radius-1, 2px);
        font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
        font-size: 0.9em;
    }}
    #{container_id} pre code {{
        background-color: transparent;
        padding: 0;
    }}
    #{container_id} blockquote {{
        border-left: 4px solid var(--blue-6, #0066cc);
        margin: 1rem 0;
        padding: 0.5rem 1rem;
        background-color: var(--blue-2, #f0f8ff);
    }}
    #{container_id} table {{
        border-collapse: collapse;
        width: 100%;
        margin: 1rem 0;
    }}
    #{container_id} th, #{container_id} td {{
        border: 1px solid var(--gray-6, #e0e0e0);
        padding: 0.5rem;
        text-align: left;
    }}
    #{container_id} th {{
        background-color: var(--gray-3, #f5f5f5);
        font-weight: 600;
    }}
    #{container_id} hr {{
        border: none;
        height: 1px;
        background-color: var(--gray-6, #e0e0e0);
        margin: 2rem 0;
    }}
    #{container_id} a {{
        color: var(--blue-9, #0066cc);
        text-decoration: none;
    }}
    #{container_id} a:hover {{
        text-decoration: underline;
    }}
    #{container_id} thinking {{
        display: block;
        background-color: var(--yellow-3, #fff8e1);
        border: 1px solid var(--yellow-6, #ffcc02);
        border-radius: var(--radius-2, 4px);
        padding: 0.75rem;
        margin: 1rem 0;
        font-style: italic;
        opacity: 0.8;
    }}
    """
    
    # JavaScript for rendering
    js_code = f"""
    (async function() {{
        const containerId = '{container_id}';
        const container = document.getElementById(containerId);
        
        if (!container) {{
            console.error('Container not found:', containerId);
            return;
        }}
        
        // Show loading state
        container.innerHTML = '<div class="loading">正在加载 Markdown...</div>';
        
        try {{
            // Check if marked is already loaded
            let marked;
            if (window.marked) {{
                marked = window.marked;
            }} else {{
                // Load marked.js
                const markedModule = await import('https://esm.sh/marked@12.0.0');
                marked = markedModule.marked;
                window.marked = marked; // Cache for future use
            }}
            
            // Add CSS styles if not already added
            const styleId = 'markdown-styles-{abs(hash(css_styles))}';
            if (!document.getElementById(styleId)) {{
                const style = document.createElement('style');
                style.id = styleId;
                style.textContent = `{css_styles}`;
                document.head.appendChild(style);
            }}
            
            // Configure marked options
            marked.setOptions({{
                breaks: true,
                gfm: true,
                sanitize: false
            }});
            
            // Render markdown
            const content = {escaped_content};
            if (content && content.trim()) {{
                container.innerHTML = marked.parse(content);
            }} else {{
                container.innerHTML = '<p style="color: var(--gray-9, #999); font-style: italic;">暂无内容</p>';
            }}
            
        }} catch (error) {{
            console.error('Markdown rendering error:', error);
            container.innerHTML = `
                <div class="error">
                    <strong>渲染错误:</strong> ${{error.message || '未知错误'}}
                </div>
            `;
        }}
    }})();
    """
    
    # For dynamic content (state variables), we need to re-run the script when content changes
    if hasattr(content, '_var_name'):
        # Create a script that watches for content changes
        dynamic_js = f"""
        // Watch for content changes
        const watchContent = () => {{
            const currentContent = {escaped_content};
            if (window.lastMarkdownContent !== currentContent) {{
                window.lastMarkdownContent = currentContent;
                {js_code.replace('const content = ' + escaped_content, 'const content = currentContent')}
            }}
        }};
        
        // Initial render
        {js_code}
        
        // Set up periodic checking for content changes
        if (!window.markdownWatcher) {{
            window.markdownWatcher = setInterval(watchContent, 100);
        }}
        """
        
        return rx.box(
            rx.script(dynamic_js),
            rx.box(
                id=container_id,
                **props
            ),
            width="100%"
        )
    else:
        return rx.box(
            rx.script(js_code),
            rx.box(
                id=container_id,
                **props
            ),
            width="100%"
        )
