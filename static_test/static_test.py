import reflex as rx
from components.working_markdown import WorkingMarkdown

def static_test_page():
    """静态测试页面 - 不使用状态变量"""
    test_content = """# Reflex Markdown 组件测试

## 功能特性
- **静态渲染**: 不依赖状态变量
- **错误处理**: 显示加载状态和错误信息  
- **样式优化**: 美观的默认样式

## 代码示例
```python
def hello_world():
    print("Hello, Reflex!")
    return "欢迎使用 Reflex Markdown 组件"
```

## 列表示例
1. 第一项
2. 第二项
3. 第三项

### 无序列表
- 项目 A
- 项目 B
- 项目 C

## 表格示例
| 功能 | 状态 | 说明 |
|------|------|------|
| 标题渲染 | ✅ | 支持 H1-H6 |
| 代码高亮 | ✅ | 支持多种语言 |
| 表格 | ✅ | 支持基本表格 |

## 引用
> 这是一个引用示例
> 可以包含多行内容

## 自定义标签
<thinking>
这是一个思考标签，用于显示特殊内容
</thinking>

---

**这是一个静态测试页面，验证 Markdown 组件的基本功能。**
"""
    
    return rx.container(
        rx.heading("Reflex Markdown 组件 - 静态测试", size="8", margin_bottom="2rem"),
        
        rx.text(
            "这是一个静态内容测试页面，用于验证 Markdown 组件的基本功能。",
            color="gray",
            margin_bottom="2rem"
        ),
        
        WorkingMarkdown(
            content=test_content,
            padding="2rem",
            border="1px solid #e0e0e0",
            border_radius="8px",
            background_color="white",
            box_shadow="0 2px 4px rgba(0,0,0,0.1)"
        ),
        
        rx.box(
            rx.heading("测试结果", size="4", margin_bottom="0.5rem"),
            rx.unordered_list(
                rx.list_item("如果上面的内容正确显示，说明 Markdown 组件工作正常"),
                rx.list_item("支持所有标准 Markdown 语法"),
                rx.list_item("包含错误处理和加载状态显示"),
                rx.list_item("自定义 <thinking> 标签会特殊显示"),
                rx.list_item("如果显示错误信息，请检查浏览器控制台")
            ),
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

# 创建应用
app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="medium",
        scaling="100%"
    )
)

app.add_page(static_test_page, route="/", title="Markdown 静态测试")
