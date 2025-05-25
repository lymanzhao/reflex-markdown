import reflex as rx
from components.simple_markdown import SimpleMarkdown

def simple_test_page():
    """简单的静态测试页面"""
    test_content = """# 简单 Markdown 测试

这是一个**简单的测试**页面，用于验证 Markdown 组件是否正常工作。

## 功能测试

### 文本格式
- **粗体文本**
- *斜体文本*
- `行内代码`

### 列表
1. 第一项
2. 第二项
3. 第三项

### 代码块
```python
def hello_world():
    print("Hello, Reflex!")
    return "测试成功"
```

### 表格
| 功能 | 状态 |
|------|------|
| 标题 | ✅ |
| 列表 | ✅ |
| 代码 | ✅ |

### 引用
> 这是一个引用示例

### 自定义标签
<thinking>
这是一个思考标签测试
</thinking>

---

**如果你能看到这些内容正确渲染，说明组件工作正常！**
"""
    
    return rx.container(
        rx.heading("Reflex Markdown 组件 - 静态测试", size="8", margin_bottom="2rem"),
        
        rx.text(
            "这是一个静态内容测试页面，用于验证 Markdown 组件的基本功能。",
            color="gray",
            margin_bottom="2rem"
        ),
        
        SimpleMarkdown(
            content=test_content,
            padding="2rem",
            border="1px solid #e0e0e0",
            border_radius="8px",
            background_color="white",
            box_shadow="0 2px 4px rgba(0,0,0,0.1)"
        ),
        
        rx.box(
            rx.text("如果上面的内容正确显示，说明 Markdown 组件工作正常。", 
                   color="green", font_weight="bold"),
            rx.text("如果显示错误信息或加载状态，请检查浏览器控制台。", 
                   color="orange"),
            margin_top="2rem",
            padding="1rem",
            border="1px solid #ccc",
            border_radius="4px",
            background_color="#f9f9f9"
        ),
        
        max_width="800px",
        margin="0 auto",
        padding="2rem"
    )

# 创建简单的应用
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="medium",
        scaling="100%"
    )
)

app.add_page(simple_test_page, route="/", title="Markdown 静态测试")
